# -*- coding: utf-8 -*-
'''
Script per tenir una consola per comandes AT
'''
import serial
import time
print "+------------------------------+"
print "| TEST SERIAL CONNECTION & SIM |"
print "+------------------------------+"

#obre serial
ser=serial.Serial()
ser.port="/dev/ttyS17"
ser.baudrate=9600
ser.bytesize=8
ser.parity=serial.PARITY_EVEN
ser.stopbits=1
ser.xonxoff=False
ser.rtscts=False
ser.dsrdtr=False
ser.timeout=1
ser.open()

#bucle comandes-respostes
while True:
    trama=raw_input("Escriu comanda AT > ") #string
    ser.write(trama+'\r') #envia tb carriage return
    time.sleep(1)
    resposta=''
    while ser.inWaiting()>0: resposta+=ser.read(1)
    print resposta, #sense newline
