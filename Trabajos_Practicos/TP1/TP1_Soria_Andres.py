'''
Escriba un programa que abra un archivo de texto pasado por argumento utilizando el modificador -f.
* El programa deberá generar tantos procesos hijos como líneas tenga el archivo de texto.
* El programa deberá enviarle, vía pipes (os.pipe()), cada línea del archivo a un hijo.
* Cada hijo deberá invertir el orden de las letras de la línea recibida, y se lo enviará al proceso padre nuevamente, también usando os.pipe().
* El proceso padre deberá esperar a que terminen todos los hijos, y mostrará por pantalla las líneas invertidas que recibió por pipe.
* Debe manejar los errores.
Modo de uso: python3 fork_use.py -f consigna.txt
'''

#!/usr/bin/python3
import os
import sys
import argparse
import time

#Parseo de argumentos.
def ArgsParse():
    parser = argparse.ArgumentParser(description="Parseo de Argumentos")
    parser.add_argument("-f", "--file", dest="archivo",
                        required=True, help="Nombre del archivo")
    #parser.add_argument("-f", type=str, required=False, help="string")
    #args = parser.parse_args()
    #print('\nArchivo de texto: %s' % args.f)
    return parser.parse_args()

#Lectura de archivo de texto.
def LeerArchivo(nombreArchivo):
    try:
        fd = os.open(nombreArchivo, os.O_RDONLY)
        #Contar cantidad de palabras
        texto = (os.read(fd, 5000)).decode()
        palabras = texto.split()
        #Cantidad de Líneas
        lineas = texto.splitlines()
        line = len(lineas)

        #print(lineas)
        resultado = [line, lineas]
        #sys.stdout.write('\nnro de lineas: '+ str(line))
        return resultado

    except OSError as error:
        with open('errors.log', mode='w+') as errorFile:
            print(error, file=errorFile)
            sys.stdout.write('\n')

#Inversión de strings con recursividad
def inversor(input):
    if len(input) <= 1:
        return input

    return inversor(input[1:]) + input[0]

def main():
    argumento = ArgsParse()
    nombreArchivo = argumento.archivo
    resultado = LeerArchivo(nombreArchivo)
    line = resultado[0]
    sys.stdout.write('\nnro de lineas: '+ str(line))
    lineas = resultado[1]
    print(lineas)
    reverso = inversor(lineas[2])
    print(reverso)

    #fdr, fdw = os.pipe()

    #Creación de n hijos de acuerdo a lineas.
    for i in range(line):
        pid = os.fork()
        if pid == 0:
            #print('\nHijo ', i+1)
            reverso = inversor(lineas[i])
            print(reverso)
            #pipe_hijo_w = os.open(fif, os.O_WRONLY)
            #os.wait()


if __name__ == "__main__":
    main()
