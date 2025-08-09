### Funciones ###

## Las funciones son códigos creados que pueden ser llamados todas las veces que queramos en nuestro programa.
## Con esto nos ahorraremos duplicar código.

def my_function (): # def es la palabra reservada para crear funciones
    print("Esto es una función")

my_function() # Para ejecutar la función, no hay palabra reservada ni nada por el estilo. Solo hay que llamar a la variable.

def suma_dos_valores (num_uno, num_dos): #Lo que está dentro de los corchetes son parámetros. Estos te los pedirá el programa cuando llames a la función.
    print(num_uno + num_dos)
    print(type(num_uno))

suma_dos_valores(4,5) #Al llamar a la función, dentro de los () pones los valores que la función necesita como parámetros.
suma_dos_valores("5","7") #Se puede concatenar cadenas de texto.
suma_dos_valores(4.5,5.4)

#### Recordar que el tipado de Python es un tipado débil y dinámico. Hay que tener cuidado con esto ####

def suma_dos_return (valor_uno, valor_dos):
    my_sum = valor_uno + valor_dos
    return my_sum #Con return la función nos deuvle un valor

my_result = suma_dos_return(5,5) #Guardamos el resultado devuelto por la función en una variable
print (my_result)

def imprime_nombre (nombre,apellido):
    print(f"{nombre} {apellido}")

imprime_nombre(apellido = "Risueño",nombre = "Juan")

def imprime_nombre_por_defecto (nombre,apellido, alias = "Sin Alias"): #Podemos indicar un valor por defecto en los parámetros
    print(f"{nombre} {apellido} {alias}")

imprime_nombre_por_defecto("Juan","Risueño","JohnyRisu") # alias coge el valor del tercer parámetro que le pasamos
imprime_nombre_por_defecto("Jon","Risueño") # alias ahora vale su valor por defecto

def imprime_textos (*textos): #con el * creamos un número de parámetros dinámico
    print(textos)

imprime_textos("Hola","Python","JohnyRisu")
imprime_textos("Hola")

def imprime_mayus (*textos):
    print(type(textos)) # Se ve que el tipado de textos es una tupla
    for texto in textos:
        print(texto.upper())

imprime_mayus("Hola","Python","JohnyRisu")
imprime_mayus("Hola")