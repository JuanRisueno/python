### Tipos de Errores ###

##Para visualizar los errores, hay que descomentar las líneas donde se producen y los verás (los errores) por la consola.

# SyntaxError
#print "Hola" # Esto da un SyntaxError al ejecutar
print("Hola")

# NameError
#print(nombre) #Esto es un NameError ya que la variable nombre no está definida
nombre = "Juan"
print(nombre)

# IndexError
mi_lista = ["Python","Swift","Kotlin","Dart","JS"]
print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[-1])
print(mi_lista[-2])
#print(mi_lista[5]) # Este error se produce porque esta intentando mostrar un elemento que no existe en la lista

# ModuleNotFoundError
#import maths # El módulo no existe
import math

# AttributeError
#print(math.PI) # Se da cuando intentas acceder mal una propiedad de un objeto
print(math.pi)

# KeyError
my_dict = {"Nombre":"Juan", "Apellido":"Risueño", "Edad":35, 1:"Python"}
print(my_dict["Edad"])
print(my_dict[1])
#print(my_dict["Apelido"]) #Se produce cuando se accede erróneamente a una posición de una estructura
print(my_dict["Apellido"])

# TypeError
#print(mi_lista["0"]) #Se produce cuando se accede de forma errónea a una lista. A las listas se accede a traves de elementos enteros (integer)
print(mi_lista[0])

# ImportError
#from math import PI #Se da cuando intentas importar mal un elemento de un módulo
from math import pi
print(pi)

# ValueError
my_int = "10 años"
print(my_int)
print(type(my_int))
#my_int = int("10 años") #Da error al intentar transformar a una int una cadena de texto con letras o símbolos
my_int = int("10")
print(my_int + 10)

# ZeroDivisionError
# print(4/0) #No se puede dividir entre 0
print(4/2)