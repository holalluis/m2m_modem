import socket
import select

#dades servidor (modem)
ip_modem='88.31.199.115'
port_modem=1024

#new socket
print "Connectant a ",ip_modem,"..."
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip_modem,port_modem))
s.setblocking(0)

#timeout per resposta del servidor
timeout_in_seconds=1

if(s):
    print "Socket connectat" 
    print s

while True:
    missatge=raw_input("Escriu missatge (sortir: <q>) >> ")
    if(missatge=="q"): 
        break
    #envia
    s.send(missatge)

    #resposta (sense select recv es queda parat)
    while True:
        ready=select.select([s],[],[],timeout_in_seconds)
        if ready[0]: 
            print s.recv(4096)
        else:
            break

print "Sortint..."
s.shutdown(socket.SHUT_RDWR)
s.close()
