matriz = []
sumas_filas = []
sumas_columnas = []
suma_diagonal_principal = 0
suma_diagonal_secundaria = 0
esMagico = True

orden = int(input("Orden de la matriz"))
for fila in range (orden):
    matriz.append([])
    for columna in range(orden):
        matriz[fila].append(int(input(f"Numero en posicion [{fila + 1}, {columna + 1}]")))

for fila in range(orden):
    sumas_filas.append(sum(matriz[fila]))
    for columna in range(orden):
        if columna == 0:
            sumas_columnas.append(matriz[columna][fila])
        else:
            sumas_columnas[fila] += matriz[columna][fila]
        if fila == columna :
                suma_diagonal_principal += matriz[fila][columna]
        if fila + columna == orden - 1:
            suma_diagonal_secundaria += matriz[fila][columna]

for i in range(len(sumas_filas)):
    for j in range (len(sumas_columnas)):
        if sumas_filas[i] != sumas_columnas[j] or sumas_filas[i] != suma_diagonal_principal or sumas_columnas[j] != suma_diagonal_principal or sumas_filas[i] != suma_diagonal_secundaria or sumas_columnas[j] != suma_diagonal_secundaria or suma_diagonal_principal != suma_diagonal_secundaria:
            esMagico = False

if esMagico:
    print("Es Magico")
else:
    print("Sumas de filas: " + sumas_filas.__str__())
    print("Sumas columnas: " + sumas_columnas.__str__())
    print(suma_diagonal_principal)
    print(suma_diagonal_secundaria)