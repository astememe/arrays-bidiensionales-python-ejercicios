import array_utils

matriz = []
for i in range(10):
    matriz.append([])
    for j in range(10):
        if i%2 == 0:
            matriz[i].append(1)
        else:
            matriz[i].append(0)

array_utils.printMatrix(matriz)