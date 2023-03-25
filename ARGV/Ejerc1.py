'''
1- Escribir un programa en Python que acepte un número de argumento entero positivo n y genere una lista
de los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar.
python3 Ejerc1.py -n 10
'''

#!/usr/bin/python3
import getopt
import sys

(opt,arg) = getopt.getopt(sys.argv[1:], 'n:')

'''
sys.stdout.write(str(len(sys.argv)))
print('\n')
sys.stdout.write(str(sys.argv[0]))
print('\n')
sys.stdout.write(str(sys.argv[1]))
print('\n')
sys.stdout.write(str(sys.argv[2]))
print('\n')
'''
numero = sys.argv[2]
lista = []
num = 1
#lista.append(num)

sys.stdout.write('\n Parámetro ingresado: '+numero)
sys.stdout.write('\n')

if int(numero)>0:
	for i in range(int(numero)):
		lista.append(num)
		num = num+2
		#lista.append(num)

	sys.stdout.write('\n Lista con números impares:')
	sys.stdout.write('\n')
	sys.stdout.write(str(lista))
	sys.stdout.write('\n')
else:
	sys.stdout.write('\n El parámetro ingresado debe ser número positivo.')
	sys.stdout.write('\n')

#print(opt)
#print(arg)
