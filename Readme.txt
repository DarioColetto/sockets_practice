Se crearan los Socket SERVIDOR y CLIENTE. 


SERVIDOR:

1-Importar el modulo socket 
2-Crear un objeto socket para el SERVIDOR

    socket_server = socket.socket()

3-Indicar en qué puerto se va a mantener a la escucha nuestro servidor utilizando el método bind(hostname, port). Para sockets IP, como
es nuestro caso, el argumento de bind es una tupla que contiene el host y el puerto. El host se puede dejar vacío, indicando al método que
puede utilizar cualquier nombre que esté disponible.

    socket_server.bind(("localhost", 9999))

4-Utilizamos listen() para hacer que el socket acepte conexiones entrantes.Requiere de un parámetro que indica el número de conexiones máximas
que queremos aceptar; 
    
    socket_server.listen(10)

5-El método accept() para comenzar a escuchar. Se mantiene a la espera de conexiones entrantes, bloqueando la ejecución hasta que llega un mensaje.
Cuando llega un mensaje, accept desbloquea la ejecución, devolviendo un objeto socket que representa la conexión del cliente y una tupla que
contiene el host y puerto de dicha conexión.

    socket_connection, (host_c, puerto_c) = socket_s.accept()

6-Una vez que tenemos este objeto socket podemos comunicarnos con el cliente a través suyo, mediante los métodos recv() y send() 
que permiten recibir o enviar mensajes respectivamente. El método send toma como parámetros los datos a enviar,
mientras que el método recv toma como parámetro el número máximo de bytes a aceptar.
    recibido = socket_connection.recv(1024)
    print ("Recibido: ", recibio)
    socket_connection.send(recibido)

7-Una vez terminado el trabajo con el socket, lo cerramos con el método close().
    
    socket_server.close()
    socket_connection.close()

CLIENTE:

1-Importar el modulo socket 
2-Crear un objeto socket para el CLIENTE
3-Utilizar el método connect() para conectarnos al servidor y utilizar los métodos send() y recv() anteriores en SERVIDOR. El argumento
de connect es una tupla con host y puerto, exactamente igual que bind.
    socket_client = socket.socket()
    socket_client.connect(("localhost", 9999))
    socket_client.send("hola")
