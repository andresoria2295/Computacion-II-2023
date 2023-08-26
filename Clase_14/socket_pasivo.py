'''
Escribir un programa que implemente un socket pasivo que gestione de forma serializada distintas
conecciones entrantes. Debe atender nuevas conexiones de forma indefinida.
NOTA: cuando decimos serializado decimos que atiende una conexión y recibe una nueva conección
una vez que esa conexión se cerró.
'''

#!/usr/bin/python3
import socket
import time

def main():
    #Crear un objeto socket.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Asignación de IP y puerto al socket.
    s.bind(('0.0.0.0', 50001))
    #Número de conexiones que recibe. Socket de carácter pasivo.
    s.listen(1)
    while True:
        #Espera de múltiples conexiones de clientes.
        conn_client, address = s.accept()
        print("Conexión establecida con %s" % str(address))
        #Mensaje del servidor.
        msg = 'Mensaje del servidor: Hola! Soy el servidor. ¿En qué puedo ayudarte?.'
        print("Enviando mensaje al cliente...")
        conn_client.send(msg.encode('utf-8'))
        #Número de bytes a recibir.
        print("Esperando datos del cliente...")
        data_client = conn_client.recv(1024)
        print (data_client.decode('utf-8'))
        #conn_client.sendall(cod_msg)
        print("Cerrando conexión...\n")
        #Agrego tiempo para generar cola de peticiones de clientes serializadas.
        time.sleep(4)
        #Cierre de conexión.
        conn_client.close()

if __name__ == '__main__':
    main()
