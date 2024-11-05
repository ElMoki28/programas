magicians=["El pelusa","voldemort","harry el sucio potter","colorado"]
print(magicians)
for mago in magicians:
    print(mago)
    print(mago.upper()+" ese fue un gran hechizo.")
    print(f"No puedo esperar a ver tu próximo hechizo, {mago.title()} \n")
print("Gracias a todos los magos, fue un gran espectáculo")


"""

    Ejercicios.

    1. Piensa en al menos tres tipos de pizzas que te gusten mucho. 
    Guarda los nombres de estas pizzas en una lista y luego utiliza 
    un ciclo for para imprimir el nombre de cada pizza.

        a) Modifica el ciclo for para que imprima una oración completa, 
        en lugar de solo el nombre de la pizza. Por ejemplo, en lugar de 
        solo imprimir "pepperoni", el programa debe mostrar: 
        "Me gusta la pizza de pepperoni".

        b) Al final del programa, fuera del ciclo for, agrega una línea 
        que diga cuánto te gusta la pizza en general. Por ejemplo, después 
        de las oraciones de las pizzas específicas, podrías agregar algo 
        como: "¡Realmente me encanta la pizza!".
    
    2. Piensa en al menos 3 animales diferentes que tengan características
    similares. Almacenalos en una lista e imprime el nombres de cada animal
    utilizando un for. 
    
        a) Imprime un mismo mensaje para cada animal, por ejemplo: " un perro
        sería una gran mascota. "
        
        b) Agrega un elemento al final de tu programa e imprímelo, 
        por ejemplo: " Todos éstos animales serían una gran mascota" 

"""
print("\n--------------Ejercicio 1-------------")


pizzas = ["pepperonni", "hawaiiana", "pastor"]
print(pizzas)
for pizza in pizzas:
    print(pizza)
    print(f"Me gusta la pizza de " + pizza.title())

print("\nMe encanta la pizza")


print("\n--------------Ejercicio 2-------------")

animales = ["capybara", "tejuino", "cuy"]
for animal in animales:
    print(animal)
    print("Los " + animal + " están muy facheros")

print(f"Todos estos animales serian una mascota bellaka")






print("\t-----------------------")
#

print("\n------------------------------------------")

print("'range method'")
for value in range (0,8):
    print(value)


print("\n---------------------------------------")
#Lista de numeros por rango
numbers=list(range(0,6))
print(numbers)

#Invertir una lista
numbers.reverse()
print(numbers)
    
#Numeros pares    
numbers_ev=list(range(2, 11, 2))
print(numbers_ev)

#Invertir una lista
numbers = list(range(10, -3, -1))
print(numbers)






squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Imprimir valores en for, comentario del for anidado
cars = ['tensla', 'ladylala', 'go-kars']
ice_creams = ['napolitano', 'fresa', 'pistache']
print()
for value in range(0,3): 
    print(cars[value] + "\n" + ice_creams[value] + '\n')    

# Otros métoso built-in
numbers = list(range(0,11))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

"""List comprehensions

    una list comprehensions combina el for loop y
    la creacion de nuevos elementos en una sola
    linea y automaticamente agrega cada nuevo 
    elemento a la lista, es decir, no tengo que
    utilizar el append.
    



    """

squares_2=[value**2 for value in range(1, 11)]
print(squares_2)



print("actualizacion")
