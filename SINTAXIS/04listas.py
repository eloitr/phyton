### LISTAS ###

my_list = list() 
my_other_list = []

print(len(my_list))

my_list = [15, 56, 33, 11, 22, 44, 55, 66, 34, 20, 20]
my_list = list([15, 56, 33, 11, 22, 44, 55, 66, 34, 20, 20])
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

#AÑADIR O CAMBIAR EN UNA LISTA
my_other_list.append("Bon dia")
print(my_other_list)

my_other_list.insert(0, "blue")
print(my_other_list)

my_other_list[0] = "Rojo" #Para cambiar alores
print(my_other_list)




#BORRADORES
my_other_list.remove("Rojo")
print(my_other_list)

my_list.remove(20)
print(my_list)#només treu un

my_list.pop()#elimina el ultio elemento (por defecto)
print(my_list)

print(my_list.pop()) # retorna el que ha eliminat
print(my_list)

my_list.pop(2)#elimina el segon(tercer realmet:0, 1, 2) element
print(my_list) 
#també ho pots guardar en una variable
my_pop_element = my_list.pop(2)

del my_list[2]
print(my_list)

my_new_list = my_list.copy() #para copiar

my_list.clear() #eliminar todos los elemetos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()#cambia el orden, da la vuelta
print(my_new_list.reverse())

my_new_list.sort()#orden alfabético, de numeros
print(my_new_list)


print(my_new_list[1:3])#posa 2 xifres, el 1 i el 2





