'''
4- Continuar el ejercicio comenzado en clase para utilizar la salida de bajo nivel.
python3 Ejerc4.py < prueba.txt
python3 Ejerc4.py < /etc/services 2 > log (lo manda a archivo log)

'''

#!/usr/bin/python3
import sys
import os

while True:
    leido = (os.read(0,1024)).decode("utf-8")
    if len(leido) < 1024:
        print(leido, end = '')
        break;
    else:
        print(leido, end = '')

lectura = leido.split()
#os.open("Ejerc4Guardado.txt",os.O_WRITE)
with open("Ejerc4Guardado.txt", "w") as f:
    while True:
        os.write(1,1024)
        print(lectura, file=f)


#with open("errors.log", "w") as f:
#    print_exc(file=f)
