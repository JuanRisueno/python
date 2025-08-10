### Listas Comprimidas ###

my_original_list = [35, 24, 62, 52, 30, 30, 17]
my_list = [i for i in my_original_list]
print (my_list)

mi_rango = range(11) #Crear listas a partir de un rango
print(list(mi_rango))

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)
my_list = [i for i in range(8)] #para hacer un rango que acabe en 7, hay que poner 8 valores ya que las listas siempre empiezan por el 0
print (my_list)

my_list = [i for i in range(21)] #Imaginemos que queremos hacer una lista de 20 números. Solo sería así de sencillo
print (my_list)

##Operaciones con las listas

my_list = [i + 1 for i in range(8)] # así se hace para empezar la lista por el número 1
print (my_list)

my_list = [i * 2 for i in range(8)] # números pares
print (my_list)

my_list = [i * i for i in range(8)] # así se hace para empezar la lista por el número 1
print (my_list)

##Listas combinadas con funciones

def sum_cinco(num):
    return num + 5

my_list = [sum_cinco(i) for i in range(8)] 
print (my_list)