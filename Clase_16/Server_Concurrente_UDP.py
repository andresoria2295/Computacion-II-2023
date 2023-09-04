'''
1 - Realizar un programa que implemente un servidor TCP o UDP usando socketserver.
El servidor puede ser un servidor de mayúsculas, un codificador en rot13 o cualquier otra tarea simple.
Se debe implementar concurrencia usanfo forking o threading.
'''
#!/usr/bin/python3
import socketserver
import threading

class ThreadedUDPServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        datos, socket = self.request
        #Referencia al hilo actual.
        cur_thread = threading.current_thread()
        #Almacenamiento de la dirección del cliente.
        client_address = self.client_address
        print('Cliente %s: %s se ha conectado. '%client_address)
        msg_inicial = "Conexión exitosa! Escribe 'exit' para desconectarte. "
        socket.sendto(msg_inicial.encode(), client_address)

        while True:
            datos, address = socket.recvfrom(1024)
            if not datos:
                break
            elif datos.decode() == 'exit':
                print('Cliente %s: %s ha solicitado cerrar la conexión. '%client_address)
                break
            else:
                print('Cliente %s: %s envió: %s '%(client_address[0], client_address[1], datos.decode()))

                #Convertir el texto a mayúsculas
                conversion = datos.decode().upper()
                socket.sendto(conversion.encode(), client_address)

        msg_final = 'Desconexión exitosa. Hasta luego!'
        socket.sendto(msg_final.encode(), client_address)
        print('Conexión con cliente %s: %s cerrada. '%client_address)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5000

    #Crear el servidor UDP con concurrencia de hilos
    server = socketserver.ThreadingUDPServer((HOST, PORT), ThreadedUDPServerHandler)

    print('Servidor escuchando en %s: %s ' % (HOST, PORT))

    try:
        #Mantener el servidor en funcionamiento hasta que se presione Ctrl+C
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server_thread.join()
        #No esperar a que el hilo del servidor termine con server_thread.join()

    except KeyboardInterrupt:
        pass

    # Apagar el servidor de manera ordenada
    server.shutdown()
