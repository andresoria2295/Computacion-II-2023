'''
3- Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto. El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar.
Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo. Esta última opción no debe ser obligatoria.
Si hubiese errores deben guardarse el un archivo cuyo nombre será "errors.log" usando la redirección de la salida de error.
python3 Ejerc3.py --lectura Consignas.txt -p
python3 Ejerc3.py -l Consignas.txt -p(opc)
python3 Ejerc3.py < Consignas.txt 2 > errorslog (lo manda a archivo log)
'''

#!/usr/bin/python3
import sys
import os
import getopt
from traceback import print_exc

try:
    (opt,arg) = getopt.getopt(sys.argv[1:],'l:p',["lectura="])
    #print(opt)
    #print(arg)
    promedio = 0

    for op, ar in opt:
        if (op in ['-l', '--lectura']):
            sys.stdout.write("\nArchivo de texto ingresado: "+ar)
            sys.stdout.write('\n')
            texto = ar
        elif (op in ['-p']):
            #sys.stdout.write("\nLongitud promedio de palabras: "+ar)
            #sys.stdout.write('\n')
            promedio = ar

    #archivo = open(texto, mode = 'r')
    #archivo = open('texto.txt',mode = 'r') (alto nivel)
    fd = os.open(texto,os.O_RDONLY)
    #lectura = archivo.read() (alto nivel)
    lectura = os.read(fd, 10000)
    #sys.stdout.write(lectura)
    sys.stdout.write('\n')

    #Cantidad de palabras
    cant_palabras = lectura.split()
    #cant_palabras = lectura.split(" ")
    #print(palabras)
    palabras = len(cant_palabras)

    #Promedio de palabras
    prom = sum(len(i) for i in cant_palabras)/len(cant_palabras)

    #Cantidad de Líneas
    #with open(texto) as archivo: (alto nivel)
    #    lineas = len(archivo.readlines())
    lineas = lectura.splitlines()
    line = len(lineas)

    sys.stdout.write("\nEl documento de texto posee " + str(palabras) + " palabras.")
    sys.stdout.write('\n')
    sys.stdout.write('\nTotal de lineas: ' + str(line))
    #print('Total de lineas: ' + str(lineas) + '.')
    sys.stdout.write('\n')

    #if sys.stdout.write(str(sys.argv[3])) == True:
    if promedio != 0:
        sys.stdout.write('\nLongitud promedio de palabras de archivo: '+ str(prom))
        #print('Total de lineas: ' + str(lineas) + '.')
        sys.stdout.write('\n')

    #os.close(fd)

#except ValueError: (alto nivel)
    #with open("errors.log", "w") as f:
    #    print_exc(file=f)

except os.error:
    sys.stdout.write('\nError en archivo: '+ texto)
    with open('errorslog', mode='w') as file_object:
        #print(file=file_object)
        print(texto, file=file_object) #Muestra solo el print de except
        sys.stdout.write('\n')
