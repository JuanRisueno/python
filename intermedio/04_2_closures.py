### Closures ###

##En Python, una clausura (closure) es una función anidada que recuerda y accede a las variables de su función contenedora, incluso después de que esta última haya terminado de ejecutarse. Esto significa que una función closure puede mantener su propio entorno y datos, lo que la convierte en una herramienta útil para la programación funcional y la creación de funciones con estado.

def suma_diez():
    def add(valor):
        return valor + 10
    return add

add_closure = suma_diez()
print(add_closure(5))

def suma_diez(valor_original): #Le podemos dar un parámetro a la función original y trabajar con él dentro de la función anidada
    def add(valor):
        return valor + 10 + valor_original
    return add

add_closure = suma_diez(1) #Para que esto funcione, le tenemos que dar un valor al parámetro de la función original
print(add_closure(5))

add_closure = suma_diez(1)(5) #Podemos darle los valores de los parámetros de las funciones anidadas en una sola línea
print(add_closure)

print(suma_diez(1)(5)) #También se puede hacer sin necesidad de igualar a una variable