### LISTAS ###

my_list = list() 
my_other_list = []

print(len(my_list))

my_list = [15, 56, 34, 20, 20]
my_list = list([15, 56, 34, 20, 20])
print (my_list)
print (len(my_list)) #numero de datos de la lista

my_other_list = [15, 1.71, "Eloi", "Traver"] #no hace falta guardar en la lista el mismo tipo de dato
print(type(my_other_list))

print(my_other_list[0])#empezamos a contar desde 0
print(my_other_list[1])
print(my_other_list[-1])#se'n va a l'últim
print(my_other_list[-3])#igual que 1

print(my_other_list.count("Eloi"))
print(my_list.count(20))#ens diu quants hi ha iguals a la mateixa llista, quantes vegades es repeteix

age, height, name, surname = my_other_list #podem posar-li nom als elements de la llista
print (name)
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]#també es pot fer això
print(name)

print (my_list + my_other_list) #s'ajunten

my_other_list.append("Bon dia")
print(my_other_list)

my_other_list.insert(0, "blue")
print(my_other_list)
