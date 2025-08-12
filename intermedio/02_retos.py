### Retos de Programación ###

"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for indice in range(1,101):
        if indice % 3 == 0 and indice % 5 == 0:
            print ("fizzbuzz")
        elif indice % 5 == 0:
            print ("buzz")
        elif indice % 3 == 0:
            print ("fizz")
        else:
            print (indice)

fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama (palabra_uno, palabra_dos):
    if palabra_uno.lower() == palabra_dos.lower():
        return False
    return sorted(palabra_uno.lower()) == sorted(palabra_dos.lower())

print(anagrama("amor","roma"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci ():
    num1 = 0
    num2 = 1
    for indice in range (0,50):
        print(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3

fibonacci()

"""
NUMEROS PRIMOS 1
Escribe un programa que se encargue de comprobar si un número es o no primo.


def numero_primo (num):
    if num < 2:
        return "El número no es primo"
    
    for indice in range (2,num):
        if num % indice == 0:
            return "El número no es primo"
        
    return "El número es primo"

num = input ("Elige un número: ")
num = int(num)
print(numero_primo(num))
"""

"""
NUMEROS PRIMOS 2
Imprime los números primos entre 1 y 100.
"""

def lista_primos():
    for num in range (1,101):
        if num >= 2:
            divisible = False
            
            for indice in range (2,num):
                if num % indice == 0:
                    divisible = True

            if not divisible:
                print(num)

lista_primos()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
## Forma 1
def invertir(texto):
    texto_len = len(texto)
    texto_invertido = ""
    for indice in range(0, texto_len):
        texto_invertido += texto[texto_len - indice - 1]

    return texto_invertido

print(invertir("Hola mundo"))

# Forma 2
def invertir(texto):
    texto_invetido = texto[::-1]
    return texto_invetido

print(invertir("Hola mundo"))