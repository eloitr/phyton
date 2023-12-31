#hola mundo


print("holamundo")

'''
Hola em dic eloi
'''

my_string = "Esto es una cadena de texto"
my_string = "Cammbiando el valor de la cadena de texto "
print(type(my_string))
print(my_string)

my_string = 6
print(type(my_string))
print(my_string)



my_int = 7
my_int = my_int+4
print(my_int)
print(my_int-1)
print(my_int)
print(my_string+my_int)
mbla_bla = 6.5
print(type(mbla_bla))
print(mbla_bla)
print(mbla_bla + my_int)


verdad = True
print(type(verdad))
print(verdad)
my_string="hola munsi"
print(type(my_string))
print(my_string)
print(str (my_int))

nom="Eloi"
anys=15
print ("El meu nom és " + nom + " i tinc "+ str(anys) + " anys." )
print(f"El meu nom és {nom} i tinc {anys} anys.")

nombre="nuria"


print(f"La {nombre} es olt guapa")

my_list = [nombre, nom, anys]
print(type(my_list))
print(my_list)
print(my_list[0]) 
my_dict = {"string":nom,"int":nombre,"string":anys,"eloi": "Eloi traver", }
print(my_dict)
print(my_dict["eloi"])
my_tuple_or_set = {nombre, nom, anys, anys, anys}
print(my_tuple_or_set)
'''
Tuple es una forma de definir una estructura ordenada y que puede contener repetidos no podemos cambiar
dict/set/list sí que podemos cambiar
'''


#----------------------------------------------------------------------------------------------------------------------------
#if / elif / else
my2_int=3
my2_int=3+4
if my2_int ==3 and verdad == True:
    print("el valor es 3") #OJO! POSAR 2 =
elif my2_int == 7:
    print("el valor es 7")
else:
    print("el valor no es 3 ni 7")

if my2_int ==3 or verdad == True:
    print("el valor es 3") #OJO! POSAR 2 =
elif my2_int == 7:
    print("el valor es 7")
else:
    print("el valor no es 3 ni 7")

#for
for my_item in my_list:
    print(my_item)

for my_item in range(10):
    print(my_item)

def my_function ():
    print("Esto es una fuincion")

for my_item in range(10):
    my_function()


print(2+9)