### Gestor de Paquetes para Python ###

### pip https://pypi.org/ --> Viene preinstalado con Python. Es lo que se usa para instalar paquetes externos como numpy o pandas.

# pip install pip
# pip install --version

# numpy --> pip install numpy --> pip uninstall numpy para desinstalar
# pip show numpy
import numpy
print(numpy.version.version)

numpy_array = numpy.array([25, 62, 52, 30, 44, 30, 17])
print(numpy_array)
print(type(numpy_array))

print(numpy_array * 2)

# pandas --> pip install pandas --> pip uninstall pandas para desinstalar

import pandas

### pip list --> Al ejecutarlo por terminal, se ve un lista de las librerías que están instaladas

# requests --> pip install requests
# Esta liberaría sirve para hacer peticiones a Apis

import requests
respuesta = requests.get("https://pokeapi.co/api/vo/pokemon?limit=151")
print(respuesta)
print(respuesta.status_code)

# Paquete Arimético - Es importante que dentro de los paquetes haya un __init__.py porque es quien identifica al conjunto de módulos como un paquete

from mypackage import arithmetics

print(arithmetics.suma_dos_valores(1,4))