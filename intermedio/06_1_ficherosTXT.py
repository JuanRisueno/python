### Manejo de Ficheros ###

import os

## .txt file

#open("mi_fichero.txt") #Da error FileNotfoundError, otro error del sistema
#txt_file = open("intermedio\mi_fichero.txt","w+") #Con el w+ podemos crear ficheros y lo sobreescrimos
txt_file = open("intermedio\mi_fichero.txt","r+") #Con el r+ del final quiere decir que el fichero está en modo leer(read) plus con lo que tambien se puede escribir, pero no sobreescribe el archivo. Para eso, sería w+. Buscar Python files modes en google
#print(txt_file.read())
#print(txt_file.read(10)) # Así solo leeremos los 10 carácteres siguientes a los ya leídos. Si no hemos leído nunca el fichero, estos serán los 10 primeros carácteres.

#print(txt_file.readline()) #Lectura de la primera línea
#print(txt_file.readline()) #Si encademanos readline vamos leyendo línea a línea
#print(txt_file.readlines()) #Convierte al fichero en una lista línea a línea

for line in txt_file.readlines(): #Así vamos a iterar línea a línea sobre el fichero
    print(line) #Imprimimos sobre cada línea iterada, con lo que imprimimos el fichero línea a línea

txt_file = open("intermedio\mi_fichero.txt","w+") #Con w+ sobreescribimos el fichero, con lo que se borra todo en un primer momento. También se puede leer al tener el +
txt_file.write("Mi nombre es Juan\nMi apellido es Risueño\n45 años\nY mi lenguaje preferido es Python") #Con write escribimos en el fichero. Con \n añadimos un salto de línea.

txt_file.write("\nAunque también me gusta JS")

txt_file.close()

#os.remove("intermedio\mi_fichero.txt") #Así borraríamos el fichero
