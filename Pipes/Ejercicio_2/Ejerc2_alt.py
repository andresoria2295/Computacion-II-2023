'''
2- Verificar si es posible que dos procesos hijos (o nieto) lean el PIPE del padre.
'''

#!/usr/bin/python3
import os
import time
# crear dos pipes uno para enviar y otro para recibir
pipe_l, pipe_w = os.pipe()
pipe_l2, pipe_w2 = os.pipe()

# crear un proceso hijo
pid = os.fork()
# crear otro hijo a partir del mismo padre
if pid != 0:
    pid = os.fork()

if pid == 0:
    #time.sleep(1)
    # Este es el proceso hijo
    # cerrar el pipe de salida
    os.close(pipe_w)
    os.close(pipe_w2)
    print('Proceso hijo (PID: %d -- PPID: %d) '% (os.getpid(), os.getppid()))
    # leer el mensaje enviado por el padre

    mensaje = os.read(pipe_l, 100)
    mensaje = os.read(pipe_l2, 100)
    print("El hijo recibio el mensaje:")
    print(mensaje.decode())
    # cerrar el pipe de entrada
    os.close(pipe_l)
    os.close(pipe_l2)
else:
    # Este es el proceso padre
    # cerrar el pipe de entrada
    os.close(pipe_l)
    os.close(pipe_l2)
    print('Proceso padre (PID: %d) '% os.getpid())
    # enviar un mensaje al hijo
    mensaje = "Hola, soy el padre"
    os.write(pipe_w, mensaje.encode())
    os.write(pipe_w2, mensaje.encode())
    # cerrar el pipe de salidas
    os.close(pipe_w)
    os.close(pipe_w2)
