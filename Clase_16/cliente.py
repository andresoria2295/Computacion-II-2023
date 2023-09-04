'''
1 - Realizar un programa que implemente un servidor TCP o UDP usando socketserver.
El servidor puede ser un servidor de mayúsculas, un codificador en rot13 o cualquier otra tarea simple.
Se debe implementar concurrencia usanfo forking o threading.
'''
#!/usr/bin/python3
import socket
import sys

#Dirección IP y puerto empleado por el servidor.
HOST, PORT = "127.0.0.1", 50001
data = " ".join(sys.argv[1:])

#Creación del objeto socket.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))


'''
    print("Estableciendo conexión con el servidor...")
    s.connect((host, port))
    print("Conexión estable.")

    #Recepción de datos del servidor.
    print("Esperando datos del servidor...")
    msg = s.recv(1024)
    print (msg.decode('utf-8'))
    msg_client = 'Mensaje de cliente: Soy el cliente nuevo.'
    print("Enviando mensaje al servidor...")
    s.send(msg_client.encode('utf-8'))
    print("Cerrando conexion...\n")
    #Cierre de conexión.
    s.close()
    '''
