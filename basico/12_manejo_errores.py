### Manejo de Errores ###

numUno, numDos = 5, 1 #Definir variables en una línea

## try except

try:
    print(numUno + numDos) #No se puede sumar int y str. Con lo que, esto da un error.
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

numDos = "1"

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

## try except else

numDos = "1"

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #Si hay un error, no se ejecuta el else
    print("La ejecución continúa")

numDos = 1

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # else se ejecuta si no se producen errores
    print("La ejecución continúa")

## try except else finally

numDos = "1"

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #Si hay un error, no se ejecuta el else
    print("La ejecución continúa")
finally: #Se ejecuta hayan o no errores
    print("Se ejecuta seguro")

numDos = 1

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # else se ejecuta si no se producen errores
    print("La ejecución continúa")
finally:
    print("Se ejecuta seguro")

### Los apartados else y finally son opcionales mientras que los apartados try y except son obligatorios

## Errores por tipo

numDos = "1"

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except TypeError: #el except se ejecutará SOLO si hay un error TypeError
    print("Se ha producido un error")

# try: 
#    print(numUno + numDos)
#    print("No se ha producido un error")
# except not TypeError: #el except se ejecutará SOLO si hay un error distinto a TypeError ... atento al not
#    print("Se ha producido un error")

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError: #Se puede usar varios except específicos
    print("Se ha producido un TypeError")

## Capturar el tipo de error

numDos = "1"

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except TypeError as typeError: #el error se guarda en la variable varError
    print("Se ha producido un TypeError")
    print(typeError) #al ejecutar nos va a dar la información ya que tiene capturado el error

print ("Fin del programa") #comprobamos que el programa continúa y se termina

try: 
    print(numUno + numDos)
    print("No se ha producido un error")
except ValueError as valueError: 
    print("Se ha producido un error ValueError")
    print(valueError)
except Exception as exceptionError: #Con Exception podemos continuar el programa con errores genéricos no controlados y guardarlo en una variable
    print("Error distinto")
    print(exceptionError)

print ("Fin del programa") #comprobamos que el programa continúa y se termina