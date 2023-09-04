'''
1 - Realizar un programa que implemente un servidor TCP o UDP usando socketserver.
El servidor puede ser un servidor de mayúsculas, un codificador en rot13 o cualquier otra tarea simple.
Se debe implementar concurrencia usanfo forking o threading.
'''
#!/usr/bin/python3
import socketserver
import threading

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 50001
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print('Server loop running:', server_thread.name)

    try:
        # Mantener el servidor en funcionamiento hasta que se presione Ctrl+C
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    # Apagar el servidor de manera ordenada
    server.shutdown()
