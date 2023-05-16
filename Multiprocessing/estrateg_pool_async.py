'''
1- Realizar un programa que busque los números primos menores a 100.
Hacerlo usando al menos dos estrategias de Pool.
'''
#!/usr/bin/python3
import os
import time
from multiprocessing import Process, Pool

#Función que calcula identifica números primos.
def primo(numero):
    valor= range(2,numero)
    contador = 0
    for n in valor:
        if numero % n == 0:
            contador +=1
            #print("divisor:", n)
    if contador > 0:
        None
    else:
        primos.append(numero)
        print('El número '+str(numero)+' es primo. Resultado obtenido por H '+str(os.getpid())+'.')
        #print(primos)
        return numero

#Función que cada proceso toma un número de lista y chequea si es primo.
def fcPool(number):
    time.sleep(2)
    print('H: '+str(os.getpid()) + ' trabajando con número '+str(number)+'.')
    listado = primo(number)
    '''
    if number == 100:
        print('\nLista de números primos menores a 100: ')
        print(primos)
    '''
    return listado
    #Falta mostrar listado de primos.

def main():

    #Generación de lista con los primeros 100 números enteros.
    valores = list(range(2,101))
    #Generación de 5 procesos.
    pool = Pool(processes=5)
    resultado = pool.map_async(fcPool,valores)
    print(resultado.get(timeout=None))
    #for i in valores:
    #    primo(i)

if __name__ == "__main__":
    primos = []
    main()
