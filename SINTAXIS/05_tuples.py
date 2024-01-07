### Tuples ###

#Definiciones:
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (15, 1.70, "Eloi", "Traver")
print(my_tuple)
print(type(my_tuple))
#Ej:
print(my_tuple[0])
print(my_tuple[-1])

#Operar con tuplas
#Contar cuantas veces aparece
print(my_tuple.count("Eloi"))
my_tuple = (15, 1.70, "Eloi", "Traver", "Eloi")
print(my_tuple.count("Eloi"))

#decir dónde esta en la tupla
print(my_tuple.index("Traver"))

#EN LAS TUPLAS NO SE PUEDEN CAMIAR LOS VALORES, CONSTANTE, IMMUTABLE POR DEFINICIÓN. TAMPOCO SE PUEDE AÑADIR COMO EN LAS LISTAS
    #my_tuple[1] = 1.50 --> TypeError: 'tuple' object does not support item assignment

#SUMAR TUPLAS
my_other_tuple = (10, 3.1, 200)
my_sum_tuple = my_other_tuple + my_tuple
print(my_sum_tuple)

#Sacar solo algunos valores
print(my_sum_tuple[3:6])#esto si como en las listas


#del my_tuple[2]
#print(my_tuple) --> TypeError: 'tuple' object doesn't support item deletion
del my_tuple
#print(my_tuple) --> NameError: name 'my_tuple' is not defined
