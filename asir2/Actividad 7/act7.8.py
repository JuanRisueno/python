'''
Desarrolla un programa que:
1. Pida la edad del usuario
2. Pregunte si tiene carnet de conducir (respuesta: si/no)
3. Determine y muestre:
 Si es mayor de edad (`edad >= 18`)
 Si puede conducir (mayor de edad AND tiene carnet)
 Si es adolescente (edad entre 13 y 17, ambos inclusive)
'''

'''
#Forma 1 de hacerlo
edad = int(input ("Dime tu edad: "))

if edad < 13:
    print ("Eres un@ niñ@")
elif edad < 18 and edad > 13:
    print ("Eres adolescente y no puedes conducir.")
else:
    carnet = input ("Tienes carnet de conducir? (si/no): ")
    if carnet == "si":
        print ("Al ser mayor de edad y tener carnet, puedes conducir")
    else:
        carnet = False
        print ("Eres mayor de edad pero no tienes carnet, NO puedes conducir")
'''

#Forma 2 de hacerlo
edad = int(input ("Dime tu edad: "))
carnet = input ("Tienes carnet de conducir? (si/no): ")

if carnet == "si" and edad > 18:
    print ("Eres mayor de edad y puedes conducir")
elif edad > 18:
    print ("Eres mayor de edad pero no tienes carnet. No puedes conducir")
elif edad >= 13:
    print ("Eres un adolescente y no puedes conducir")
else:
    print ("Eres un niño")

'''
Nota: A mi me gusta más la forma 1. Pero la forma 2 es más adecuada para el ejercicio
'''