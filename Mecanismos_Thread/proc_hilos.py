'''
1 - Escribir un programa que reciba un mensaje desde otro proceso usando fifo (pipes con nombre).
El proceso receptor deberá lanzar tantos hilos como líneas tenga el mensaje y deberá enviar
cada línea a los hilos secundarios. Cada hilo secundario deberá calcular la cantidad de caracteres
de su línea y COMPROBAR la cuenta de la línea anterior.
'''

#!/usr/bin/python3

import os
import threading

#Ruta del archivo FIFO (pipe con nombre).
fifo_name = 'my_fifo'

#Mecanismo para la sincronización entre hilos.
#Garantiza que solo un hilo acceda a la sección crítica a la vez y evita problemas de concurrencia.
lock = threading.Lock()

def thread_task(line, prev_count, count_lines):
    #Cálculo de la cantidad de caracteres en la línea actual.
    caracteres = len(line.strip())

    #EL método acquire() adquiere el recurso (decrementa y bloquea) antes de realizar la comprobación.
    lock.acquire()
    try:
        #Comprobación de la cuenta de la línea anterior.
        if caracteres == prev_count:
            print('\nLínea '+str(count_lines)+': '+str(line.strip())+ '- Cantidad: '+str(caracteres)+ ' caracteres - Coincide con la cuenta de la línea anterior.\n')
        else:
            print('\nLínea '+str(count_lines)+': '+str(line.strip())+ '- Cantidad: '+str(caracteres)+ ' caracteres - NO coincide con la cuenta de la línea anterior.\n')
    finally:
        #El método release() libera el recurso (incrementa y desbloquea) después de que se haya completado la comprobación.
        lock.release()

def main():
    print('\n Proceso receptor (PID: %d) '% os.getpid())
    #Creación de FIFO si no existe.
    if not os.path.exists(fifo_name):
        os.mkfifo(fifo_name)

    #Abrir el FIFO para lectura.
    fifo_file = open(fifo_name, 'r')

    #Leer el mensaje desde el FIFO. Strip suprime blancos u otro carácter especificado
    #del final o del principio de una expresión de serie.
    mensaje = fifo_file.read().strip()

    #Cerrar el FIFO.
    fifo_file.close()

    #Splitear el mensaje en líneas.
    lines = mensaje.split('\n')

    #Lanzamiento de hilo para cada línea.
    prev_count = 0
    count_lines = 1
    for line in lines:
        thread = threading.Thread(target=thread_task, args=(line, prev_count, count_lines))
        thread.start()
        #Espera a que el hilo termine antes de continuar.
        thread.join()
        #Contador de lineas.
        count_lines+=1
        #Actualiza la cuenta de la línea anterior
        prev_count = len(line.strip())

if __name__ == '__main__':
    main()
