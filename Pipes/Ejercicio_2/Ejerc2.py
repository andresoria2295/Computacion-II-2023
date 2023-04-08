'''
2- Verificar si es posible que dos procesos hijos (o nieto) lean el PIPE del padre.
'''

#!/usr/bin/python3
import subprocess as sp
import os
import sys
import time

def main():
    hijoA = sp.Popen(['python3', 'HijoA.py'], stdin=sp.PIPE)
    hijoB = sp.Popen(['python3', 'HijoB.py'], stdin=sp.PIPE)

    sys.stdout.write('\n Proceso padre (PID: %d) \n'% os.getpid())
    sys.stdout.write('\n')
    mensaje = "Soy el padre de ustedes."

    #Cerrar el pipe de entrada
    hijoA.stdin.write(mensaje.encode())
    hijoB.stdin.write(mensaje.encode())

    #Cerrar stdin para que no espere
    hijoA.stdin.close()
    hijoA.wait()
    hijoB.stdin.close()
    hijoB.wait()
    #hijoA.stdin.close()
    #hijoA.wait()

    time.sleep(10)

if __name__ == "__main__":
    main()
