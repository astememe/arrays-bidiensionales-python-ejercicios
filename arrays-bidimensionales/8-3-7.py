import array_utils

matriz = []

for fila in range(3):
    matriz.append([])
    nota = 0
    columna = 0
    while columna < 30 and nota != -1:
            nota = float(input(f"Clase {fila + 1}: Introduzca nota. Introduzca -1 si quiere pasar a la siguiente clase. "))
            if nota != -1:
                matriz[fila].append(nota)
            columna+=1
array_utils.printMatrix(matriz)

maximo = (max((max(matriz[0]), max(matriz[1]), max(matriz[2]))))
minimo = (min((min(matriz[0]), min(matriz[1]), min(matriz[2]))))

print(f"Nota máxima: {maximo}\nConseguida por:")
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == maximo:
            print(f"Alumno {columna + 1} del grupo {fila + 1}")

print(f"Nota mínima: {minimo}\nConseguida por:")
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == minimo:
            print(f"Alumno {columna + 1} del grupo {fila + 1}")