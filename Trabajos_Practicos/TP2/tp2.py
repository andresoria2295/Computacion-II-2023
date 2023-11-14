#!/usr/bin/python3
import argparse
import os
import http.server
import socketserver
import threading
import io
from PIL import Image
from io import BytesIO
import multiprocessing
from multiprocessing import Event
import requests
import socket

#Define colas compartidas.
image_queue = multiprocessing.Queue()
processed_image_queue = multiprocessing.Queue()
conversion_event = Event()

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
    print('Dirección IP:', ip)
    print('Puerto:', port)
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

#Función que gestiona el envío de imagenes a servidor secundario.
def send_image(img_grises):
    try:
        #URL del segundo servidor.
        url = "http://localhost:5001"
        #Factor de escala para la imagen.
        scale = 0.4
        headers = {'Factor-Escala': str(scale)}

        #Convierte la imagen en bytes.
        img_byte = BytesIO()
        img_grises.save(img_byte, format='JPEG')
        bytes_imagen = img_byte.getvalue()
        #Configuración de los datos a enviar.
        files = {'file': ('imagen_recibida.jpg', bytes_imagen, 'image/jpeg')}
        #Realiza la solicitud POST al segundo servidor.
        response = requests.post(url, files=files, headers=headers)

        #Verifica si la solicitud fue exitosa.
        if response.status_code == 200:
            print("Imagen despachada al servidor B.")
        else:
            print("Error al enviar imagen al servidor B:", response.text)

    except Exception as e:
        print('Error al enviar imagen al servidor B:', e)

def process_image(image_queue, processed_image_queue, destino, scale, second_server_url):
    while True:
        #Procesos hijos desencolan las solicitudes, obtienen la imagen y procesan en paralelo.
        data_imagen = image_queue.get()
        try:
            #Abre la imagen desde los datos de la solicitud y la convierte a escala de grises.
            imagen = Image.open(BytesIO(data_imagen))
            img_grises = imagen.convert("L")

            #Define el nombre del archivo y la ruta completa de salida.
            nombre_archivo = "gray_image.jpg"
            ruta_completa = os.path.join(destino, nombre_archivo)

            #Guarda la imagen en escala de grises y obtiene los datos de la imagen procesada.
            with BytesIO() as buffer_salida:
                img_grises.save(ruta_completa, format="JPEG")
                data_imagen_gris = buffer_salida.getvalue()

            #Guarda la imagen en el servidor local con un nombre fijo.
            with open("gray_image.txt", "wb") as f:
                f.write(data_imagen_gris)

            #Pone los datos de la imagen en escala de grises en la cola correspondiente.
            processed_image_queue.put(data_imagen_gris)

            send_image(img_grises)

            #Establece el evento para indicar que la conversión de imagen ha terminado.
            conversion_event.set()

        except Exception as e:
            print('Error al abrir la imagen: {}'.format(e))
            return None

#Define una clase que hereda de http.server.BaseHTTPRequestHandler para manejar las solicitudes HTTP.
class ImageProcessingHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('REQUEST: ', self.requestline)

        try:
            #Desencola la imagen en escala de grises de la cola.
            data_imagen_gris = processed_image_queue.get()
            #Abre el archivo de imagen en escala de grises.
            with open("img_salida/gray_image.jpg", "rb") as f:
                #Lee el contenido del archivo.
                content = f.read()

            #Envía la respuesta HTTP con la imagen en escala de grises.
            self.send_response(200)
            self.send_header('Content-Type', 'image/jpg')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(b'Procesando solicitud GET..\n')
            self.wfile.write(content)
            #Envía la imagen al cliente.
            self.wfile.write(data_imagen_gris)

        except FileNotFoundError:
            #Si no se encuentra la imagen, envía un mensaje de error.
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Error: Imagen no encontrada.')

    def do_POST(self):
        print('REQUEST: ', self.requestline)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Procesando solicitud POST..\n')
        self.wfile.write(b'Procesamiento de imagen en curso..\n')

        #Obtiene el factor de escala y la URL del segundo servidor
        scale = float(self.headers.get('Scale-Factor', '0.5'))
        second_server_url = "http://localhost:5001"

        #Obtiene la longitud del contenido de la solicitud POST.
        contenido = int(self.headers["Content-Length"])
        #Lee los datos de la imagen de la solicitud POST.
        data_imagen = self.rfile.read(contenido)

        #Se asegura de que el evento no esté establecido antes de procesar la nueva imagen.
        #Garantiza que el servidor espere activamente a que ocurra el evento después de enviar la imagen para su procesamiento.
        conversion_event.clear()

        #Encola la imagen para su procesamiento.
        image_queue.put(data_imagen)

        try:
            #Define la ruta de la carpeta de destino.
            destino = "/home/andres/Documentos/Facultad/Computacion_II/Computacion_2023/GitHub/Computacion-II-2023/Trabajos_Practicos/TP2/img_salida"

            #Verifica si el directorio de destino existe, caso contrario, la crea.
            if not os.path.exists(destino):
                os.makedirs(destino)

            #Crea un nuevo proceso hijo (subproceso) para procesamiento de la imagen.
            process = multiprocessing.Process(target=process_image, args=(image_queue, processed_image_queue, destino, scale, second_server_url))
            process.start()

            #Espera a que el evento se establezca antes de continuar.
            conversion_event.wait()

            self.wfile.write(b'Imagen guardada en el servidor.\n')

        #Maneja cualquier excepción que pueda ocurrir al abrir la imagen y envía respuesta de error.
        except Exception as e:
            #Maneja errores en la creación del subproceso.
            print('Error al crear subproceso: {}'.format(e))

            #Error interno del servidor.
            self.send_response(500)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Error al procesar la imagen.\n')

#Define una función serve_forever_on_thread() que inicia el servidor HTTP en un hilo.
def serve_forever_on_thread(httpd, PORT):
    print('Corriendo servidor A en puerto:', PORT)
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
    #myhttphandler = ImageProcessingHandler
    httpd = http.server.HTTPServer((IP, PORT), ImageProcessingHandler)

    #Crea un hilo para gestionar el servidor HTTP.
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
        print('\nRecibiendo interrupción repentina. Deteniendo el servidor...')
        server_running = False

    #Detiene el servidor si no se ha detenido correctamente.
    if not server_running:
        stop_server(httpd)

if __name__ == '__main__':
    main()
