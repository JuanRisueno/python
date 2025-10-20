'''
Desarrolla un programa que calcule el área de un rectángulo:
1. Pide al usuario la base (puede ser decimal)
2. Pide la altura (puede ser decimal)
3. Calcula el área (base × altura)
4. Muestra el resultado con 2 decimales
'''

base = float(input ("Dime la Base: "))
altura = float(input ("Dime la Altura: "))

cuadrado = base * altura
triangulo = cuadrado / 2

print(f"Me has dado como base {base} y como altura {altura}")
print(f"El área del cuadrado es {cuadrado: .2f}")
print(f"El área del triángulo es {triangulo: .2f}")