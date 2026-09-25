dineroDepositado= float(input("Ingrese la cantidad de dinero depositado: "))
años= 3
interes= 4
capital= dineroDepositado * (1 + interes/100)**años
print(f"El capital obtenido después de {años} años es: {capital}")