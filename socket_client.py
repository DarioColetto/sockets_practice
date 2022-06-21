import socket
s = socket.socket()
s.connect(("localhost", 9999)) 


mensaje = bytes(input("Escribe algo: "), 'utf-8')
s.send(mensaje)


print("adios")
s.close() 