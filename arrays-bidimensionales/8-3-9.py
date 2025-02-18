import math

import array_utils

matriz = []
salir = True
fila = 0
while fila < 20 and salir:
    columna = 0
    exponente = int(input("Introduzca exponente: "))
    if exponente != -1000:
        matriz.append([])
    #exponente = randint(1, 1000)
    while columna < 2 and salir:
        if exponente != -1000 and columna == 0:
            matriz[fila].append(exponente)
        elif exponente != -1000 and columna != 0:
            matriz[fila].append((math.pow(2, exponente)))
        else:
            salir = False
        columna += 1
    fila += 1

array_utils.printMatrix(matriz)