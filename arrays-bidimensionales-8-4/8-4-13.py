matriz = [["+", "-", "*", "/", "=", "?","\\", "!", "¿", "$", "(", "@", "#"], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']]

def numToSymbol(vector):
    salida = ""
    for i in range(len(vector)):
        salida += matriz[0][matriz[1].index(vector[i])]
    print(salida)

def symbolToNum(vector):
    salida = ""
    for i in range(len(vector)):
        salida += matriz[1][matriz[0].index(vector[i])]
    print(salida)

opcion = int(input("Número a Símbolo: Introuce 1\nSímbolo a Número: Introduce 2\n"))
if opcion == 1:
    numToSymbol(input("Introduce los números separados por espacios\n").split(" "))
elif opcion == 2:
    symbolToNum(input("Introduce texto\n"))

