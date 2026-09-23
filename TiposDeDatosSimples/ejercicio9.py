cantidad= int(input("Dime una cantidad a invertir: "))
interes= float(input("dime el interes anual (en porcentaje): "))
naños= int(input("Dime el número de años: "))
capital= print(f"El capital obtenido es: {cantidad * (1 + interes/100)**naños}")