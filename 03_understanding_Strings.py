"""
Strings

Un string es de mandera sencilla una serie de caracteres, en python todo lo que se encuentre dentro de comillas simples
'' o de dobles comillas "" es considerado un string.

Ejemplos:
"Esto es un string"
"Esto también es un string"
"Le dije a un amigo, python es mi lenguaje favorito"
"eL LENGUAJE 'Python' lleva el nombre por Monty Python y no

"""

name="proGRa"


print("..........")
print(name)
print("..........")
print(name.title())
print("..........")
print(name.upper())
print("..........")
print(name.lower())
print("..........")

"""

Title

Un metodo es una accion que python puede realizar en un fragmento de datos o
sobre una variable, el punto despues de la variable seguida del metodo title() dice que se tiene
que ejecutar el metodo title de la variable name.

Todos los metodos van seguidos de parentesis, porque en ocasiónes necesitan información adicional para funcionar,
lo cual iria dentro del parentesis. En esta ocasión el metodo .title() no requiere
información extra para ejecutarse.

"""
"""

CONCATENACIÓN DE STRINGS


"""

first_name="Oscar"
last_name="Ruiz"

full_name=first_name+" "+last_name

print("----------")
print(full_name)
print("----------")
print("Hola"+" "+full_name.title()+"!")

"""
Whitespaces

"""
print("\n ----Whitespaces----")
print("\thola")

print("\nLinea1\n\tLinea2\n\t\tLinea3")


"""
Eliminacion espacios en blanco

"""

programming_language=" Python "

print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())

print("\n--------------Ejercicio 1-------------")

"""
Ej 1
Guarda nombre de persona famosa en una variable e imprime un mensaje
 de bienvenida a esta persona, ejemplo de salida:
 "Hola charly, ¿Te gustaría aprender algo mas sobre python?"
"""
name_person=" Oscar"
message=" ¡Bienvenido! y felicidades por tu 100 en mate."
print("Hi,"+name_person+","+message)


print("\n--------------Ejercicio 2-------------")

""" 
    2. Guarda el nombre de una persona en una variable e imprime
    su nombre en minúsculas, mayúsculas y utilizando el método title.
""" 
persona = "Nathanael Rubén Cano Monge"

print("-Mayusculas-")
print(persona.upper())

print("-Minusculas-")
print(persona.lower())

print("-Title-")
print(persona.title())

""" 
    3. Encuentra una cita de alguna persona famosa. Imprime la cita
    y el nombre del autor. Por ejemplo:
    "Charly Mercury una vez dijo, 'Python is love'"
""" 
print("\n--------------Ejercicio 3-------------")

print ('Pelusa Caligari una vez dijo, "Al final, todo estará bien, y si no está bien, es que no hemos llegado al final"')

"""     
    4. Repite el ejercicio anterior, pero ahora almacena el nombre
    de la persona famosa en una variable famous_person. Ahora
    crea la variable para la cita e imprime el mensaje.
""" 

print("\n--------------Ejercicio 4-------------")

idolo = "pelusa caligari"
frase = '"Al final, todo estará bien, y si no está bien, es que no hemos llegado al final" ' 

print (idolo.title()+" una vez dijo: "+frase)

""" 
    5. Guarda el nombre de una persona en una variable,
    agrega espacios, 
    tabuladores, saltos de línea. Imprime el nombre, 
    después 
    el nombre varias veces utilizando los métodos 
    rstrip, lstrip, strip.
"""

nombre_string = "    Antonio Herrera Perez  "

print(nombre_string)
print(nombre_string.rstrip())
print(nombre_string.lstrip())
print(nombre_string.strip())

