### Bucles ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional el else ... es para ejecutar algo cuando se sale del bucle
    print("Mi condición es mayor o igual que 10")

print ("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es menor que 15 y se detiene la ejecución")
        break #Te saca del bucle (no del if solo, sino del bucle)
    print(my_condition)

print ("La ejecución continúa")

# For
## Un for itera sobre objetos iterables

my_list = [35,24,62,52,30,30,17]

for element in my_list: #Con el for se itera sobre la lista. La variable element va cogiendo el valor iterado.
    print(element)

my_tuple = (25, 1.70, "Juan", "Risueño", "Juan")

for element in my_tuple: #Con el for se itera sobre la tupla
    print(element)

my_set = {"Juan", "Risu", 45}

for element in my_set: #Con el for se itera sobre la set
    print(element)

my_dict = {"Nombre":"Juan", "Apellido":"Risueño", "Edad":35, 1:"Python"}

for element in my_dict: #Con el for se itera sobre la diccionario - Nos devuelve los campos del dicionario
    print(element)
    if element == "Edad":
        break 
else: #Si se activa un break, no se activa este else ya que el break te saca del for al completo (el else pertenece al else)
    print("El bucle for ha finalizado")

for element in my_dict.values(): #Con el for se itera sobre la diccionario - Nos devuelve los valores de los campos del dicionario
    print(element)
    if element == "Risueño":
        continue #El continue te saca del if (te puedes dar cuenta k no ejecuta el print siguiente cuando llega al valor Risueño). Desaconsejado usarlo.
    print("Se Ejecuta")
else:
    print("El bucle for ha finalizado")

