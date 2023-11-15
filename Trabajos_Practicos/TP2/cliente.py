#!/usr/bin/python3
import http.client
import argparse

def enviar_imagen(host, port, imagen_path, output_path, metodo):
    try:
        #Lee el contenido de la imagen binaria.
        with open(imagen_path, 'rb') as file:
            imagen_data = file.read()

        #Configura la conexión HTTP.
        conn = http.client.HTTPConnection(host, port)

        #Configura la ruta del recurso en el servidor.
        resource_path = "/"

        #Configura los encabezados de la solicitud.
        headers = {
            'Content-Type': 'application/octet-stream',
            'Content-Length': str(len(imagen_data))
        }

        if metodo == 'POST':
            #Realiza la solicitud POST.
            conn.request('POST', resource_path, body=imagen_data, headers=headers)
        elif metodo == 'GET':
            #Realiza la solicitud GET.
            conn.request('GET', resource_path)

        #Obtiene la respuesta del servidor.
        response = conn.getresponse()

        if metodo == 'GET':
            #Lee la respuesta del servidor y guarda en el archivo de salida.
            with open(output_path, 'wb') as output_file:
                output_file.write(response.read())
        else:
            #Imprime la respuesta del servidor para solicitudes POST.
            print(response.read().decode())

        #Cierra la conexión.
        conn.close()

    except Exception as e:
        print('Error al enviar imagen al servidor:', e)

if __name__ == '__main__':
    #Configura el argumento de línea de comandos para el nombre del archivo de salida.
    parser = argparse.ArgumentParser(description='Cliente HTTP para enviar/recibir imágenes desde un servidor.')
    parser.add_argument('-o', '--output', default='gray_image.jpg', help='Nombre del archivo de salida')
    parser.add_argument('-m', '--method', choices=['GET', 'POST'], default='POST', help='Método de solicitud (GET o POST)')

    #Agrega más argumentos según sea necesario.
    args = parser.parse_args()

    #Configura la dirección IP y puerto del servidor.
    servidor_host = "127.0.0.1"
    servidor_port = 1111

    #Configura la ruta de la imagen que deseas enviar al servidor.
    imagen_path = "img_entrada/prueba.jpg"

    #Llama a la función para enviar/recibir la imagen al/desde el servidor.
    enviar_imagen(servidor_host, servidor_port, imagen_path, args.output, args.method)
