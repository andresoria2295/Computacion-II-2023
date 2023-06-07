'''
Desarrollo en serie de Taylor para el seno(x).
El ejercicio consiste en crear tantos hilos como términos se desea calcular.
Luego, desde un hilo que no sea el main, se deben sumar todos los terminos calculados.
 Al finalizar esta operación el hilo main deberá mostrarlo por pantalla junto con la resta
 del valor de referencia. El valor de referencia, la cantidad de términos y los puntos a evaluar
 proporcionan a continuación:

Punto 1
- Cantidad de términos: 12
- x = 0.
- Valor de referencia: 0.0
Punto 2
- Cantidad de términos: 12
- x = 0.7853981633974483
- Valor de referencia: 0.7071067811865475
Punto 3
- Cantidad de términos: 12
- x = 1.5707963267948966
- Valor de referencia: 1.0000000000000002
Punto 4
- Cantidad de términos: 12
- x = 3.141592653589793
- Valor de referencia: -1.7028581387855716e-13
'''
#!/usr/bin/python3
import threading
import math

#Calculo de un término de la serie de Taylor para el seno(x).
def calculoTermino(n, x):
    coeficiente = (-1) ** n
    numerador = x ** (2 * n + 1)
    denominador = math.factorial(2 * n + 1)
    termino = coeficiente * numerador / denominador
    return termino

def agregarTermino(n, x, terminos, lock):
    """
    Calcula un término y lo agrega a la lista de terminos.
    """
    termino = calculoTermino(n, x)
    lock.acquire()
    terminos.append(termino)
    lock.release()

#Sumatoria de términos.
def sumaTerminos(terminos, ref):
    suma = sum(terminos)
    referencia = math.sin(x)
    resta = suma - ref
    print('Suma de los términos calculados:', suma)
    print('Resta con el valor de referencia:', resta)

#Cálculo de la serie de Taylor para sen(x) por hilos.
def calculoSerie(x, num_terminos, num_hilos, ref):
    hilos = []
    terminos = []
    lock = threading.Lock()

    for n in range(num_terminos):
        hilo = threading.Thread(target=agregarTermino, args=(n, x, terminos))
        hilos.append(hilo)
    #for n in range(num_terminos):
    #    thread = threading.Thread(target=lambda: terminos.append(calculoTermino(n, x)))
    #    hilos.append(thread)

    for i in range(0, num_terminos, num_hilos):
        for thread in hilos[i:i+num_hilos]:
            thread.start()

        for thread in hilos[i:i+num_hilos]:
            thread.join()

    sumaTerminos(terminos, ref)

#Valor de referencia para comparación.
ref = float(input('Ingresar el valor de referencia: '))
#referencia = math.sin(x)
x = float(input('Ingresar el valor de x: '))
#Número de términos a calcular.
num_terminos = 4
# Número de hilos a utilizar.
num_hilos = int(input('Ingresar el número de hilos a ejecutar: '))

calculoSerie(x, num_terminos, num_hilos, ref)
