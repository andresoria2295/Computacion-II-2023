#!/usr/bin/python3
import argparse
import os
import http.server
import socketserver
import threading
from PIL import Image
from io import BytesIO

#Función para crear un objeto ArgumentParser que manejará los argumentos de línea de comandos.
def parser():
    parser = argparse.ArgumentParser(description='Tp2 - procesa imágenes')

    #Agregar argumentos requeridos.
    parser.add_argument('-i', '--ip', required=True, help='Dirección IP de escucha.')
    parser.add_argument('-p', '--port', required=True, type=int, help='Puerto de escucha.')

    #Analiza los argumentos de línea de comandos proporcionados por el usuario.
    args = parser.parse_args()

    #Acceso a los valores ingresados por el usuario de los argumentos analizados.
    ip = args.ip
    port = args.port

    #Uso de valores ingresados.
    print('Dirección de escucha:', ip)
    print('Puerto de escucha:', port)
    return ip, port

#Función para convertir imágenes a escala de grises.
def convert_to_grayscale(input_image_path, output_image_path):
    #Abre la imagen de entrada.
    imagen = Image.open(input_image_path)
    #Convierte la imagen a escala de grises.
    escala_gris = imagen.convert("L")
    #Guarda la imagen en una nueva ubicación.
    escala_gris.save(output_image_path)

def abrir_imagen(img):
    ruta = ("/home/andres/Documentos/Facultad/Computacion_II/Computacion_2023/GitHub/Computacion-II-2023/Trabajos_Practicos/TP2/img_salida/" + img)
    img = Image.open(ruta)
    img.show()

#Define una clase que hereda de http.server.BaseHTTPRequestHandler para manejar las solicitudes HTTP.
class ImageProcessingHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('REQUEST: ', self.requestline)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'hola mundo GET\n')
        self.wfile.write(b'Abriendo imagen..\n')
        abrir_imagen('gray_image.jpg')

    def do_POST(self):
        print('REQUEST: ', self.requestline)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'hola mundo POST\n')
        self.wfile.write(b'Procesando imagen..\n')

        #Obtiene la longitud del contenido de la solicitud POST.
        contenido = int(self.headers["Content-Length"])
        #Lee los datos de la imagen de la solicitud POST.
        data_imagen = self.rfile.read(contenido)

        try:
            #Abre la imagen desde los datos de la solicitud y la convierte a escala de grises.
            imagen = Image.open(BytesIO(data_imagen))
            img_grises = imagen.convert("L")
            #Define la ruta de la carpeta de destino.
            destino = "/home/andres/Documentos/Facultad/Computacion_II/Computacion_2023/GitHub/Computacion-II-2023/Trabajos_Practicos/TP2/img_salida"

            #Verifica si el directorio de destino existe, caso contrario, la crea.
            if not os.path.exists(destino):
                os.makedirs(destino)

            #Define el nombre del archivo y la ruta completa de salida.
            nombre_archivo = "gray_image.jpg"
            ruta_completa = os.path.join(destino, nombre_archivo)
            #Guarda la imagen en escala de grises y obtiene los datos de la imagen procesada.
            with BytesIO() as buffer_salida:
                img_grises.save(ruta_completa, format="JPEG")
                data_imagen = buffer_salida.getvalue()
            self.wfile.write(b'Imagen procesada y guardada en el servidor.\n')

            #Guarda la imagen en el servidor local con un nombre fijo.
            with open("gray_image.txt", "wb") as f:
                f.write(data_imagen)

        #Maneja cualquier excepción que pueda ocurrir al abrir la imagen y envía respuesta de error.
        except Exception as e:
            print('Error al abrir la imagen: {}'.format(e))
            self.send_response(400)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Error al procesar la imagen. Imagen invalida.\n')

#Define una función serve_forever_on_thread() que inicia el servidor HTTP en un hilo.
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

    #Configura el manejador de solicitudes HTTP y crea una instancia del servidor HTTP.
    myhttphandler = ImageProcessingHandler
    httpd = http.server.HTTPServer(('', PORT), myhttphandler)

    #Crea un hilo para manejar el servidor HTTP.
    httpd_thread = threading.Thread(target=serve_forever_on_thread, args=(httpd, PORT))
    httpd_thread.daemon = True

    #Inicia el hilo del servidor HTTP.
    httpd_thread.start()

    #Inicializa la bandera del servidor en funcionamiento.
    server_running = True

    try:
        #Espera a que el hilo termine.
        httpd_thread.join()

    #Maneja la interrupción de teclado y detiene el servidor.
    except KeyboardInterrupt:
        print('\nRecibiendo Ctrl+C. Deteniendo el servidor...')
        server_running = False
    #Detiene el servidor si no se ha detenido correctamente.
    if not server_running:
        stop_server(httpd)

if __name__ == '__main__':
    main()
