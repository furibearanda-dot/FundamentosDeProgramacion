nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))

costeT = precio * unidades

resultado = "El producto es {}, el precio {:9.2f}, las unidades son {:3d}, y el coste total es {:11.2f}".format(nombre, precio, unidades, costeT)

print(resultado)