'''
1- Escribir un programa en Python que comunique dos procesos.
El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo
a través de un pipe. El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas,
contar la cantidad de palabras que contiene y mostrar ese número.
'''

#!/usr/bin/python3
import os
import sys
#import subprocess as sp

lectura = []
datos = []
def main():
    fdr, fdw = os.pipe()
    pid = os.fork()

    if pid == 0:
        print('Proceso hijo (PID: %d -- PPID: %d) '% (os.getpid(), os.getppid()))
        os.close(fdw)
        while True:
            recibido = (os.read(fdr,1024)).decode("utf-8")
            if len(recibido) == 0:
                break
            '''
            if len(leido) < 1024:
                #print(leido, end = '')
                lectura.append(leido)
                break;
            else:
                #print(leido, end = '')
                lectura.append(leido)
            '''
            lin = recibido.splitlines()
            print(recibido)
            os.close(fdr)
        #Cantidad de palabras
        #palabras = lectura.split()
        #print(palabras)
        #palabras = len(cant_palabras)
        #print(palabras)
        #for ... por c/oswrite para mostrar nro palabra
        #data_bytes = str.encode(leido)
        #os.write(1,bytes(palabras))


    print('Proceso padre (PID: %d) '% os.getpid())
    os.close(fdr)
    while True:
        fd = os.open('Consignas.txt',os.O_RDONLY)
        leido = (os.read(fd,1024)).decode("utf-8")
        if len(leido) < 1024:
            #print(leido, end = '')
            lectura.append(leido)
            break;
        else:
            #print(leido, end = '')
            lectura.append(leido)
    lines = leido.splitlines()
    #for linea in lines:
	#       datos.append(linea.strip('\n'))
    #print(leido)

    data_bytes = str.encode(leido)
    #data_bytes = leido.encode()
    os.write(fdw,data_bytes)
    os.close(fdw)

if __name__ == "__main__":
    main()
