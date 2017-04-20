# -*- coding: utf-8 -*-
'''
M2M SERVER
# RESUM COMANDES
	at                                      #test device
	at+cmee=2                               #verbose error reporting
	at+cpin=1234                            #entra el pin
	at+creg?                                #regsitrat a la xarxa mobil? (0,1)
	at#scfg=1,1,300,90,600,50               #Set packet size and timeouts on context 1-6
	at#sgact=1,1,"apn","password"')         #registrar-se a APN
	at+cgpaddr=1                            #comprova ip assignada per apn
	at#frwl=1,"0.0.0.0","0.0.0.0"           #firewall: permet tot
	at#frwl=1,"1.2.3.4","255.255.255.255"') #firewall: permet que la ip 1.2.3.4 es connecti
	at#ss                                   #socket status (1,4,ip) 4 vol dir "listening"
	at#sl=1,1,1024,255                      #listen
	at#sa=1                                 #socket accept connection
	at#sh=1                                 #socket shutdown
'''
#parametres connexió
port="/dev/ttyS17" #cygwin (windows)
pin=4776
apn="movistar.es"
psw=""

#imports
import serial
import time
import sys

#inici
print "+--------------------+"
print "| Configuració modem |"
print "+--------------------+"
print "Port serie: ",port
print "SIM PIN:",pin
print "SIM APN:",apn
print "SIM psw:",psw

#crea connexió serial
ser=serial.Serial()
ser.port=port
ser.baudrate=115200
ser.bytesize=8
ser.parity=serial.PARITY_EVEN
ser.stopbits=1
ser.xonxoff=False
ser.rtscts=False
ser.dsrdtr=False
ser.timeout=1
ser.open()

#envia comanda AT, mostra resposta
def comanda(cmd):
    ser.write(cmd+'\r')
    time.sleep(1)
    resposta=''
    while ser.inWaiting()>0: resposta+=ser.read(1)
    print resposta, #sense newline

#escolta el modem via serial
def escolta():
    print "Escoltant modem..."
    while True:
        resposta=''
        while ser.inWaiting()>0: resposta+=ser.read(1)
        if(resposta!=''):
            print resposta
            if(resposta.find("NO CARRIER")+1): return
        time.sleep(1)

#menu usuari per comandes AT predefinides
def select():
    print "\n[+] Tria una opció"
    comandes={
        'a':'at',
        'b':'at+cmee=2',
        'c':'at+cpin='+str(pin),
        'd':'at+creg?',
        'e':'at#sgact=1,1,"'+apn+'","'+psw+'"',
        'f':'at+cgpaddr=1',
        'g':'at#frwl=1,"0.0.0.0","0.0.0.0"',
        'h':'at#ss',
        'i':'at#sl=1,1,1024,255',
        'j':'at#sa=1',
        'k':'at#sh=1',
        'l':'at#scfg=1,1,300,90,600,50',
				'x':'comanda AT custom',
        'y':'ESCOLTAR MODEM',
        'z':'SORTIR',
         '':'MOSTRAR COMANDES'
    };
    triada=raw_input('>> ')
    if(triada==''): #mostra opcions
        for opt in comandes: print opt+") "+comandes[opt]
		elif triada=='x':
			  comanda(raw_input("Comanda: ")+'\r')
    elif(triada=='y'): #escoltar modem
        escolta()
    elif(triada=='z'): #sortir
        sys.exit()
    else: #comanda AT
        comanda(comandes[triada])

#main loop select
while True: select()


