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

print("--------------Ejercicio 1-------------")

"""
Ej 1
Guarda nombre de persona famosa en una variable e imprime un mensaje
 de bienvenida a esta persona, ejemplo de salida:
 "Hola charly, ¿Te gustaría aprender algo mas sobre python?"
"""
name_person="Oscar"
message="¡Bienvenido! y felicidades por tu 100 en mate."
print("Hi,"+name_person+","+message)

print("--------------Ejercicio 2-------------")





















"""
famous_person="Oscar Ruiz"
quote="python is love"
print(famous_person+" una vez dijo, "+quote)
message_f_string=f"{famous_person} una vez dijo: {quote}"
print(message_f_string)
"""