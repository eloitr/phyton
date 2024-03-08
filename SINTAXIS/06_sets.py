### SETS ###

#Definición
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente dice que es un dict

my_other_set = {"Eloi", "Traver", 15}
print(type(my_other_set))#ahora set

print(len(my_other_set))
print(my_other_set)

my_other_set.add("Cols")
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add("Cols")
print(my_other_set) #un set no admite repetidos

print("Traver" in my_other_set)#true
print("Traber" in my_other_set)#false

my_other_set.remove("Traver")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))


del my_other_set
#print(my_other_set) --> marca error porque ya no existe la variable

my_set = {"Eloi", "Traver", 15}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Java", "Kotlin", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_other_set).union(my_set).union({"Swift", "HTML"})) #como son repetidos, no los muestra. LOS NUEVOS CREADOS SÍ (NO HACE FALTA CRAR NUEVA VARIABLE)

print(my_new_set.difference(my_set))#mustra la diferencia, los que quedan menos my_set. Los últimos .union no los pone pq era solo pare el print