'''
Memoria Compartida
Etapa 1
Escribir un programa que reciba por argumento la opción -f acompañada de un path_file
El programa deberá crear un segmento de memoria compartida y generar dos hijos H1 y H2.
H1 deberá leer desde sdtin lo que ingrese el usuario, línea por línea, enviando una señal USR1
al padre en cada línea leida.
Una vez ingresada una línea, el proceso padre leerá la memoria compartida y mostrará la línea leida
por pantalla y enviará una señal USR1 a H2.
Al recibir la señal USR1, H2 leerá la línea desde la memoria compartida y la escribirá en mayúsculas
en el archivo recibido como argumento.
Etapa 2
Cuando el usuario introduzca "bye" en la terminal, H1 enviará al padre la señal USR2 y terminará.
Al recibir la señal USR2, el padre, la enviará a H2 que también terminará.
El padre esperará a ambos hijos y terminará también.
'''

#!/usr/bin/python3
import os
import sys
import argparse
import mmap
import signal
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

def lecturaPadre(signal,frame):
    sys.stdout.write('\n Proceso Padre: '+ str(os.getpid()))
    #Ubica en posición cero.
    area.seek(0)
    leido = area.read(16)
    print("Lectura de Padre de memoria compartida: ", leido)
    #Envío de señal usr1 a hijo 2.
    os.kill(pidH2, signal.SIGUSR1)

def H1(signal, frame):
    print("Hijo 1 operando...")
    linea = input("Ingresar una linea por teclado: ")
    if linea == "bye":
        #Envío de señal usr2 a padre.
        os.kill(os.getppid(), signal.SIGUSR2)
        exit()
    #Ubica en posición cero.
    area.seek(0)
    area.write(linea.encode())
    #Envío de señal usr1 a hijo padre.
    os.kill(os.getppid(), signal.SIGUSR1)

def H2(signal, frame):
    print("Hijo 2 operando...")
    #Ubica en posición cero.
    area.seek(0)
    leido = area.read(16)
    leido.decode()
    fdw = open(fileName, 'a')
    fdw.write(str(leido.decode('utf-8').upper())+"\n")
    area.seek(0)

def FinH1(signal, frame):
    exit()

def FinH2(signal, frame):
    exit()
'''
def padreEjecutaHijo1(s, f):
    os.kill(pidH1, signal.SIGUSR1)
'''
def concluyePadre(signal, frame):
    print("Ha finalizado la operación.")
    #Envío de señal usr2 a hijo 2 para que le de fin al mismo.
    os.kill(pidH2, signal.SIGUSR2)
    os.wait()
    os.wait()
    exit()

def main():
    #Recepción de argumento.
    argumento = ArgsParse()
    fileName = argumento.archivo


    #Generación de señal para lectura desde proceso padre.
    signal.signal(signal.SIGUSR1, lecturaPadre)
    #Generación de señal para lectura desde proceso padre.
    signal.signal(signal.SIGUSR2, concluyePadre)

    #Creación de procesos hijos
    pidH1 = os.fork()
    if pidH1 == 0:
        #Establecimiento de comportamientos de señales de hijo 1.
        signal.signal(signal.SIGUSR1, H1)
        signal.signal(signal.SIGUSR2, FinH1)
        while True:
            #El proceso duerme hasta que reciba una señal.
            signal.pause()

    pidH2 = os.fork()
    if pidH2 == 0:
        #Establecimiento de comportamientos de señales de hijo 2.
        signal.signal(signal.SIGUSR1, H2)
        signal.signal(signal.SIGUSR2, FinH2)
        while True:
            #El proceso duerme hasta que reciba una señal.
            signal.pause()

    time.sleep(5)
    while True:
        os.kill(pidH1, signal.SIGUSR1)
        time.sleep(8)

if __name__ == "__main__":
    #Mapeo de memoria.
    area = mmap.mmap(-1, 16)
    main()
