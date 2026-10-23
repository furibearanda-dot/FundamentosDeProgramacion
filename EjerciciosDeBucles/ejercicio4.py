numero = int(input("Dime un numero entero positivo: "))

for i in range(numero, -1, -1):
    if i == 0:
        print(i)
    else:
        print(i, end=",")