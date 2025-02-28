import array_utils
matriz = []

fila_actual = 0
for i in range(5):
    filas = int(input(f"Cuántas ventas ha realizado el empleado {i + 1}? "))
    for fila in range(filas):
        matriz.append([])
        for columna in range(3):
            if columna == 0:
                matriz[fila_actual].append(input(f"Cuándo se realizó la venta nº{fila + 1} del empleado nº{i + 1}? "))
            elif columna == 1:
                matriz[fila_actual].append(i+1)
            else:
                matriz[fila_actual].append(int(input("Cuál fue el ingreso de esa venta? ")))
        fila_actual += 1
array_utils.printMatrix(matriz)

contador_empleado = 1
total_empresa = 0
total_vendedor = 0
num_ventas = 0
total_vector = []
ventas_medias = []
for i in range(1, len(matriz) + 1):
    num_ventas += 1
    if contador_empleado != matriz[i - 1][1]:
        contador_empleado += 1
        total_vector.append(total_vendedor)
        ventas_medias.append(total_vector[contador_empleado-1]/)
        total_vendedor = 0
        num_ventas = 0
    total_empresa += matriz[i - 1][2]
    total_vendedor += matriz[i - 1][2]


print(total_vector)
print(total_empresa)