## .json file

import json

file_json = open("intermedio\mi_fichero.json","w+") #Creamos y sobreescribimos el fichero json

test_json = {
    "name":"Juan",
    "surname":"Risueno",
    "age":35,
    "languages": ["Python","JS","Java"],
    "website":"https://moure.dev"}

json.dump(test_json,file_json,indent = 4)   #Con dump escribimos el fichero json. Hay que indicarle que va a escribir y donde lo va a escribir
                                            #Con el indent damos formato al fichero json. Cuanto más alto es número, más espacios dejará a la izquierda. 4 es una tabulación

file_json.close() 
with open("intermedio\mi_fichero.json") as mi_otro_json: #Abrimos el fichero y lo asignamos a una variable
    for line in mi_otro_json.readlines(): #Para poderlo imprimir por consola, el fichero debe ser cerrado y abierto de nuevo en modo lectura
        print(line)

diccionario_json = json.load(open("intermedio\mi_fichero.json")) #leemos el fichero json y asignamos a una variable
print(diccionario_json) #al imprimimos vemos que esta variable es un diccionario, hemos transformado el json en un diccionario
print(type(diccionario_json))
print(diccionario_json["name"])