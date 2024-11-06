"""
Problema 1 tipo entrevista

Descifra el mensaje oculto

se tiene la siguiente lista 
mensaje = ["u", "n", "e", "m", "i", " ", "t", "o", " ", "Q", "o", "a", "d", "A", "R"]


Crea un programa que reemplace:
 -La letra a/A por la e
 -La letra e/E por la i
 -LA letra i/I por la o
 -LA letra o/O por la u 
 -LA letra u/U por la a
 -LA letra q/Q por la p
 -LA letra r/R por la s
 
 MUestra al final el mensaje oculto en consola cn la funcion print.
 (imprime el mensaje con un ciclo for para la salida, utiliza el 
 argumento end="" para qu eno imprima un salto de linea en cada print
 Ejemplo:
    print(letter, end"")
    
    )
"""

mensaje = ["u", "n", "e", "m", "i", " ", "t", "o", " ", "Q", "o", "a", "d", "A", "R"]
print("\n----Mensaje sin ordenar----")
print(mensaje)

print("\n----Mensaje ordenado----")
#a

#i
mensaje.remove("u")
mensaje.remove("n")
mensaje.remove("e")
mensaje.remove("m")
mensaje.remove("i")
mensaje.remove("t")
mensaje.remove("o")
mensaje.remove("Q")
mensaje.remove("o")
mensaje.remove("a")
mensaje.remove("d")
mensaje.remove("A")
mensaje.remove("R")

mensaje.insert(0, "a")
mensaje.insert(1,"n")
mensaje.insert(2,"i")
mensaje.insert(3,"m")
mensaje.insert(4,"o")

mensaje.insert(6,"t")
mensaje.insert(7,"u")

mensaje.insert(9,"p")
mensaje.insert(10,"u")
mensaje.insert(11,"e")
mensaje.insert(12,"d")
mensaje.insert(13,"e")
mensaje.insert(14,"s")

print(mensaje)





