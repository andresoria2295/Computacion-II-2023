'''
En el ejercicio de la clase 15 se proponía el siguiente ejercicio:
**Realizar dos versiones de un servidor de mayúsculas que atienda múltiples clientes de
forma concurrente utilizando multiprocessing y threading utilizando sockets TCP.**
1- Actualizar el servidor para que funcione indistintamente con IPv4 e IPv6
Ej cliente: telnet ::1 50010
'''

#!/usr/bin/python3
import socket
import threading

def thserver(cliente):
    sock, addr = cliente
    try:
        while True:
            msg_cliente = sock.recv(1024)
            print("Mensaje recibido: %s de %s" % (msg_cliente.decode(), addr))
            decoded_original = msg_cliente.decode()
            # Strip() elimina espacios en blanco alrededor
            decoded = msg_cliente.decode().strip()
            if decoded == "exit":
                print("Cerrando conexión con %s\n" % str(addr))
                sock.send("Conexión finalizada.".encode('utf-8'))
                sock.close()
                # Cerrar la conexión para finalizar este proceso hijo
                break
            else:
                msg_server = decoded_original.upper()
                sock.send(msg_server.encode('utf-8'))
    except:
        print("Error en la conexión con %s" % str(addr))
        sock.close()

def main():
    #Creación de socket que admita tanto IPv4 como IPv6.
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Escuchar en todas las interfaces disponibles, incluyendo IPv4 e IPv6.
    s.bind(('', 50010))
    s.listen(5)
    hilos = []
    print("Servidor en linea.")
    try:
        while True:
            cliente = s.accept()
            conn_client, address = cliente
            print("\nConexión establecida con %s" % str(address))
            msg = 'Conexión exitosa: Hola! Soy el servidor. ¿En qué puedo ayudarte?.\n'
            print("Enviando mensaje al cliente...")
            conn_client.send(msg.encode('utf-8'))
            th = threading.Thread(target=thserver, args=(cliente,))
            th.start()
            hilos.append(th)

    except KeyboardInterrupt:
        print("\nCerrando conexiones...")
        for h in hilos:
            # Espera a que el hilo termine.
            h.join()

        s.close()
        print("Servidor cerrado.")

if __name__ == '__main__':
    main()
