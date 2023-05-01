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
        lines = len(lineas)

        #print(lineas)
        resultado = [lines, lineas]
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
    lista_read = []
    lista_write = []
    indice = []
    indice2 = []
    id_process = 0
    argumento = ArgsParse()
    nombreArchivo = argumento.archivo
    resultado = LeerArchivo(nombreArchivo)
    lines = resultado[0]
    sys.stdout.write('\n Numero de lineas de archivo: '+ str(lines))
    lineas = resultado[1]
    sys.stdout.write('\n')
    #print(lineas)
    #Prueba parcial
    #reverso = inversor(lineas[2])
    #print(reverso)

    sys.stdout.write('\n Proceso Padre: '+ str(os.getpid()))
    sys.stdout.write('\n')
    fdrp, fdwp = os.pipe()

    #Creación de pipes de lectura y escritura por c/linea.
    for i in range(lines):
        fdr, fdw = os.pipe()
        lista_read.append(fdr)
        lista_write.append(fdw)

    #Funcion que se le pasa lines, lineas,lista_read no devuelve nada.
    #Creación de n hijos de acuerdo a lineas.
    for i in range(lines):
        pid = os.fork()
        id_process += 1
        indice.append(id_process)
        if pid == 0:
            pipe_r = os.fdopen(lista_read[i])
            line_read = pipe_r.readline()
            print('\n Proceso Hijo', i+1,'-', os.getpid())
            print('\n Linea ' + str(i+1) + ' capturada: ',line_read)
            #reverso = inversor(lineas[i])
            reverso = str(i+1)+": "+inversor(lineas[i])
            #print(reverso)
            #print('\n Hijo', i+1, 'retorna: ',reverso)
            os.write(fdwp,(reverso+"\n").encode("utf-8"))
            time.sleep(5)
            pipe_r.close()
            os._exit(0)
            #os.wait()

    #Envio de lineas a hijos.
    for i in range(lines):
        envio_linea = lineas[i]+"\n"
        os.write(lista_write[i], envio_linea.encode("utf-8"))
    for i in range(lines):
        os.wait()

    #Lectura por el pipe de lo resuelto por hijos.
    #for i in range(lines):
    while True:
        leido = os.read(fdrp, 1024)
        leido = leido.decode()
        lect_parcial = leido.split("\n")
        #Quitar última posicion vacía.
        lect_parcial.pop()
        #Ordenar lista.
        lect_parcial.sort()
        print(lect_parcial)
        #for i in lect_parcial:
        #    muestra = lect_parcial[i].split()
        #print(muestra)
        for i in indice:
            #print('Resultado de Hijo',indice[i-1],lect_parcial[i-1])
            print('Resultado de Hijo',lect_parcial[i-1])
        break;

if __name__ == "__main__":
    main()
