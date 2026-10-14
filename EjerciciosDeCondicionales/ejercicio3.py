n1 = input("Dime el numero 1 (dividendo): ")
n2 = input("Dime el numero 2 (divisor): ")
resultadoD = n1/n2

if n2 == 0:
    print("Error, introduce un divisor válido distinto de 0.")
else:
    print("El resultado de la división es " + (resultadoD))