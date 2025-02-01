### OPERADORES ARITMÉTICOS ###

print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print (10 % 2) # Módulo. Nos da como resultado el resto de la división
print (10 % 3) # Módulo. Nos da como resultado el resto de la división
print (10 // 3) # Floor division. La división nos devuelve el número entero aproximado
print (2 ** 3) # Exponente
print (2 ** 3 + 3 - 7 / 1 // 4)

print ("Hola " + "Python, " + "¿Qué tal?")
print ("Hola " + str(5))
print ("Hola " * 5) # Puedes multiplicar cadenas de strings (Sólo multiplica números enteros)
print ("Hola " * (2 ** 3)) # Puedes multiplicar cadenas de strings (Sólo multiplica números enteros)

my_int = 2 * 5
print ("Hola " * my_int)

my_float = 2.5 * 2
print ("Hola " * int(my_float))

### OPERADORES COMPARATIVOS ###

print (3 > 4)
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4)

print ("Hola" > "Python") # Compara la ordenación alfabética. No distingue entre mayúsculas y minúsculas
print ("Hola" < "Python")
print ("Hola" >= "Zola")
print ("Hola" <= "hola")
print ("Hola" == "Hola")
print ("Hola" != "Python")

print (len("Hola") > len("Python")) # Compara la longitud de la cadena de texto
print (len("Hola") < len("Python")) # Compara la longitud de la cadena de texto

#### OPERADORES LÓGICOS ####

print (3 > 4 and "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (3 < 4 and "Hola" < "Python")
print (3 < 4 or "Hola" < "Python")
print (3 < 4 or ("Hola" > "Python" and 4 == 4))

print (3 < 4)
print (not(3 < 4))
