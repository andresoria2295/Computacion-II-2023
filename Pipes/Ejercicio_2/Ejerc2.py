'''
2- Verificar si es posible que dos procesos hijos (o nieto) lean el PIPE del padre.
'''

#!/usr/bin/python3
import subprocess as sp
import os
import sys
import time

def main():
    #Creación de dos pipes uno por c/hijo.
    hijoA = sp.Popen(['python3', 'HijoA.py'], stdin=sp.PIPE)
    hijoB = sp.Popen(['python3', 'HijoB.py'], stdin=sp.PIPE)

    sys.stdout.write('\n Proceso padre (PID: %d) \n'% os.getpid())
    sys.stdout.write('\n')
    mensaje = "Soy el padre de ustedes."

    #Mandar mensaje por el pipe de entrada
    hijoA.stdin.write(mensaje.encode())
    hijoB.stdin.write(mensaje.encode())

    #Cerrar entrada del pipe
    hijoA.stdin.close()
    hijoA.wait()
    hijoB.stdin.close()
    hijoB.wait()
    #hijoA.stdin.close()
    #hijoA.wait()

    time.sleep(12)

if __name__ == "__main__":
    main()
