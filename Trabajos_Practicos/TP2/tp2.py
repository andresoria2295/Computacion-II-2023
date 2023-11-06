#!/usr/bin/python3
import argparse
import http.server
import socketserver
import threading

def parser():
    parser = argparse.ArgumentParser(description='Tp2 - procesa imágenes')

    #Agregar argumentos requeridos.
    parser.add_argument('-i', '--ip', required=True, help='Dirección IP de escucha.')
    parser.add_argument('-p', '--port', required=True, type=int, help='Puerto de escucha.')

    args = parser.parse_args()

    #Acceso a los valores ingresados por el usuario.
    ip = args.ip
    port = args.port

    #Uso de valores ingresados.
    print('Dirección de escucha:',ip)
    print('Puerto de escucha:',port)
    return ip, port

class handler_manual(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('REQUEST: ', self.requestline)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'hola mundo GET\n')

    def do_POST(self):
        print('REQUEST: ', self.requestline)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'hola mundo POST\n')

def serve_forever_on_thread(httpd, PORT):
    print('Ejecutando servidor httpd en puerto:', PORT)
    httpd.serve_forever()

def stop_server(httpd):
    httpd.shutdown()
    httpd.server_close()

def main():
    global httpd
    global PORT
    global server_running

    IP, PORT = parser()
    socketserver.TCPServer.allow_reuse_address = True

    myhttphandler = handler_manual
    httpd = http.server.HTTPServer(('', PORT), myhttphandler)

    #Crea un hilo para manejar el servidor HTTP.
    httpd_thread = threading.Thread(target=serve_forever_on_thread, args=(httpd, PORT))
    httpd_thread.daemon = True

    #Inicia el hilo del servidor HTTP.
    httpd_thread.start()

    #Inicializa la bandera del servidor en funcionamiento
    server_running = True

    try:
        #Espera a que el hilo termine
        httpd_thread.join()

    except KeyboardInterrupt:
        print('\nRecibiendo Ctrl+C. Deteniendo el servidor...')
        server_running = False

    if not server_running:
        stop_server(httpd)

if __name__ == '__main__':
    main()
