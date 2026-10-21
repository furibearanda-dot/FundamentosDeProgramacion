edad = int(input("Dime tu edad: "))

if edad < 4:
    print("El cliente puede entrar gratis")
elif edad < 19:
    print("El precio a pagar es de 5€")
else:
    print("El precio a pagar es de 10€")