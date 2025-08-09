### Módulos ###

## Un módulo (también llamado biblioteca o librería) es un conjunto de funciones, clases y métodos predefinidos que se pueden usar para realizar tareas específicas, evitando la necesidad de escribir código desde cero.

import modulo #Importamos modulo.py
# import 10_funciones.py <--- no funciona porque la nomenclatura del archivo que queremos acceder empieza por un número.
modulo.suma(5, 5, 5) #Usamos la función del módulo que está en modulo.py
modulo.imprime("Hola Python!")

from modulo import suma, imprime # Así importamos apartados específicos de los módulos y se puede usar sin necesidad de nombrar el módulo
suma(5, 5, 1)
imprime("Hola de nuevo")

## Hay módulos del sistema de Python

import math # math es un módulo que esta en el core de Python para poder trabajar con él
print(math.pi) #accedemos al valor de pi a través del módulo math
print(math.pow(2,8)) #con pow hacemos potencias. Esto sería 2 elevado a 8

from math import pi as valor_pi #le damos un alias a pi
print(valor_pi)