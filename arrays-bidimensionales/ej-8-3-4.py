import array_utils
matriz= []

filas = int(input("Cuántas filas va a tener la matriz? "))
columnas = int(input("Cuántas columnas va a tener la matriz? "))
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        matriz[i].append(int(input(f"Valor en posicion ({i + 1}, {j + 1}): ")))

array_utils.printMatrix(matriz)
print(array_utils.esIdentidad(matriz))