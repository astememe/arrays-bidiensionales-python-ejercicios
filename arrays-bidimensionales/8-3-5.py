import random

import array_utils

matriz = []

for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(random.randint(1, 10))
array_utils.printMatrix(matriz)

for i in range(5):
    suma_fila = sum(matriz[i])
    print(f"Suma de la fila {i+1}: {suma_fila}")

for i in range(5):
    suma_columna = 0
    for j in range (5):
        suma_columna += matriz[j][i]
    print(f"Suma de la columna {i + 1}: {suma_columna}")