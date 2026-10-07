fecha = input("Dime una fecha en formato dd/mm/aaaa  :")
dia = fecha.split('/')[0]
mes = fecha.split('/')[1]
año = fecha.split('/')[-1]

print("El dia es " + dia + ", el mes " + mes + " y el año " + año)