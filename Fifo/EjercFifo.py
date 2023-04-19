'''
1- Escribir un programa que realice la multiplicación de dos matrices de 2x2.
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado
en una fifo indicando el indice del elemento. El padre deberá leer en la fifo y
mostrar el resultado final.
'''

#!/usr/bin/python3
import os
import sys
import time

def imprimirMatriz(matriz):
    for fila in matriz:
        for valor in fila:
            print(' ',valor, end=" ")
        print(" ")

def main():
    fifo_name = "fifo_matriz"
    listadoA = []
    listadoB = []
    matrizA = []
    matrizB = []
    lista_matrices = []
    matriz_resultante = []
    mat_total = []

    print('\n Ingresar valores para matriz A: ')
    for a in range(4):
        valor=int(input('\n '))
        listadoA.append(valor)
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

    #Generación de indices.
    indice_a = str(matrizA[0][0]) + "-" + str(matrizA[0][1]) + "-" + str(matrizB[0][0]) + "-" + str(matrizB[1][0])
    indice_b = str(matrizA[0][0]) + "-" + str(matrizA[0][1]) + "-" + str(matrizB[0][1]) + "-" + str(matrizB[1][1])
    indice_c = str(matrizA[1][0]) + "-" + str(matrizA[1][1]) + "-" + str(matrizB[0][0]) + "-" + str(matrizB[1][0])
    indice_d = str(matrizA[1][0]) + "-" + str(matrizA[1][1]) + "-" + str(matrizB[0][1]) + "-" + str(matrizB[1][1])

    valores = [indice_a, indice_b,
               indice_c, indice_d]

    if not os.path.exists(fifo_name):
        os.mkfifo(fifo_name)

    #Creación de 4 hijos por posiciones de matriz y cáculo de valores.
    for i in range(4):
        pid = os.fork()
        if pid == 0:
            posicion = str(i)
            matriz_calculo = valores[i]
            print('\nHijo ', i+1)
            indices = matriz_calculo.split("-")
            resultado = str(int(indices[0])*int(indices[2]) + int(indices[1])*int(indices[3]))
            indice_resultado = posicion + "-" + resultado

            #Escritura del pipe por el hijo usando fifo.
            pipe_hijo_w = os.open(fifo_name, os.O_WRONLY)
            print('\n')
            print("Enviando resultado - indice-valor: ", indice_resultado)
            if (i == 0):
                time.sleep(2)
            if (i == 1):
                time.sleep(4)
            if (i == 2):
                time.sleep(6)
            os.write(pipe_hijo_w,(indice_resultado+"\n").encode("utf-8"))
            os.close(pipe_hijo_w)
            os._exit(0)

    #Lectura del pipe por el padre.
    pipe_hijo_r = open(fifo_name, 'r')

    for i in range(4):
        os.wait()

    #Insertar valores de indices resultantes en matriz.
    for linea in pipe_hijo_r:
        linea = str(linea)[:-1]
        valor = linea.split("-")
        matriz_resultante.insert(int(valor[0]), valor[1])

    pipe_hijo_r.close()

    #Generar visualización de matriz resultante.
    filaT1 = matriz_resultante[:2]
    mat_total.append(filaT1)
    filaT2 = matriz_resultante[2:]
    mat_total.append(filaT2)

    print("\n Matriz Resultante: \n")
    imprimirMatriz(mat_total)

if __name__ == "__main__":
    main()
