### STRINGS ###
my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + my_other_string)
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulador inicial"
print(my_tab_string)

my_scape_string = "\\tEste es un String con tabulador inicial que ha escapado del tabulador inicial"
print(my_scape_string)

### FORMATEO ###
name, surname, edad = "Juan", "Risueño", 44
print("Mi nombre es {} {} y mi edad es {} años".format(name, surname, edad))
print("Mi nombre es %s %s y mi edad es %d años" %(name, surname, edad))

print(f"Mi nombre es {name} {surname} y mi edad es {edad} años") ### ESTA ES LA MEJOR MANERA DE DAR FORMATEO AL TEXTO

### DESEMPAQUETADO DE CARACTERES ###
lenguaje = "python"
a, b, c, d, e, f = lenguaje
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)

### DIVISION DE CARACTERES###
lenguaje_div = lenguaje[1:3]
print(lenguaje_div)

lenguaje_div = lenguaje[1:]
print(lenguaje_div)

lenguaje_div = lenguaje[0:6:2]
print(lenguaje_div)

lenguaje_div = lenguaje[-2]
print(lenguaje_div)

### REVERSE ###
lenguaje_rev = lenguaje[::-1]
print(lenguaje_rev)

### FUNCIONES ###
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.lower())
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print("1".isnumeric())
print(lenguaje.upper().isupper())
print(lenguaje.lower().isupper())
print(lenguaje.startswith("py"))