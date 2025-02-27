def printMatrix(matriz):
    for fila in matriz:
        print(fila)

def printTraspuesta(matriz):
    matriz_traspuesta = []
    for i in range (len(matriz[1])):
        matriz_traspuesta.append([])
        for j in range(len(matriz)):
            matriz_traspuesta[i].append(matriz[i][j])
    for fila in matriz_traspuesta:
        print(fila)


def esIdentidad(matriz):
    identidad = True
    if len(matriz) != len(matriz[0]):
        identidad = False
        return identidad
    for i in range(len(matriz)):
        for j in range(len(matriz([]))):
            if i == j and matriz[i][j] != 1:
                identidad = False
                return identidad
            if i != j and matriz[i][j] != 0:
                identidad = False
                return identidad
    return identidad

def sumaFila(matriz):
    sumas = []
    for i in range(len(matriz)):
        sumas.append(sum(matriz[i]))

