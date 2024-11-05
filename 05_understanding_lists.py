""""
Los corchetes hacen listas [] y se separan por comas



"""

Guitarras=["fender", "Takamine", "Purepecha", "Ibanez", "Yamaha","RMC", ]
print(Guitarras)
print(Guitarras[0].title())
print(Guitarras[1], Guitarras[2])
print(Guitarras[3])
print(Guitarras[-1])
print(Guitarras[-2])

message="Mi primer guitarra fue una "+Guitarras[3].title()
print(message)
message_f=f"Mi primer guitarra fue una {Guitarras[3].upper()}"
print(message_f)

print("\n-----------------------------------------")

"""
Almacena los nombres de algunos de tus amigos en una lista llamada names,
imprime los nombres de tus amigos 1 por 1 accediendo a los elementos de la lista.

Utilizando la lista anterior. Imprime el nombre de cada persona agregandole un mensaje, es decir el texto del mensaje debe ser el mismo 
pero cada mensaje debe estar personalizad con el nombre de la persona.

Crea una lista con tus metodos, de transporte o con los modos de transporte que conozcas, utiliza la lista para imprimir una serie de 
mensajes sobre cada elemento de la lista.
Por ejemplo, "Me gustaria tener un auto tesla".

"""
print("\n--------------Compas---------------------------")

Compas=["Pedro", "Pepe", "Carlos", "Miguel", "Lolo"]
print(Compas[0])
print(Compas[1])
print(Compas[2])
print(Compas[3])
print(Compas[4])

print("\n-----------------------------------------")

print("A " + Compas[0]+" Le gustan los camotes")
print(Compas[1]+" es bellako")
print(Compas[2]+"   sabe cantar chido")
print("A "+Compas[3]+" lo anexaron")
print("El " +Compas[4]+ " no trae ni un duro")

print("\n------------Carros-----------------------------")

Carros=["BMW", "Tsuru", "Mototaxi torito", "Chevy 4x4", "Versa"]
print(Carros[0]+" es caro")
print("Quiero un "+Carros[1]+" tuneado")
print("El"+ Carros[2]+" es mi lugar seguro")
print("Voy a hacer un " +Carros[3])
print("Mi mamá tiene un "+ Carros[4])

"""
Agregar elementos a una lista

"""

print("---------Guitarras-------------------")
print(Guitarras)
# Como agregariamos elementos a la lista?
Guitarras.append("Stratocaster")
print(Guitarras)
Guitarras.append("Segovia")
print(Guitarras)


print("-------Bajos-----------------")

Bajos=["Yamaha, Kingsman, Stratocastro"]

print(Bajos)

Bajos.append("Fender")
print(Bajos)
Bajos.append("Babilon")
print(Bajos)
Bajos.append("Ibanez")
print(Bajos)
Bajos.insert(0,"PARACHO")

"""
Metodo remove



"""
print(Bajos)
Bajos.remove("Babilon")
print(Bajos)
element_to_delete="Fender"
print(Bajos)

