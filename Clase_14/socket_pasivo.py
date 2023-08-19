'''
Escribir un programa que implemente un socket pasivo que gestione de forma serializada distintas
conecciones entrantes. Debe atender nuevas conexiones de forma indefinida.
NOTA: cuando decimos serializado decimos que atiende una conexión y recibe una nueva conección
una vez que esa conexión se cerró
'''

#!/usr/bin/python3
import socket

def main():
    #Crear un objeto socket.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Asignación de IP y puerto al socket.
    s.bind(('0.0.0.0', 50010))
    #Número de conexiones que recibe. Socket de carácter pasivo.
    s.listen(2)
    #Espera de conexión del cliente.
    connect, address = s.accept()
    #Número de bytes a recibir.
    data = connect.recv(1024)
    #Mensaje del servidor.
    msg = 'Servidor recibiendo.\n'
    cod_msg = msg.encode('utf-8')

    connect.sendall(cod_msg)
    #Cierre de conexión.
    connect.close()

if __name__ == '__main__':
    main()
