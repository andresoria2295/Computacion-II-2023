#!/usr/bin/python3
import socket

def connect_udp_server(host, port):
    try:
        #Crear un socket UDP.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:
            #Leer datos del usuario.
            msg = input("Escribe un mensaje: ")
            #Enviar datos al servidor UDP.
            client_socket.sendto(msg.encode(), (host, port))
            if msg.lower() == 'exit':
                dato, server_address = client_socket.recvfrom(1024)
                print('Respuesta del servidor: ', dato.decode())
                break

            #Recibir y mostrar la respuesta del servidor UDP.
            dato, server_address = client_socket.recvfrom(1024)
            print('Respuesta del servidor: ', dato.decode())

    except Exception as e:
        print('Error: ', e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 5000

    connect_udp_server(server_host, server_port)
