magicians=["El pelusa","voldemort","harry el sucio potter","colorado"]
print(magicians)
for mago in magicians:
    print(mago)
    print(mago.upper()+" ese fue un gran hechizo.")
    print(f"No puedo esperar a ver tu próximo hechizo, {mago.title()} \n")
print("Gracias a todos los magos, fue un gran espectáculo")



print("\t-----------------------")

print("'for'para las variables list")

for nombres in names:
    print(nombres)
    print(nombres.upper()+"q rollo plebe")
    print(f"hoy vi a {nombres.title()} en la cafe \n")
print("ei")


print("\n------------------------------------------")

print("'range method'")
for value in range (0,7):
    print(value)


print("\n---------------------------------------")
numbers=list(range(0,6))
print(numbers)

numbers=list(range(0,-1,-1))
print(numbers)
    
numbers_even=list(range(2,11,2))
print(numbers_ev)


print (min(digits))
print (max (digits))

"""
List comprehensions

    una list comprehensions combina el for y
    la creacion de nuevos elementos en una sola
    linea y automaticamente agrega cada nuevo 
    elemento a la lista, es decir, no tengo que
    utilizar el append.
    



    """

squares_2=[value**2 for value in range(1, 11)]
print(squares_2)