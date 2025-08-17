### Expresiones Regulares ###

## Las expresiones regulares, a menudo abreviadas como regex, son una secuencia de caracteres utilizada para comprobar si un patrón existe o no en un texto (cadena) dado.

import re #Importamos re, que es el módulo que tiene las funcionalidades relacionadas con las expresiones regulares

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de Ficheros"

# match

print(re.match("Esta es la lección",my_string)) #match busca en la cadena de texto desde el principio de la cadena y tiene que estar bien lo que buscamos
print(re.match("Esta es la lección",my_other_string))
print(re.match("Expresiones",my_string)) #no lo encuentra porque no está bien escrito desde EL PRINCIPIO de la cadena.
print(re.match("Esta es la lección número 7: Expresiones",my_string)) #Así está bien buscado
print(re.match("Esta es la lección",my_string, re.I)) #La tercera parte de la expresión match son los flags

emparejar = re.match("Esta es la lección",my_string, re.I)
print(emparejar)
print(emparejar.span())
empezar,acabar = emparejar.span() #En las tuplas, al definir dos variables, la primera variable se refiere al primer elemento de la tupla y la segunda variable, al último.
print(type(emparejar.span())) #Nos podemos dar cuenta de que emparejar.span() es una tupla.
print(empezar) 
print(type(empezar))
print(acabar)
print(type(acabar))
print(my_string[empezar:acabar]) #Así conseguimos ver el valor de my_string restringido por el match

emparejar = re.match("Esta no es la lección",my_other_string, re.I)
if emparejar != None: #Otra forma de comprobar el None --> not(emparejar == None) ... otra: emparejar is not None
    print(emparejar)
    empezar,acabar = emparejar.span()
    print(my_other_string[empezar:acabar])

# search

buscar = re.search("lección",my_string, re.I) #Con search no hace buscar desde el principio de la cadena de texto (hasta la primera vez que lo encuentra)
print(buscar)
empezar,acabar = buscar.span()
print(my_string[empezar:acabar])

# findall

encontrar = re.findall("lección",my_string,re.I) #Busca todas las veces que se repite la string y crea una lista con ellas. Vemos que el re.I nos coge mayúsculas y minúsculas. Prueba a quitarlo.
print(encontrar)
print(type(encontrar))
print(f"La palabra 'lección' se repite {len(encontrar)} veces en my_string")

# split

dividir = re.split(":",my_string,re.I) #Crea una lista a traves de lo que nosotros queramos, en este caso los :
print(dividir)
print(type(dividir))

# sub

sustituir = re.sub("Lección", "LECCIÓN", my_string) #Con sub sustituimos una palabra con otra ... pero NO de forma definitiva. Tener cuidado con mayúsculas y minúsculas
print(sustituir)
print(type(sustituir))
sustituir = re.sub("Lección|lección", "LECCIÓN", my_string) #Con | indicamos varias expresiones a sustituir
print(sustituir)
sustituir = re.sub("[l|L]ección", "LECCIÓN", my_string) #Otra manera de hacerlo es meter las letras entre [] divididas por | Esto es un patrón de las expresiones regulares.
print(sustituir)
sustituir = re.sub("Expresiones Regulares", "RegEx", my_string)
print(sustituir)
print(my_string) #Comprobamos que my_string no ha sido modificada de forma definitiva