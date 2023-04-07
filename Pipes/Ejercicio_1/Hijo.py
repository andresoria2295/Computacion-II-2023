#!/usr/bin/python3
import sys

#Leer la entrada del pipe
i = 0

sys.stdout.write('\n Número de palabras por línea: \n')
sys.stdout.write('\n')
for line in sys.stdin:
    i = i + 1
    words = len(line.split())
    # mandamos por la salida del pipe la cantidad
    sys.stdout.write('Linea '+ str(i) + ': ' + str(words) + ' palabras. ' + '\n')
