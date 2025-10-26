'''
Crea un programa que:
1. Pida al usuario que introduzca cualquier valor
2. Intente convertirlo a `int`, `float` y `bool`
3. Muestre el tipo de dato original y los resultados de las conversiones
4. Use la función `type()` para verificar los tipos
'''

#Vamos a hacer el ejercicio con varias variables.
'''valor = input("Introduce un valor: ")

print(f"Valor original: '{valor}'")
print(f"Tipo original: {type(valor)}")

valor_int = int(valor)
print(f"Resultado int: {valor_int}")
print(f"Tipo de int: {type(valor_int)}")

valor_float = float(valor)
print(f"Resultado float: {valor_float}")
print(f"Tipo de float: {type(valor_float)}")

valor_bool = bool(valor)
print(f"Resultado bool: {valor_bool}")
print(f"Tipo de bool: {type(valor_bool)}")'''

#Vamos a hacer el ejercicion con una sola variable
# 1. Pedimos el valor UNA SOLA VEZ
valor_original = input("Introduce un valor: ")

print(f"Valor original: '{valor_original}'")
print(f"Tipo original: {type(valor_original)}")

print(f"Resultado int: {int(valor_original)}")
print(f"Tipo de int: {type(int(valor_original))}")

print(f"Resultado float: {float(valor_original)}")
print(f"Tipo de float: {type(float(valor_original))}")

print(f"Resultado bool: {bool(valor_original)}")
print(f"Tipo de bool: {type(bool(valor_original))}")