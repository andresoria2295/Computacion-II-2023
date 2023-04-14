'''
3- Verificar si el PIPE sigue existiendo cuando el padre muere (termina el proceso),
cuando el hijo muere [o cuendo mueren ambos]
$ ls -l /proc/[pid]/fd/
'''

#!/usr/bin/python3
import os
import sys
import subprocess as sp
import time

def main():
    HijoA = sp.Popen(['python3', 'HijoA.py'], stdin=sp.PIPE)
    hijoB = sp.Popen(['python3', 'HijoB.py'], stdin=sp.PIPE)

    sys.stdout.write('\n Proceso padre (PID: %d) \n'% os.getpid())
    sys.stdout.write('\n')
    mensaje = "Soy el padre de ustedes."

    #Cerrar el pipe de entrada
    HijoA.stdin.write(mensaje.encode())
    hijoB.stdin.write(mensaje.encode())

    cp_ls = sp.Popen(['ls -la /proc/' + str(os.getpid()) + '/fd'], shell=True, stdout=sp.PIPE)
    cp_grep = sp.Popen(['grep', 'pipe'], stdin=cp_ls.stdout)

    #pid = os.getpid() + 1
    print(cp_ls)
    print(cp_grep)

    # cerramos stdin para que no se quede esperando
    hijoB.stdin.close()
    hijoB.wait()
    HijoA.stdin.close()
    HijoA.wait()
    time.sleep(12)


if __name__ == "__main__":
    main()
