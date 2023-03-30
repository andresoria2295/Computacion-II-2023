'''
Realizar un programa que implemente fork junto con el parseo de argumentos.
Deberá realizar relizar un fork si -f aparece entre las opciones al ejecutar el programa.
El proceso padre deberá calcular la raiz cuadrada positiva de un numero y el hijo la raiz negativa.
python3 fork_use.py -f hola.txt -n 4
'''

#!/usr/bin/python3
import os
import argparse
import sys
import math
import cmath
import time

def main():
    parser = argparse.ArgumentParser(description="Parseo de Argumentos")

    parser.add_argument("-f", type=str, required=False, help="string")
    parser.add_argument("-n", "--number", type=int, default=0, help="numero")
    args = parser.parse_args()

    print('Indicador %s.' % args.f)
    print('Numero introducido: %d.' % args.number)
    print('\n')
    print('Proceso vigente: ', os.getpid())
    print('\n')
    #print(args.f)
    if(args.f != 'None'):
        print('entro al if')
        print('\n')

        bifurc = os.fork()
        if args.number > 0:
            if bifurc > 0:
                #print('Proceso padre: ', os.getpid())
                #time.sleep(2)
                print('Proceso padre (PID: %d) '% os.getpid())
                raizPos = cmath.sqrt(args.number)
                print('Resultado de raíz cuadrada positiva de '+ str(args.number) + ': ',raizPos)
                print('\n')

            elif bifurc == 0:
                print('Proceso hijo (PID: %d -- PPID: %d) '% (os.getpid(), os.getppid()))
                valor = args.number * (-1)
                raizNeg = cmath.sqrt(valor)
                print('Resultado de raíz cuadrada negativa de '+ str(args.number) + ': ',raizNeg)
                print('\n')
        elif args.number < 0:
            if bifurc > 0:
                #print('Proceso padre: ', os.getpid())
                #time.sleep(2)
                print('Proceso padre (PID: %d) '% os.getpid())
                raizPos = cmath.sqrt(args.number)
                print('Resultado de raíz cuadrada positiva de '+ str(args.number) + ': ',raizPos)
                print('\n')

            elif bifurc == 0:
                print('Proceso hijo (PID: %d -- PPID: %d) '% (os.getpid(), os.getppid()))
                valor = args.number * (-1)
                raizNeg = cmath.sqrt(valor)
                print('Resultado de raíz cuadrada negativa de '+ str(args.number) + ': ',raizNeg)
                print('\n')

if __name__ == "__main__":
    main()
