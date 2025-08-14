### Lambdas ###

## En Python, una función lambda es una pequeña función anónima, definida sin nombre, utilizando la palabra clave lambda. Se utiliza principalmente para crear funciones de corta duración y de una sola expresión. Son ideales para casos donde se necesita una función rápida y sencilla, especialmente como argumentos en otras funciones de orden superior como map, filter, o sorted.

suma_dos_numeros = lambda num1, num2: num1 + num2
print(suma_dos_numeros(2,4))

multiplica_valores = lambda num1, num2: num1 * num2 - 3
print(multiplica_valores(2,4))

def suma_tres_numeros(valor):
    return lambda num1,num2: num1 + num2 + valor #Esto es una lambda dentro de una función.
print(suma_tres_numeros(5)(2,4))