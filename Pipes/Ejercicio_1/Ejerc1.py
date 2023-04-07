'''
1- Escribir un programa en Python que comunique dos procesos.
El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo
a través de un pipe. El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas,
contar la cantidad de palabras que contiene y mostrar ese número.
'''

#!/usr/bin/python3
import os
import sys
import subprocess as sp

def main():

    #Crear el hijo con subprocess usando el programa hijo.py y pipe
    hijo = sp.Popen(['python3','./Hijo.py'], stdin=sp.PIPE)

    #Padre lee el archivo y escribe por entrada de pipe
    fdr = os.open('Consignas.txt', os.O_RDONLY)
    text = (os.read(fdr, 1024)).decode()
    sys.stdout.write('\n Lectura de documento: \n')
    sys.stdout.write('\n')
    sys.stdout.write(text)
    for line in text:
        hijo.stdin.write(line.encode())

    # cerrar el pipe de entrada
    hijo.stdin.close()
    hijo.wait()

if __name__ == "__main__":
    main()
