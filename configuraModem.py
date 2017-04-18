# -*- coding: utf-8 -*-
'''m2m server'''
#posa el modem en modo escoltar
import serial
import time

#parametres
port="/dev/ttyS17"
pin=4776
apn="movistar.es"
psw=""
ipClient="84.89.63.102"

print "+-----------------+"
print "| configura modem |"
print "+-----------------+"
print "Port serie: ",port
print "SIM PIN:",pin
print "SIM APN:",apn
print "SIM psw:",psw

print ""

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

def comanda(cmd):
    continuar=raw_input("Enviar comanda ["+cmd+"]? (saltar: Enter, executar: s) ")
    if(continuar!="s"): return
    ser.write(cmd+'\r')
    time.sleep(1)
    resposta=''
    while ser.inWaiting()>0: resposta+=ser.read(1)
    print resposta, #sense newline

def escolta():
    print "Escoltant modem..."
    while True:
        resposta=ser.readlines()
        if(len(resposta)):
            print resposta
        else:
            print ".",
        time.sleep(1)

#script comandes at
comanda('at')
comanda('at+cmee=2')
comanda('at+creg?')
comanda('at+cpin='+str(pin))
comanda('at#sgact=1,1,"'+apn+'","'+psw+'"')
comanda('at+cgpaddr=1') #comprova ip assignada per apn
comanda('at#frwl=1,"'+ipClient+'","255.255.255.255"') #firewall
comanda('at#sl=1,1,1024,255') #listen
comanda('at#ss')
comanda('at#sa=1')

#fi script, escolta modem
escolta()
