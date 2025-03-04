### Sets ###

my_set = set()
my_other_set = {}

print(type (my_set))
print(type (my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Juan", "Risu", 45}
print(type (my_other_set)) # Al rellenarlo se "transforma" en un set

print(my_other_set)
print(len (my_other_set))

my_other_set.add("Johny")
print(my_other_set) # Un set NO es una estructura ordenada

### En un set no podemos buscar elementos por su posicion al no saber 
### en que posición está, por no estar ordenada ###

my_other_set.add("Johny") # Un set NO admite repetidos
print(my_other_set)

print("Juan" in my_other_set) # Realizamos búsquedas y nos devuelve true o false
print("Jon" in my_other_set)

my_other_set.remove("Johny") # Eliminar datos del set
print(my_other_set)

my_other_set.clear() # Elimina todos los datos del set
print(my_other_set)
print(len (my_other_set))

del my_other_set # Borramos la variable
# print(my_other_set) Si la imprimimos, ya nos da error al no existir

my_set = {"Juan", 45, "Tina", 1.70}
my_list = list(my_set) # Transformar un set en una lista es una operación muy arriesgada y poco fiable
print(my_list)
print(my_list[0])

my_other_set = {"Jon", 1.65, "Noa", 1.50}

my_new_set = my_set.union(my_other_set) # Unimos dos sets
print(my_new_set)
print(my_new_set.union({'Bailen'})) # Añadimos valores a la variable directamente en el print. Solo para este print ya que no almacenamos los valores en la variable
print(my_new_set) # aquí ya no tiene Bailén añadido al set

print(my_new_set.difference(my_set)) # Quitamos los valores que están repetidos en los dos sets