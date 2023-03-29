'''
4- Continuar el ejercicio comenzado en clase para utilizar la salida de bajo nivel.
python3 Ejerc4.py < prueba.txt
python3 Ejerc4.py < /etc/services 2 > log (lo manda a archivo log)
'''

#!/usr/bin/python3
import sys
import os
lectura = []

sys.stdout.write("\nLectura de documento: \n")
sys.stdout.write('\n')

while True:
    leido = (os.read(0,1024)).decode("utf-8")
    if len(leido) < 1024:
        print(leido, end = '')
        lectura.append(leido)
        break;
    else:
        print(leido, end = '')
        lectura.append(leido)

#os.open("Ejerc4Guardado.txt",os.O_WRITE)
sys.stdout.write("\nLectura de documento volcada a ArchivoLeido.txt")
sys.stdout.write("\n")

with open("ArchivoLeido.txt", "w") as f:
    for i in range(len(lectura)):
        print(lectura[i], file=f)
    sys.stdout.write('\n')

'''
new_file = open('Ejerc4Guardado.txt', 'w')
sys.stdout.write(lectura, file=new_file)
new_file.close()
'''
