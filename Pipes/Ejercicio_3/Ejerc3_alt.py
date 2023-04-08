'''
3- Verificar si el PIPE sigue existiendo cuendo el padre muere (termina el proceso),
cuando el hijo muere [o cuendo mueren ambos]
$ ls -l /proc/[pid]/fd/
'''

#!/usr/bin/python3
import os
import time

def main():
    fdr, fdw = os.pipe()
    pid = os.fork()

    if pid == 0:
        time.sleep(5)
        # Este es el proceso hijo
        # cerrar el pipe de salida
        os.close(fdw)
        print('Proceso hijo (PID: %d -- PPID: %d) '% (os.getpid(), os.getppid()))
        # leer el mensaje enviado por el padre

        mensaje = os.read(fdr, 100)
        print("El hijo recibio el mensaje:")
        print(mensaje.decode())
        # cerrar el pipe de entrada
        os.close(fdr)

    os.close(fdr)
    print('Proceso padre (PID: %d) '% os.getpid())
    # enviar un mensaje al hijo
    mensaje = "Hola, soy el padre, pero ya morí."
    os.write(fdw, mensaje.encode())
    # cerrar el pipe de salidas
    os.close(fdw)


if __name__ == "__main__":
    main()
