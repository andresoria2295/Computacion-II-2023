#!/usr/bin/python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='Tp2 - procesa imágenes')

    #Agregar argumentos requeridos.
    parser.add_argument('-i', '--ip', required=True, help='Dirección IP de escucha.')
    parser.add_argument('-p', '--port', required=True, help='Puerto de escucha.')

    args = parser.parse_args()

    #Acceso a los valores ingresados por el usuario.
    ip = args.ip
    port = args.port

    #Uso de valores ingresados.
    print('Dirección de escucha:',ip)
    print('Puerto de escucha:',port)

if __name__ == '__main__':
    main()
