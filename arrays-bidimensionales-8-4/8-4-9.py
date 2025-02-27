matriz = []
determinante = 0

for fila in range(3):
    matriz.append([])
    for columna in range(3):
        matriz[fila].append(int(input(f"Numero en posicion [{fila + 1}, {columna + 1}]")))

determinante += (matriz[0][0] * (matriz[1][1]*matriz[2][2] - matriz[1][2] * matriz[2][1]) - matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) + matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))
print(determinante)