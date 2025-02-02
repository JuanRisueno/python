### LISTAS (Engloba a los arrays y a las listas en sí. En Python no existen los arrays como en otros lenguajes. Existen las listas.) ###

my_list = list () # Creando listas 
my_other_list = [] # Otra forma de crear listas. Es la forma más común para definir las listas

print (len(my_list))

my_list = [25, 62, 52, 30, 44, 30, 17] # Pueden haber datos repetidos

print (my_list)
print (len(my_list)) # Nos devuelve cuantos elementos hay en la lista

my_other_list = [35, 1.77, "Juan", "Risueño"]
print (type(my_other_list))

print (my_other_list[0])
print (my_other_list[1])
print (my_other_list[-1]) # Cuenta el primer elemento del final de la lista.
print (my_other_list[-3]) # Cuenta el 3º elemento contando desde el final de la lista hacia la izquierda

print (my_other_list.count("Juan"))
print (my_list.count(30)) # En la variable my_list hay 2 valores que valen 30 y es lo que nos devuelve el count
print (len(my_other_list))

edad, altura, nombre, apellido = my_other_list # Al desempaquetar la lista, tiene que haber tantas variables como elementos en la lista
#my_other_list = edad, altura, nombre, apellidos  <--- así no funciona
print(nombre)

print (my_list + my_other_list)

my_other_list.append("RisuTech") # Añadimos un nuevo elemento a la lista con append
print (my_other_list)

my_other_list.insert(1, "Rojo") # Eliminamos un elemento.
print (my_other_list)

my_other_list[1] = "Azul"
print (my_other_list)

my_other_list.remove("Azul") # Añadimos un elemento en la posición que le indiquemos.
print (my_other_list)

my_list.remove(30) # Elimina el primer elemento que encuentra de izq a derecha.
print (my_list)

print(my_list.pop(2)) # Le indicamos que elemento queremos eliminar. Recordamos que en las listas el primer elmento es el 0.
print(my_list) # Ahora vemos que en la lista ya no esta el elemento que hemos eliminado con el pop

my_pop_element = my_list.pop(1) # Guardamos el elemnento pop en una variable antes de eliminarlo de la lista
print(my_pop_element)
print(my_list)

del my_list[2] #Borramos del todo el elemento indicado. Elimina por índice. No podremos operar con él, como con pop
print(my_list)

my_new_list = my_list.copy() # Copia la lista a una nueva variable

my_list.clear() #Borramos la lista entera
print(my_list)
print(my_new_list)

my_new_list.reverse() # Le damos la vuelta a la lista
print(my_new_list)

my_new_list.sort() # Ordena la lista en orden ascendente por defecto.
print(my_new_list)

print(my_new_list[0:2]) # Devuelve el elemento indicado en el primer número hasta el elemento indicado en el segundo número. Este elemento indicado en el segundo número NO LO DEVUELVE.


my_list = "Hola Python" 
### Deja de ser una lista para convertirse en una str. Python tiene tipado dinámico o débilmente tipado. Hay que tener mucho cuidado con este tema. ###
### Si se quieren definir constante, las buenas prácticas dicen que las variables se definan en mayúscula. Ejemplo: MY_LIST ... Pero si nos damos cuenta, aún estando en mayúsculas podríamos cambiarle el tipado. ###
### Lo dicho, puede ser una fuente de errores el tipado dinámico y hay que tener mucho cuidado. ###
print(my_list)