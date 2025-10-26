'''
Desarrolla un programa que:
1. Solicite dos números al usuario
2. Indique si el primero es mayor, menor o igual al segundo
3. Muestre si ambos números son pares (usa el operador `%`)
'''

num1 = int(input("Dime el número 1: "))
num2 = int(input("Dime el número 2: "))

if num1 > num2:
    print (f"El número {num1} es mayor que el número {num2} ")
elif num2 > num1:
    print (f"El número {num2} es mayor que el número {num1}")
else:
    print ("Los dós números ons iguales")

mod1 = (num1 % 2 == 0)
mod2 = (num2 % 2 == 0)

ambos = (mod1 and mod2)

print(f"El número 1 es Par? {mod1}")
print(f"El número 2 es Par? {mod2}")
print(f"Ambos son pares? {ambos}")