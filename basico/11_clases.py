### Clases ###

## En Python, una clase es un modelo o plantilla para crear objetos. Define un tipo de objeto, especificando sus atributos (datos) y métodos (funciones) que operan sobre esos datos. Básicamente, una clase es un plano para construir objetos con características y comportamientos similares

class MiPersonaVacia:
    pass #La palabra clave pass dentro de una clase actúa como un marcador de posición. No realiza ninguna acción, pero permite que la clase sea sintácticamente válida cuando no se necesita definir ningún método o atributo inmediatamente. Es útil cuando se está construyendo la estructura de la clase pero aún no se ha implementado su funcionalidad. Es el final de la clase o la función. Lo que pusieras detrás, esta fuera de la estructura.

print(MiPersonaVacia)
print(MiPersonaVacia())

#Definimos una clase con los valores dentro de la propia clase.
class MiPersona:
    def __init__(self): # init sirve para crar un constructor de clase
        self.nombre = "Juan"
        self.apellido = "Risueño"

mi_persona = MiPersona()
print (mi_persona.nombre)
print(f"{mi_persona.nombre} {mi_persona.apellido}")

#Definimos una clase donde los parámetros se los damos desde la variable
class MiPersona:
    def __init__(self, nombre, apellido): 
        self.nombre = nombre # self sirve para poder acceder a los atríbutos o métodos dentro de la instancia donde estemos trabajando
        self.apellido = apellido

mi_persona = MiPersona("Juan","Risueño")
print (mi_persona.nombre)
print(f"{mi_persona.nombre} {mi_persona.apellido}")

#Definimos una clase más compleja con operaciones dentro
class MiPersona:
    def __init__(self, nombre, apellido, alias = "Sin alias"): #También podemos asignar valores por defecto, como con las funciones
        self.nombre_completo = f"{nombre} {apellido} {alias}" #Le damos formato a la cadena de texto y lo guardamos en la variable nombre_completo

mi_persona = MiPersona("Juan","Risueño")
print(mi_persona.nombre_completo)

mi_persona = MiPersona("Juan","Risueño","RisuTech")
print(mi_persona.nombre_completo)

mi_otra_persona = MiPersona("Jon","Risueño","Junkan")
print(mi_otra_persona.nombre_completo)

class MiPersona:
    def __init__(self, nombre, apellido, alias = "Sin alias"): 
        self.nombre_completo = f"{nombre} {apellido} ({alias})" #Esta es una propiedad pública
        self.__nombre = nombre #Esta es una propiedad privada. Se puede acceder a ella, pero no modificarla

    def get_nombre (self):
        return self.__nombre
    
    def caminar (self): #esto es una función dentro de una clase
        print(f"{self.nombre_completo} está caminando")

mi_persona = MiPersona("Juan","Risueño")
print(mi_persona.nombre_completo)
print(mi_persona.get_nombre())
mi_persona.caminar() #llamamos a la funcion dentro de la clase. Se imprime porque DENTRO de la funcion dentro de la clase tiene un print
mi_otra_persona = MiPersona("Jon","Risueño","Junkan")
print(mi_otra_persona.nombre_completo)
mi_otra_persona.caminar()

mi_otra_persona.nombre_completo = "Tina Navarro (Anit)" #Podemos darle el valor a la variable nombre_completo directamente
print(mi_otra_persona.nombre_completo)

mi_otra_persona.nombre_completo = "RisuTech" #El nuevo valor que le damos a la variable no tiene porque mantener el formato que tiene en la clase
print(mi_otra_persona.nombre_completo)
print(type(mi_otra_persona.nombre_completo))

mi_otra_persona.nombre_completo = 10 #El nuevo valor que le damos a la variable no tiene porque mantener el tipado que tiene en la clase
print(mi_otra_persona.nombre_completo)
print(type(mi_otra_persona.nombre_completo))