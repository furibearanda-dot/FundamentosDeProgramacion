rendimiento = (input("dime tu puntucacion: "))
aceptable = 2400 * 0.4
meritorio = 2400 * 0.6

if  rendimiento == "0.0":
    print("Su rendimiento es inaceptable, no recibirá dinero extra.")
elif rendimiento == "0.4":
    print("Su rendimiento es aceptable, se lleva ", aceptable)
elif rendimiento >= "0.6":
    print ("Su rendimiento es meritorio, se lleva ", meritorio)