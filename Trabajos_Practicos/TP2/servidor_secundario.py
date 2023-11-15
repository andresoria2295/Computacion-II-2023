import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from PIL import Image
from io import BytesIO
import cgi
import os

#Función para crear un objeto ArgumentParser que manejará los argumentos de línea de comandos.
def parser():
    parser = argparse.ArgumentParser(description='Server secundario')

    #Agrega argumentos requeridos.
    parser.add_argument('-i', '--ip', required=True, help='Dirección IP')
    parser.add_argument('-p', '--port', required=True, type=int, help='Puerto')

    #Analiza los argumentos de línea de comandos proporcionados por el usuario.
    args = parser.parse_args()

    #Acceso a los valores ingresados por el usuario de los argumentos analizados.
    ip = args.ip
    port = args.port

    return ip, port

class ImageReceiverHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_type, _ = cgi.parse_header(self.headers['Content-Type'])
            content_length = int(self.headers['Content-Length'])
            #img_data = self.rfile.read(content_length)
            #self.wfile.write(b'Procesando solicitud POST..\n')
            #self.wfile.write(b'Procesando imagen recibida del servidor A..\n')

            #Configura el parser para obtener los datos del formulario enviado en la solicitud POST.
            data_img_form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST',
                             'CONTENT_TYPE': self.headers['Content-Type']}
                )

            #Extrae los datos del archivo de la solicitud POST.
            file_description = data_img_form['file']
            img_data = file_description.file.read()

            #Carga la imagen recibida.
            new_img = Image.open(BytesIO(img_data))

            #Redimensión de imagen.
            scale = float(self.headers['Factor-Escala'])
            print("Factor de escala:",scale)
            new_width = int(new_img.width * scale)
            new_height = int(new_img.height * scale)
            img_reduce = new_img.resize((new_width, new_height))

            #Envia la respuesta HTTP indicando que la operación fue exitosa.
            img_reduce.save("img_salida/imagen_reducida.jpg")
            img_reduce.save("imagen_reducida.jpg")

            #Envia la imagen redimensionada al servidor primario.
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            #self.wfile.write(b'Imagen despachada al servidor B.\n')

            #Convierte la imagen redimensionada a bytes y se envía.
            img_byte = BytesIO()
            img_reduce.save(img_byte, format='JPEG')
            bytes_imagen = img_byte.getvalue()
            self.wfile.write(bytes_imagen)

        except Exception as e:
            #Si hay un error, envía una respuesta de error al cliente.
            print(str(e))
            self.send_response(500)
            self.end_headers()
            self.wfile.write('Error en procesamiento de imagen: {}'.format(str(e)).encode())


if __name__ == "__main__":
    ip, port = parser()
    #server_address = (ip, port)
    httpd = HTTPServer((ip, port), ImageReceiverHandler)
    print("Servidor secundario B corriendo en puerto:", port)
    httpd.serve_forever()
