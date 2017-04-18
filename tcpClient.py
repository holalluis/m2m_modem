import socket
BUFFER_SIZE = 1024

#socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('88.31.135.237',1024))
print s
s.send('hola modem')

while True:
    missatge=raw_input("Escriu missatge (sortir: q) >> ")
    if(missatge=="q"): break
    s.send(missatge)

print "sortint"
s.close()
