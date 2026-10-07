correo = input("Dime un correo: ")
dominio = correo.split('@')[0]
correoF = dominio + "@ceu.es"
print(correoF)