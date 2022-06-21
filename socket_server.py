import socket
s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
sc, addr = s.accept()


recibido = sc.recv(1024)

print("Recibido: ", recibido)
sc.send(recibido)

print("adios")

sc.close()
s.close()

