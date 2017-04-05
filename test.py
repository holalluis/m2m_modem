# -*- coding: utf-8 -*-
'''
Script per fer una prova de mínims:
    1. Crear una connexió serial
    2. Enviar una trama
    3. Rebre una resposta

Comandes AT per testing (manual Siretta)
========================================
    "descripcio"
        > "Comanda"
        < "Respostes possibles"

    check serial port
        > AT
        < OK

    set verbose error reporting
        > AT+CMEE=2
        < OK

    get parameters
        > AT&V
        < [...] OK

    check pin registration
        > AT+CPIN?
        < +CPIN: READY
        < OK
        < +CME ERROR: SIM not inserted
        < +CME ERROR: SIM pin

    query firmware version
        > AT+GMR
        < Firmware version

    query imei number
        > AT+CGSN
        < IMEI number

    set network registration to 'ALL'
        > AT+COPS=0
        < OK

    check network registration
        > AT+CREG?
        < +CREG:0,1 (registered to local network)
        < +CREG:0,5 (registered to roaming network)
        < +CREG:0,0 (not registered to a network)
        < +CREG:0,2 (searching for a network)
        < +CREG:0,3 (registration is denied)

    check network signal strength
        > AT+CSQ
        < +CSQ: 23,1 (value>9 if successful)
        < +CSQ: 99,1 (value=99 if no signal)
        < +CSQ: 3,1 (value<9 if ther are network connectivity issues)

    check GPRS context availability
        > AT+CGATT?
        < +CGATT:1 (if successful)
        < OK

    set GPRS APN for your network
        >AT+CGDCONT=1,"IP","APN name"
        < OK

    connect to GPRS context
        > AT#SGACT=1,1,"APN username","APN password"
        < #SGACT:x.x.x.x
        < OK
        < ERROR

    setup tcp socket connection parameters
        > AT#SCFG:1,1,300,90,600,50
        < OK

    connect TCP socket to server ip address
        > AT#SD=1,0,xxxx,"y.y.y.y"
        < CONNECT
        < NO CARRIER
'''
import serial
print "+------------------------------+"
print "| TEST SERIAL CONNECTION & SIM |"
print "+------------------------------+"

#obre serial
ser=serial.Serial()
ser.port="/dev/ttyS5"
ser.baudrate=9600
ser.bytesize=8
ser.parity=serial.PARITY_EVEN
ser.stopbits=1
ser.xonxoff=False
ser.rtscts=False
ser.dsrdtr=False
ser.timeout=1
ser.open()

#bucle comandes/respostes
while True:
    trama=raw_input("Escriu comanda AT > ") #string
    ser.write(trama+'\r') #envia tb carriage return
    ser.flush()
    resposta=ser.readlines() #array
    for r in resposta: 
        print "<",str(r), #without newline
