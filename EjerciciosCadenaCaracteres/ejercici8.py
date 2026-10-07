precio = input("Dime un precio en euros y con dos decimales: ")
euros = precio.split(',')[0]
cts = precio.split(',')[-1]
print("El numero de euros es " + euros + " y los centimos " + cts )