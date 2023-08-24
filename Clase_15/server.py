#!/usr/bin/python3
import socket, sys, time, os
import signal

#Señal que se envía a un proceso cuando uno de sus hijos termina. La acción es ignorarla,
#lo que significa que el proceso padre no necesita realizar ninguna acción específica
#cuando un proceso hijo finaliza.
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

"""
    socket.AF_INET -> sockets tcp/ip
    socket.AF_UNIX -> sockets Unix (archivos en disco, similar a FIFO/named pipes)

    socket.SOCK_STREAM -> socket tcp, orientado a la conexion (flujo de datos)
    socket.SOCK_DGRAM -> socket udp, datagrama de usuario (no orientado a la conexion)
"""

# get local machine name
host = socket.gethostname()
#host = ""
#port = int(sys.argv[1])
port = 50001

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    print("Esperando conexiones remotas...")
    clientsocket,addr = serversocket.accept()

    print("Conexión desde %s" % str(addr))

    ret = os.fork()
    if not ret: # hijo
        msg = 'Bienvenido al server.'+ "\r\n"
        #clientsocket.send(msg.encode('ascii'))
        print("Esperando...")
        time.sleep(20)
        print("Enviando mensaje...")
        clientsocket.send(msg.encode('utf-8'))
        print("Cerrando conexión...")
        clientsocket.close()
        exit()
