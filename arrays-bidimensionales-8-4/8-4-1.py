import array_utils

def generar_cuadrado_magico(orden):
    cuadrado_magico = []
    for fila in range(orden):
        cuadrado_magico.append([])
        for columna in range(orden):
            cuadrado_magico[fila].append(0)
    cuadrado_magico[0][int(orden/2)] = 1

    fila = 0
    columna = int(orden/2)
    for numero in range(2, orden ** 2 + 1):
        nueva_fila = fila - 1
        nueva_columna = columna + 1
        if nueva_fila < 0:
            nueva_fila = orden - 1
        if nueva_columna >= orden:
            nueva_columna = 0
        if cuadrado_magico[nueva_fila][nueva_columna] != 0:
            nueva_fila = fila + 1
            nueva_columna = columna
        if nueva_fila >= orden:
            nueva_fila = 0
        cuadrado_magico[nueva_fila][nueva_columna] = numero
        fila, columna = nueva_fila, nueva_columna
    return cuadrado_magico


n = int(input("Introduce el orden impar del cuadrado mágico: "))
if n % 2 == 1:
    cuadrado_magico = generar_cuadrado_magico(n)
    array_utils.printMatrix(cuadrado_magico)
else:
    print("El número debe ser impar.")
