'''
2- Escribir un programa en Python que acepte dos argumentos de línea de comando: una cadena de texto, un número entero.
El programa debe imprimir una repetición de la cadena de texto tantas veces como el número entero.
python3 Ejerc2.py -n 6 ---cadena como estas che
'''

#!/usr/bin/python3
import getopt
import sys

(opt,arg) = getopt.getopt(sys.argv[1:],'n:c:',["numero=","cadena="])

#numero = sys.argv[2]
'''
sys.stdout.write(str(len(sys.argv)))
print('\n')
sys.stdout.write(str(sys.argv[0]))
print('\n')
sys.stdout.write(str(sys.argv[1]))
print('\n')
sys.stdout.write(str(sys.argv[2]))
print('\n')
sys.stdout.write(str(sys.argv[3]))
print('\n')
sys.stdout.write(str(sys.argv[4:]))
'''

for op, ar in opt:
    if (op in ['-n', '--numero']):
        sys.stdout.write("\nNúmero entero ingresado: "+ar)
        sys.stdout.write('\n')
        numero = ar
    elif (op in ['-c', '--cadena']):
        sys.stdout.write("\nCadena de texto ingresada: "+ar)
        sys.stdout.write('\n')
        cadena = ar

#print('{}'.format(arg))

sys.stdout.write('\nRepetición de cadena de texto ingresada: ')
sys.stdout.write('\n')

for i in range(int(numero)):
	sys.stdout.write(' '.join(arg))
	sys.stdout.write('\n')
#print(opt)
#print(arg)
