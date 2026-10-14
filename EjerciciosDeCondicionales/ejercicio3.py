n1 = int(input("Dime el numero 1 (dividendo): "))
n2 = int(input("Dime el numero 2 (divisor): "))


if n2 == 0:
    print("Error, introduce un divisor válido distinto de 0.")
else:
    resultadoD = n1/n2
    print("El resultado de la división es ", resultadoD)