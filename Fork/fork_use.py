'''
Realizar un programa que implemente fork junto con el parseo de argumentos.
Deberá realizar un fork si -f aparece entre las opciones al ejecutar el programa.
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

def calculoRaizPos(number):
    raizPos = cmath.sqrt(number)
    print('Resultado de raíz cuadrada positiva de '+ str(number) + ': ',raizPos)
    print('\n')
    return raizPos

def calculoRaizNeg(number):
    valor = number * (-1)
    raizNeg = cmath.sqrt(valor)
    print('Resultado de raíz cuadrada negativa de '+ str(number) + ': ',raizNeg)
    print('\n')
    return raizNeg

#Padre realiza raíz positiva de n, hijo realiza raíz negativa de n.
def forked(number):
    bifurc = os.fork()
    if number > 0:
        if bifurc > 0:
            print('Proceso padre (PID: %d) '% os.getpid())
            #print('Proceso padre: ', os.getpid())
            #time.sleep(2)
            raizPos = calculoRaizPos(number)

        elif bifurc == 0:
            print('Proceso hijo (PID: %d -- PPID: %d) '% (os.getpid(), os.getppid()))
            raizNeg = calculoRaizNeg(number)

    elif number < 0:
        if bifurc > 0:
            print('Proceso padre (PID: %d) '% os.getpid())
            #print('Proceso padre: ', os.getpid())
            #time.sleep(2)
            raizPos = calculoRaizPos(number)

        elif bifurc == 0:
            print('Proceso hijo (PID: %d -- PPID: %d) '% (os.getpid(), os.getppid()))
            raizNeg = calculoRaizNeg(number)

#Padre realiza todo el requerimiento.
def unforked(number):
    if number > 0:
        print('Proceso padre (PID: %d) '% os.getpid())
        raizPos = calculoRaizPos(number)
        raizNeg = calculoRaizNeg(number)


    elif number < 0:
        print('Proceso padre (PID: %d) '% os.getpid())
        raizPos = calculoRaizPos(number)
        raizNeg = calculoRaizNeg(number)

def main():
    #Parseo de argumentos.
    parser = argparse.ArgumentParser(description="Parseo de Argumentos")

    parser.add_argument("-f", type=str, required=False, help="string")
    parser.add_argument("-n", "--number", type=int, default=0, help="numero")
    args = parser.parse_args()

    print('Indicador %s.' % args.f)
    print('Numero introducido: %d.' % args.number)
    print('\n')
    print('Proceso vigente: ', os.getpid())
    print('\n')

    #Si -f es llamado nace proceso hijo, si -f no es llamado continua solo proceso padre.
    if(args.f != None):
        forked(args.number)
    else:
        unforked(args.number)


if __name__ == "__main__":
    main()
