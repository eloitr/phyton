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