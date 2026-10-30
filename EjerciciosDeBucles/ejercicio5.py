cantidad = float(input("Dime una cantidad a invertir: "))
interes = float(input("Dime el numero de interes que tienes: "))
numAños = int(input("Dime el numero de años: "))

for i in range(1, numAños + 1):
        cantidad = cantidad * (1 + interes / 100)
        print("numAños " + str(i) + " - Capital obtenido: " + str(round(cantidad, 2)))

