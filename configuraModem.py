# -*- coding: utf-8 -*-
'''
# M2M SERVER

Resum comandes utilitzades
at                                      #test device
at+cmee=2                               #verbose error reporting
at+cpin=1234                            #entra el pin
at+creg?                                #regsitrat a la xarxa mobil? (0,1)
at#sgact=1,1,"apn","password"')         #registrar-se a APN
at+cgpaddr=1                            #comprova ip assignada per apn
at#frwl=1,"1.2.3.4","255.255.255.255"') #firewall: permet que la ip 1.2.3.4 es connecti
at#ss                                   #socket status (1,4,ip) 4 vol dir "listening"
at#sl=1,1,1024,255                      #listen
at#sa=1                                 #socket accept connection
at#sh=1                                 #socket shutdown
'''
import serial
import time
import sys

#parametres connexió
port="/dev/ttyS17"
pin=4776
apn="movistar.es"
psw=""
ipClient="84.89.63.102" #client que es connectarà al modem

print "+--------------------+"
print "| Configuració modem |"
print "+--------------------+"
print "Port serie: ",port
print "SIM PIN:",pin
print "SIM APN:",apn
print "SIM psw:",psw
print "IP client permesa:",ipClient

#obre serial
ser=serial.Serial()
ser.port=port
ser.baudrate=9600
ser.bytesize=8
ser.parity=serial.PARITY_EVEN
ser.stopbits=1
ser.xonxoff=False
ser.rtscts=False
ser.dsrdtr=False
ser.timeout=1
ser.open()

#envia comanda AT i mostra resposta
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
            if(resposta=='+++'): return
        time.sleep(1)

#tria una opcio
def select():
    print "\n[+] Tria una opció"
    comandes={
        'a':'at',
        'b':'at+cmee=2',
        'c':'at+cpin='+str(pin),
        'd':'at+creg?',
        'e':'at#sgact=1,1,"'+apn+'","'+psw+'"',
        'f':'at+cgpaddr=1',
        'g':'at#frwl=1,"'+ipClient+'","255.255.255.255"',
        'h':'at#ss',
        'i':'at#sl=1,1,1024,255',
        'j':'at#sa=1',
        'k':'at#sh=1',

        'y':'ESCOLTAR MODEM',
        'z':'SORTIR',
         '':'MOSTRAR COMANDES'
    };
    triada=raw_input('>> ')
    if(triada==''): #mostra opcions
        for opt in comandes: print opt+") "+comandes[opt]
    elif(triada=='q'): #sortir
        sys.exit()
    elif(triada=='y'): #escoltar modem
        escolta()
    else: #comanda AT
        comanda(comandes[triada])

#loop select
while True: select()
