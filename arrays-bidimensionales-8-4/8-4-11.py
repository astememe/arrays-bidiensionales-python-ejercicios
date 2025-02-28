matriz =[["Dólar", "Libra esterlina", "Yen", "Dirham"],[0.82, 1.072, 0.0075, 0.084]]
divisa_actual = input("Qué divisa tienes?")
cantidad_actual = float(input(f"Cantidad de {divisa_actual} que tienes: "))
divisa_querida = input("A qué divisa quieres convertir?")

cantidad_querida = cantidad_actual * matriz[1][matriz[0].index(divisa_querida)] / matriz[1][matriz[0].index(divisa_actual)]
print(cantidad_querida)

