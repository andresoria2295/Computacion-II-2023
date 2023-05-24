'''
1 - Escribir un programa que genere dos hilos utilizando threading.
Uno de los hilos debera leer desde stdin el texto ingresado por el usuario y deberá escribirlo
en una cola de mensajes (queue).
El segundo hilo deberá leer desde la queue el contenido y encriptará dicho texto utilizando
el algoritmo ROT13 y lo almacenará en una cola de mensajes (queue).
El primer hilo deberá leer dicho mensaje de la cola y lo mostrará por pantalla.
ROT13
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
gato (claro)->(rot13) tngb
'''
#!/usr/bin/python3

import threading as th, queue
import time
import codecs

def enter():
    #colaIN = []
    print("\n Ingresar 3 lineas de texto.\n")
    for i in range (3):
        entrada = input()
        #colaIN.append(entrada)
        encolado.put(entrada)
    print("\n Hilo 1 encolando datos..\n")
    #if encolado_cript.empty() == False:
    time.sleep(15)
    print("\n Hilo 1 descargando datos encriptados..\n")
    for i in range(3):
        #lectura = codificado(i)
        #print(lectura)
        codificado = encolado_cript.get()
        print(codificado)

def encrypted():
    #colaOUT = []
    print("\n Hilo 2 cargando datos..\n")
    for i in range (3):
        recepcion = encolado.get()
        print(recepcion)
        msg = codecs.decode(recepcion, 'rot13')
        encolado_cript.put(msg)
    print("\n Hilo 2 codificando datos..\n")

def main():
    #cola = queue.Queue()
    t1 = th.Thread(target=enter)
    t2 = th.Thread(target=encrypted)
    t1.start()
    time.sleep(10)
    t2.start()
    #encolado.join()
    #encolado_cript.join()
    #t2.join()


if __name__ == '__main__':
    encolado = queue.Queue()
    encolado_cript = queue.Queue()
    main()
