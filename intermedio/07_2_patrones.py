### Patrones de expresiones regulares ###
## https://regex101.com/

import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"

patron = r"[lL]ección" # r expresado de esta manera es un caracter reservado para crear expresiones regulares
encontrar = re.findall(patron,my_string,re.I)
print(encontrar)

patron = r"[lL]ección|Expresiones"
encontrar = re.findall(patron,my_string,re.I)
print(encontrar)

patron = r"[0-9]"
print(re.search(patron,my_string,re.I))
print(re.findall(patron,my_string,re.I))

patron = r"\d" # Los carácteres que no sean letras y crea una lista
print(re.findall(patron,my_string,re.I))

patron = r"\D" # Solo los carácteres que sean letras y crea una lista
print(re.findall(patron,my_string,re.I))
print(f"En my_string hay {len(re.findall(patron,my_string,re.I))} letras") #Contamos cuantas letras hay en una cadena de texto

patron = r"[l|L]." # Busca dentro de la cadena de texto donde se encuentren las letras l o L y el siguiente carácter
print(re.findall(patron,my_string))

#Validación de un email
email = "risu.profesional@gmail.com"
patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" #Este es el patrón estándar sobre el que se trabaja normalmente.
print(re.match(patron,email))
print(re.search(patron,email))
print(re.findall(patron,email))

email = "risu.profesional@gmail"
patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.findall(patron,email)) #Nos devuelve un elemento vacío ya que el patron no corresponde con la variable email

email = "risu.profesional@gmail.com.mx"
if re.match(patron,email):
    print("El email es válido")
else:
    print("El email no es válido")