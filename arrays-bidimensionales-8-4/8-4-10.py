import array_utils
matriz= []
for fila in range(int(input("Cuántos almacenes hay?"))):
    matriz.append([])
    for columna in range(int(input(f"Cuántas piezas distintas hay en el almacen {fila + 1}?"))):
        matriz[fila].append(int(input(f"Cuántas piezas de tipo {columna + 1} hay en el almacén {fila + 1}?")))
matriz.append([])
for precio in range(len(matriz[0])):
    matriz[len(matriz) - 1].append(float(input(f"Cuáles son los costes totales de la pieza {precio + 1}?")))

print(f"El valor total general es de: {sum(matriz[len(matriz) - 1])}")
for columna in range (len(matriz)):
    valor_pieza = 0
    for fila in range(len(matriz[columna])):
        pieza_por_almacen = 0
        if fila != len(matriz) - 1:
            valor_pieza += matriz[fila][columna]
            print(f"Una pieza de tipo {columna + 1} vale: {matriz[fila][columna] / matriz[len(matriz) - 1][columna]} en el almacén {fila + 1}")
        else:
            valor_pieza = valor_pieza / matriz[fila][columna]
            print(f"Una pieza de tipo {columna + 1} es: {valor_pieza}")