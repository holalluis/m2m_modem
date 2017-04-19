import socket

ip_modem='88.31.159.2'
port_modem=1024

#crea socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip_modem,port_modem))

if(s):
    print s
    print "Socket connectat a",ip_modem+":"+port_modem

while True:
    missatge=raw_input("Escriu missatge (sortir: q) >> ")
    if(missatge=="q"): break
    s.send(missatge)

print "Sortint..."
s.shutdown(socket.SHUT_RDWR)
s.close()
