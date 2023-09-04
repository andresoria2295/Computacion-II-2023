'''
1 - Realizar un programa que implemente un servidor TCP o UDP usando socketserver.
El servidor puede ser un servidor de mayúsculas, un codificador en rot13 o cualquier otra tarea simple.
Se debe implementar concurrencia usanfo forking o threading.
'''
#!/usr/bin/python3
import socketserver
import threading

#Manejador de las solicitudes de clientes.
class ThreadedTCPServerHandler(socketserver.BaseRequestHandler):
    #Método que será llamado cuando se maneje una solicitud de cliente.
    def handle(self):
        #Referencia al hilo actual.
        cur_thread = threading.current_thread()
        #Almacenamiento de la dirección del cliente.
        client_address = self.client_address
        print('Cliente %s: %s se ha conectado. '%client_address)
        msg_inicial = "Conexión exitosa! Escribe 'exit' para desconectarte. "
        #El mensaje se convierte en bytes utilizando encode() y se envía al cliente utilizando self.request.sendall().
        self.request.sendall(msg_inicial.encode())

        while True:
            datos = self.request.recv(1024).strip()
            #Si datos está vacío, el cliente se ha desconectado, y se sale del bucle.
            if not datos:
                break
            elif datos.decode() == 'exit':
                print('Cliente %s: %s ha solicitado cerrar la conexión.'%client_address)
                msg_final = 'Desconexión exitosa. Hasta luego!'
                self.request.sendall(msg_final.encode())
                break
            else:
                #Se imprime el mensaje que el cliente envió junto con su dirección IP y puerto.
                print('Cliente %s: %s envió: %s'%(client_address[0], client_address[1], datos.decode()))
                #Convertir el texto a mayúsculas
                conversion = datos.decode().upper()
                #Envío de datos al cliente.
                self.request.sendall(conversion.encode())

        print('Conexión con cliente %s: %s cerrada.'% client_address)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5000

    #Crear el servidor TCP con concurrencia de hilos
    server = socketserver.ThreadingTCPServer((HOST, PORT), ThreadedTCPServerHandler)

    #Iniciar el servidor en un hilo
    server_thread = threading.Thread(target=server.serve_forever)
    #Asegura que el hilo del servidor se detenga cuando el programa principal termine su ejecución.
    server_thread.daemon = True
    server_thread.start()

    print('Servidor en linea escuchando en %s: %s'%(HOST, PORT))

    try:
        #Mantener el servidor en funcionamiento hasta que se presione Ctrl+C
        server_thread.join()
    except KeyboardInterrupt:
        pass

    #Apagar el servidor de manera ordenada
    server.shutdown()
