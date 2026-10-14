edad  = int(input("Dime tu edad: "))
ingresosM = int(input("Dime tus ingresos mensuales: "))

if edad >= 16 and ingresosM >= 1000:
    print ("El individuo puede tributar")
else:
    print ("El individuo NO puede tributar")