#!/usr/bin/python3
import sys
import os

#Leer la entrada del pipe
i = 0
sys.stdout.write('\n Proceso hijo (PID: %d) \n'% (os.getpid()))
sys.stdout.write('\n')
sys.stdout.write('\n Número de palabras por línea: \n')
sys.stdout.write('\n')

for line in sys.stdin:
    i += 1
    words = len(line.split())
    #Enviar por la salida del pipe la cantidad de palabras
    sys.stdout.write('Linea '+ str(i) + ': ' + str(words) + ' palabras. ' + '\n')
