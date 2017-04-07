#posa el modem en modo escoltar,
#mostra la ip
#mostra totes les dades que rebis
import serial
import time
print "+-----------------+"
print "| configura modem |"
print "+-----------------+"

#parametres
pin=4776
port="/dev/ttyS17"

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
    ser.write(cmd+'\r')
    time.sleep(1)
    resposta=''
    while ser.inWaiting()>0: resposta+=ser.read(1)
    print resposta, #sense newline

#script comandes at
comanda('at');
