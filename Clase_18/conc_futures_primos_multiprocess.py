'''
1 - Implementar un buscador de número primos. Deberá encontrar el número primo inmediátamente inferior
a un valor dado.
Debe implementarse utilizando concurrent.futures.
Deberán lanzarse distintos procesos que vayan probando desde 2 hasta el valor dado con pasos diferentes
para maximizar la posibilidad de encuentro en el menor tiempo.
'''
#!/usr/bin/python3
import concurrent.futures

#Función que verifica si un número es primo.
def primoID(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Función para buscar el número primo inmediatamente inferior de manera concurrente.
def buscadorPrimo(nro_limite):
    if nro_limite <= 2:
        return None

    #Creación de un objeto ProcessPoolExecutor llamado executor. Proporciona un grupo de hilos en el que se ejecutan tareas en paralelo.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        #Iterar desde nro_limite-1 hasta 2 con pasos negativos.
        for n in range(nro_limite-1, 1, -1):
            if executor.submit(primoID, n).result():
                return n

if __name__ == "__main__":
    nro_limite = int(input("Ingresar un valor límite: "))

    print("Buscando el número primo inmediatamente inferior a {0}...".format(nro_limite))

    resultado_final = buscadorPrimo(nro_limite)

    if resultado_final is not None:
        print("El número primo inmediatamente inferior a {0} es: {1}.".format(nro_limite, resultado_final))
    else:
        print("No se encontró ningún número primo inferior a {0}.".format(nro_limite))
