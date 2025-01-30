# Variables

#Usar _ entre las palabras de la variable
my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str = str(my_int_variable) #con str ha cambiado el tipo de la variable a de int a str
print(my_int_to_str)
print(type(my_int_to_str))


my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un mismo print
print(my_bool_variable, my_int_variable, my_string_variable, my_int_to_str)
print("Este es el valor de mi variable bool:", my_bool_variable)

#Algunas funciones del sistema
print(len(my_string_variable)) #len cuenta los caracteres de la variable que se le indique

#Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
nombre, apellido, alias, edad = "Juan", "Risueño", "RisuTech", 44
print("Mi edad es:", edad, "y mi apellido es:",apellido, "mi nombre es:", nombre,"y mi alias es", alias)

#input --> pide un valor y lo almacena en una variable
#nombre = input ("¿Cual es tu nombre?")
#print("Mi nombre es ", nombre)

#Cambiamos el tipo de dato a la variable
nombre = 44
edad = "Juan"
print(nombre, edad)

#Como forzar el tipo a una variable
direccion: str = "Mi dirección" # <-- Así forzamos de que tipo es la variable
print(direccion)
print(type(direccion))
direccion = 32 # <-- pero se puede cambiar sin problema
print(direccion)
print(type(direccion))

#Como se ve el tipado en Python es débil.