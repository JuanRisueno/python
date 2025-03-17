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
