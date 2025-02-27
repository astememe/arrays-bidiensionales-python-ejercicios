import array_utils

matriz1 = []
matriz2 = []
resultado = [[],[],[]]
suma = 0

for fila in range(3):
    matriz1.append([])
    matriz2.append([])
    for columna in range(3):
        matriz1[fila].append(int(input(f"Número de la matriz 1 en posicion [{fila + 1}, {columna + 1}]")))
        matriz2[fila].append(int(input(f"Número de la matriz 2 en posicion [{fila + 1}, {columna + 1}]")))

for fila in range(3):
    for columna in range(3):
        suma = 0
        for elemento in range(3):
            suma += matriz1[fila][elemento] * matriz2[elemento][columna]
        resultado[fila].append(suma)

array_utils.printMatrix(resultado)