'''
Crea un programa que convierta grados Celsius a Fahrenheit:
1. Solicita la temperatura en Celsius
2. Aplica la fórmula: F = C × 9/5 + 32
3. Muestra el resultado
'''

grados = float(input ("Dime los grados celsius: "))

formula = grados * 9/5 + 32

print(f"Son {formula: .2f}F")