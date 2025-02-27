import array_utils

matriz = []
suma = []
for fila in range(3):
    matriz.append([])
    for columna in range(4):
        matriz[fila].append(int(input(f"Número en posición [{fila + 1} , {columna + 1}]: ")))
    suma.append(sum(matriz[fila]))
print(matriz[suma.index(max(suma))])