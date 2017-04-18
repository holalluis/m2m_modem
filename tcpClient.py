import socket
BUFFER_SIZE = 1024

ip_modem='95.124.201.120'

#socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip_modem,1024))

print s

while True:
    missatge=raw_input("Escriu missatge (sortir: q) >> ")
    if(missatge=="q"): break
    s.send(missatge)

print "sortint"
s.close()
