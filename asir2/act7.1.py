'''
Crea un programa que:
1. Solicite al usuario su nombre
2. Solicite su edad
3. Muestre un mensaje de bienvenida personalizado
'''
nombre = input ("Dime tu nombre: ")
edad = int(input ("Dime tu edad: "))

print("Hola {}. Gracias por decirme que tienes {} años".format(nombre.title(),edad))
print("Hola %s. Gracias por decirme que tienes %d años"%(nombre.title(),edad))
print(f"Hola,{nombre.title()}. Gracias por decirme que tienes {edad} años.")