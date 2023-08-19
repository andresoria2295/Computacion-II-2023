#!/usr/bin/python3

import socket

def main():
    #Creación del objeto socket.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Dirección ip Telnet.
    host = "127.0.0.1"
    #Puerto empleado por el servidor.
    port = 50010

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

if __name__ == '__main__':
    main()
