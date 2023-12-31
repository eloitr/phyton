### STRINGS ###

my_string = "My Strings"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # salta de línea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # tabulación
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado" # combina
print(my_scape_string)
my_scape_string_2 = "\\tEste es un String \\n escapado" # si posem 2 barres ja no fa cas a tab i salto de línea
print(my_scape_string_2)

# Formateo 

#%s para poner la variable en la cadena de texto #per un int millor %d
name, surname, age = "Eloi", "Traver", 15
print("Em dic {} {} i tinc {} anys.".format(name, surname, age)) #en format {}
print("Em dic %s %s i tinc %s anys." %(name, surname, age)) # per % posar al final % i variables
#mejor que:
print("Em dic " + name + " " + surname + " i tinc " + str(age) + " anys." )