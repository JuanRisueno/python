### Type Hints ###
## https://fastapi.tiangolo.com/es/python-types/

my_string_variable = "My String Variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My typed String variable" #Para trabajar con FastAPI siempre vamos a indicar de que tipo es la variable
                                                    #FastAPI se ayuda de esta forma de definir las variables para tener una mejor comunicación con el servidor, agilizando el proceso.
                                                    #Si tu le indicas que una variable es str y le mandas un número entero, FastAPI te creará un error.
                                                    #En mi opinión, es una forma de darle tipado más fuerte al propio Python.
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))