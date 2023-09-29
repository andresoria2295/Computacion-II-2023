'''
1 - Implementar un buscador de número primos. Deberá encontrar el número primo inmediátamente inferior
a un valor dado.
Debe implementarse utilizando concurrent.futures.
Deberán lanzarse distintos procesos que vayan probando desde 2 hasta el valor dado con pasos diferentes
para maximizar la posibilidad de encuentro en el menor tiempo.
'''
#!/usr/bin/python3
from __future__ import print_function
#Proporciona una API para trabajar con ejecución en paralelo y concurrencia.
import concurrent.futures

#Función que verifica si un número "n" es primo.
def primoID(n):
    #Los números primos comienzan desde 2, por lo que cualquier número menor o igual a 1 no puede ser primo.
    if n <= 1:
        return False
    #2 y 3 son números primos.
    elif n <= 3:
        return True
    #Ningún número primo (excepto 2 y 3) es divisible por 2 o 3.
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    #Mientras el cuadrado de i sea menor o igual a n.
    while i * i <= n:
        #Verifica la divisibilidad por i y i + 2 en cada iteración del bucle.
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    #Si no se encuentra que n sea divisible por i o i + 2 en el rango de 5 hasta la raíz cuadrada de n, se considera que n es primo y se devuelve True.
    return True

#Función que localiza el número primo inmediatamente inferior a un límite dado.
def buscadorPrimo(nro_limite):
    #Recorrer los números desde limit - 1 hacia abajo hasta el 1 (inclusive), con un paso de -1.
    for n in range(nro_limite-1, 1, -1):
        if primoID(n):
            return n
    return None

if __name__ == "__main__":
    nro_limite = int(input("Ingresar un valor límite: "))

    #Creación de un objeto ThreadPoolExecutor llamado executor. Proporciona un grupo de hilos en el que se ejecutan tareas en paralelo.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #Enviar una tarea para que se ejecute en el grupo de hilos. La fc buscadorPrimo() se ejecutará en el grupo de hilos con el argumento nro_limite.
        #Se adquiere un objeto "futuro" que representa el resultado de una tarea que se ejecutará a futuro.
        futuro = executor.submit(buscadorPrimo, nro_limite)
        print("Buscando el número primo inmediatamente inferior a {0}...".format(nro_limite))

        #Esperar hasta que la tarea haya terminado y se obtiene el resultado.
        resultado = futuro.result()

        #None representa la ausencia de un valor o la falta de un resultado.
        if resultado is not None:
            print("El número primo inmediatamente inferior a {0} es: {1}.".format(nro_limite, resultado))
        else:
            print("No se encontró ningún número primo inferior a {0}.".format(nro_limite))
