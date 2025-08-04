### DICCIONARIOS ###

my_dict = dict()
my_other_dict = {}

print (type(my_dict))
print (type(my_other_dict))

my_other_dict = {"Nombre":"Juan", "Apellido":"Risueño", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Juan",
    "Apellido":"Risueño",
    "Edad":35,
    "Lenguajes": {"Python","Java","JS"},
    1:1.70
    }

print (my_dict)
print (my_other_dict)

print (len(my_other_dict))
print (len(my_dict))

print (my_dict["Nombre"])

my_dict["Nombre"] = "Pedro" #Cambia el valor de un campo
print (my_dict["Nombre"])

print (my_dict[1])

my_dict["Calle"] = "Calle Jaen" #Añade el campo calle al diccionario my_dict
print (my_dict)

del my_dict["Calle"] #Así borramos un elemento de un diccionario 
print (my_dict)

print("Pedro" in my_dict) #Realizamos búsquedas y nos devuelve true o false
print("Apellido" in my_dict)

print(my_dict.items()) #forma de listar los items, keys o valores del diccionario
print(my_dict.keys())
print(my_dict.values())

my_list = ["nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) #Con fromkeys crea un diccionario sin valores. Aqui a través de una lista.
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) #Con fromkeys crea un diccionario sin valores
print((my_new_dict))
my_new_dict = dict.fromkeys((my_dict)) #Aqui, con fromkeys, hacemos una copia de las keys de otro diccionario dejando los valores vacíos
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "JohnyRisu") #Damos valor Johnyrisu a cada una de las keys del diccionario
print((my_new_dict))

my_values = my_new_dict.values() #Es una nueva estructura, dict_values
print(type(my_values))

print(list(my_new_dict)) #Transformarmos el diccionario en otras estructuras
print(list(my_new_dict.values())) #Transforma en una lista los valores del diccionario
print(tuple(my_new_dict))
print(set(my_new_dict))

