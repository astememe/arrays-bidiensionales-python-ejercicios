from random import randint

import array_utils

matriz = []

suma = randint(0,10)
for fila in range(10):
    matriz.append([])
    matriz[fila].append(suma)
    suma = 0
    for columna in range(14):
        matriz[fila].append(randint(0, 10))
        #matriz[fila].append(int(input("Introduce número ")))  #linea para dejar al usuario meter valores que el quiera
    suma = sum(matriz[fila])

array_utils.printMatrix(matriz)