#!/usr/bin/python3

import os

print('Proceso emisor (PID: %d) '% os.getpid())
#Ruta del archivo FIFO (pipe con nombre).
fifo_name = 'my_fifo'

# Mensaje a enviar
mensaje = """
1 - Escribir un programa que reciba un mensaje desde otro proceso usando fifo (pipes con nombre).
El proceso receptor deberá lanzar tantos hilos como líneas tenga el mensaje y deberá enviar
cada línea a los hilos secundarios. Cada hilo secundario deberá calcular la cantidad de caracteres
de su línea y COMPROBAR la cuenta de la línea anterior.
"""

# Abrir el FIFO para escritura.
fifo_file = open(fifo_name, 'w')

# Escribir el mensaje en el FIFO.
fifo_file.write(mensaje)

# Cerrar FIFO.
fifo_file.close()
