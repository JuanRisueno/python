### Tuplas ###

## En Python, una tupla es una colección ordenada e inmutable de elementos. Esto significa que una vez creada, no se puede modificar su contenido. 

my_tuple= tuple ()
my_other_tuple = ()

my_tuple = (25, 1.70, "Juan", "Risueño", "Juan")
my_other_tuple = (35, 60, 30)

print (my_tuple)
print (type (my_tuple))

print (my_tuple[0])
print (my_tuple[-1])
#print (my_tuple[4]) Error

print(my_tuple.count("Juan")) #Diferencia entre mayúsculas y minúsculas. Cuenta cuantos valores hay en la tupla
print(my_tuple.index("Risueño")) #Posición en la tupla
print(my_tuple.index("Juan")) #Posición en la tupla. Te devuelve la posición del primer valor que se encuentra.

#my_tuple[0] = 35 #Los valores de las tuplas no se pueden modificar
#Una tupla es inmutable. No se puede modificar ni tampoco añadir ni borrar valores.
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple #Se puede operar entre tuplas para añadir valores

print(my_sum_tuple)
print(type(my_sum_tuple)) #El resultado de operar entre tuplas es una nueva tupla

print(my_sum_tuple[3:6]) #Imprime desde el 3 (inclusive) al 6(no inclusive). O sea, imprime 3, 4 y 5

my_tuple = list(my_tuple) #Cambiamos el tipado de la tupla a una lista

print(type(my_tuple)) 

#Operamos con ella como una lista normal
my_tuple[4] = "Juanito"
my_tuple.insert(1, "Rojo")
print(my_tuple)

my_tuple = tuple(my_tuple) #Cambiamos el tipado de la lista a una tupla
print(type(my_tuple))
print(my_tuple)

#del my_tuple(2) No se pueden borrar valores de una tupla
#del (my_tuple) Las tuplas se pueden borrar.
#print(my_tuple) Si imprimes una tupla borrada, da error al no estar definida la variable