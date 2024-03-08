### DICCIONARIOS ###


my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))


my_other_dict = {"Nombre":"Eloi", "Apellido":"Traver", "Edad":15, 1:"Python"}
my_dict = {
    "Nombre":"Eloi", 
    "Apellido":"Traver", 
    "Edad":15, 
    "Lenguajes":{"Python", "Swift", "Java"},
    1:1j
    }
print(my_other_dict)
print(my_dict)
print(len(my_other_dict))
print(len(my_dict))


print(my_dict["Nombre"])#imprime valor

my_dict["Nombre"] = "Terròs"
print(my_dict["Nombre"])

print(my_dict[1])


my_dict["Carrer"] = "Can Rossell"
print(my_dict)


del my_dict["Carrer"]
print(my_dict)

print("Eloi" in my_dict) #busca en claves, no valor
print("Nombre" in my_dict) #ara sí


print(my_dict.items())#igual
print(my_dict.keys())#lista de la clave
print(my_dict.values())#lista de valor

my_new_dict = my_dict.fromkeys(("Nombre", 1, "Piso")) #se crea un diccionario nuevo sin valores en vase a las claves que le damos
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) #tambén sie puede hacer con dict, sin reutilizar un diccionario existente
print(my_new_dict)

my_list = ["Nombre", 1, "Piso"] 
my_new_dict = dict.fromkeys(my_list) #otra opción
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Eloi", "Traver")) #le metemos estos str a tooas las claves
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Eloi") #le metemos esta str a tooas las claves
print(my_new_dict)

print(list(my_new_dict))#clave
print(tuple(my_new_dict))#clave
print(set(my_new_dict))#clave