'''
1- Escribir un programa que realice la multiplicación de dos matrices de 2x2.
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado
en una fifo indicando el indice del elemento. El padre deberá leer en la fifo y
mostrar el resultado final.
'''

#!/usr/bin/python3
import os
import sys
import subprocess as sp


pipe_name = '/tmp/pipe_test'
'''
#Suma de matrices
    A = [[12,7],
        [14,5]]
    B = [[5,8],
        [4,2]]
    result = [[0,0],
             [0,0]]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = (A[i][j] * B[i][j]) + (A[i][j+1] * B[i+1][j+1])

    for r in result:
        print(r)
'''

def productoMatrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])

    if columnas_a != filas_b:
        return None

    #Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = []

    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)

    #hijo.stdin.write(.encode())
    #Rellenar el producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto


def imprimirMatriz(matriz):
    for fila in matriz:
        for valor in fila:
            #Imprimir sin salto de línea. Usando un espacio al final
            print(' ',valor, end=" ")
        print(" ")

def hijo():
    pipeout1 = open(pipe_name, 'r')
    #line = pipein.readline()[:-1]
    recep1 = pipeout1.read(strlist)
    print(recep1)
    producto = productoMatrices(matrizA, matrizB)
    pipeout2 = open(pipe_name, 'w')
    pipeout2.flush()
    pipeout2.write(p)
    time.sleep(1)

def padre():
    listadoA = []
    listadoB = []
    matrizA = []
    matrizB = []
    lista_matrices = []

    sys.stdout.write('\n Proceso padre (PID: %d) \n'% os.getpid())
    #Crear el hijo con subprocess usando el programa hijo.py y pipe
    #hijoA = sp.Popen(['python3','./HijoA.py'], stdin=sp.PIPE)

    print('\n Ingresar valores para matriz A: ')
    for a in range(4):
        valor=int(input('\n '))
        listadoA.append(valor)
    #print(listadoA)
    filaA1 = listadoA[:2]
    matrizA.append(filaA1)
    filaA2 = listadoA[2:]
    matrizA.append(filaA2)
    print("\n Matriz A: \n")

    imprimirMatriz(matrizA)

    print('\n Ingresar valores para matriz B: ')
    for b in range(4):
        valor=int(input('\n '))
        listadoB.append(valor)
    #print(listadoB)
    filaB1 = listadoB[:2]
    matrizB.append(filaB1)
    filaB2 = listadoB[2:]
    matrizB.append(filaB2)
    print("\n Matriz B: \n")

    imprimirMatriz(matrizB)

    pipein1 = open(pipe_name, 'w')
    lista_matrices.append(matrizA)
    lista_matrices.append(matrizB)
    strlist = " ".join(lista_matrices)
    pipein1.write(strlist)
    pipein1.flush()
    time.sleep(1)

    pipein2 = open(pipe_name, 'r')
    producto = pipein2.read(p)
    #producto = productoMatrices(matrizA, matrizB)
    if producto:
        #Mostrar resultado
        print('\n Matriz resultante: \n')
        imprimirMatriz(producto)
    else:
        print("El número de columnas de A es distinto al número de filas de B.")


def main():
    pipe_name = '/tmp/pipe_test'

    if not os.path.exists(pipe_name):
        os.mkfifo(pipe_name)

    pid = os.fork()

    if pid != 0:
        padre()
    else:
        hijo()

if __name__ == "__main__":
    main()
