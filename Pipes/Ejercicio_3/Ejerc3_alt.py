#!/usr/bin/python3

import subprocess as sp
import os
import sys
import time

hijoA = sp.Popen(['python3', 'HijoA.py'], stdin=sp.PIPE)
hijoB = sp.Popen(['python3', 'HijoB.py'], stdin=sp.PIPE)

print("Soy el padre -", os.getpid())
mensaje = "Ustedes son mis hijos"


# cerrar el pipe de entrada
hijoA.stdin.write(mensaje.encode())
hijoB.stdin.write(mensaje.encode())


cp_ls = sp.Popen(['ls -la /proc/'+str(os.getpid()) +
                 '/fd'], shell=True, stdout=sp.PIPE)
cp_grep = sp.Popen(["grep", "pipe"], stdin=cp_ls.stdout)

"""
Se crea el pipe del padre con cada hijo, pero si corro el comando para ver los pipes por shell
no me muestra el pipe del primer proceso hijo que se corrio
"""
time.sleep(4)
hpid = os.getpid() + 1
print("Hijo: ", hpid)
print("el 1: ", cp_grep)


cp_ls2 = sp.Popen(['ls -la /proc/'+str(hpid) +
                   '/fd'], shell=True, stdout=sp.PIPE)
cp_grep2 = sp.Popen(["grep", "pipe"], stdin=cp_ls2.stdout)

# cerramos stdin para que no se quede esperando
hijoB.stdin.close()
hijoB.wait()
hijoA.stdin.close()
hijoA.wait()

time.sleep(4)
