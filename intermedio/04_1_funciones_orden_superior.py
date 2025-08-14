### Funciones de orden superior ###

## En Python, una función de orden superior es aquella que toma otra función como argumento o devuelve una función como resultado. Esto significa que estas funciones operan con funciones, ya sea recibiéndolas como entrada o produciéndolas como salida.

def suma_uno(valor):
    return valor + 1

def suma_dos_numeros_y_uno (num1, num2):
    return suma_uno(num1 + num2) #Este num1 + num2 lo toma como parámetro suma_uno. Para entenderlo valor = num1 + num2
print(suma_dos_numeros_y_uno(5,2))

def suma_dos_numeros_y_uno_y_funcion (num1, num2, f):
    return f(num1 + num2) 
print(suma_dos_numeros_y_uno_y_funcion(5,2,suma_uno)) #Aquí, f es el parámetro de suma_uno. Para entenderlo f = valor ... y f es (num1 + num2)

def suma_cinco(valor):
    return valor + 5

print(suma_dos_numeros_y_uno_y_funcion(5,2,suma_cinco)) #Con este print, reusamos la funcion suma_dos_numeros_y_uno_y_funcion para hacer otro cálculo

## Funciones de orden superior que ya existen en el propio lenguaje

numeros = [2,5,10,21,3,30]

# Map

def multi_por_dos(numero):
    return numero * 2

print(list(map(multi_por_dos,numeros))) #Una función map siempre va a necesitar una lista de valores para iterar en ella y genera una nueva lista.
print(list(map(lambda numero: numero * 2,numeros))) #En vez de pasar una función, se puede usar una lambda

# Filter

def filter_mayor_de_diez(numero):
    if numero > 10:
        return True
    return False

print(list(filter(filter_mayor_de_diez,numeros))) #filter genera una nueva lista ajustándose a la condición de la función
print(list(filter(lambda numero: numero > 10,numeros))) #Usando una lambda

# Reduce

# En Python, reduce() es una función que aplica acumulativamente una función a los elementos de un iterable para reducirlo a un único valor. 

from functools import reduce #Para poder usar reduce, hay que importarla

numeros = [2,5,10,21,3,30]

def suma_dos_valores(num1,num2):
    print(num1) 
    print(num2)
    #Vamos a imprimir los dos valores para ver como van fluctuando.
    return num1 + num2

print(reduce(suma_dos_valores,numeros)) #El retorno de reduce() es solo un valor, en este caso, 71. Si quieres coprobarlo, comenta los prints de la función