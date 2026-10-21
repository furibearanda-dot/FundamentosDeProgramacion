pizza = input("Quieres una pizza vegetariana?: ")

if pizza ==  "si":
    IngrVege = input("Los ingredientes disponibles para las pizzas vegetarianas son: Pimiento y tofu, cual quieres? ")
    print("Has elegido la pizza vegetariana, con el ingrediente " + IngrVege)
elif pizza == "no":
    IngrNoVege = input("Los ingredientes disponibles para las pizzas NO vegetarianas son: Peperoni, Jamon y Salmon, cual quieres? ")
    print("Has elegido la pizza NO vegetariana, con el ingrediente "+ IngrNoVege)
