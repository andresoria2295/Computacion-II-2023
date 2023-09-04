#!/usr/bin/python3
import socket

def connect_tcp_server(host, port):
    try:
        #Crear un socket TCP.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Conectar al servidor TCP.
        client_socket.connect((host, port))

        while True:
            #Recibir y mostrar la respuesta del servidor.
            dato = client_socket.recv(1024)
            print('Mensaje del servidor: ', dato.decode())
            #Leer datos del usuario.
            msg = input("Escribe un mensaje: ")
            #Enviar datos al servidor.
            client_socket.send(msg.encode())
            if msg.lower() == 'exit':
                dato = client_socket.recv(1024)
                print('Mensaje del servidor: ', dato.decode())
                break

    except Exception as e:
        print("Error: ", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 5000
    connect_tcp_server(server_host, server_port)
