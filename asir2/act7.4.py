'''
Escribe un programa que:
1. Pida dos números enteros al usuario
2. Muestre:
- La suma
- La resta
- La multiplicación
- La división (con decimales)
- La división entera
- El resto (módulo)
- El primer número elevado al segundo
'''

num1 = float(input("Dime el número 1: "))
num2 = float(input("Dime el número 2: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2
divie = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multi}")
print(f"División: {divi}")
print(f"Divisón Entera: {divie}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")


