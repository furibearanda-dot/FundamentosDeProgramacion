nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo (M para mujer, H para hombre): ")

if (sexo == 'M' and nombre < 'M') or (sexo == 'H' and nombre > 'N'):
    grupo = "A"
else:
    grupo = "B"

print("Te corresponde el grupo " + grupo)