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
print(f"Mi nombre es {name} {surname} i tinc {age} anys.")

#DESEMPAQUETADO DE CARACTERES
language = "python"
a, b, c, d, e, f = language #cada letra
print(a)
print(c)

#DIVISION
language_slice = language[1:3]#de la 1 a la 3 sin contar la 3
print(language_slice)

language_slice = language[1:]#todo menos la primera letra
print(language_slice)

language_slice = language[-2]#la segunda empezando por el final
print(language_slice)

language_slice = language[0:6:2]#rimero pilla un rango y despues dice otro rango8ver ejemplo
print(language_slice)

#REVERSE
reversed_language = language[::-1]#dar la vuelta al str
print(reversed_language)


#MÉTODOS/FUNCIONES
print(language.capitalize())#posa la primera en majuscula
print(language.upper())#todo mayus
print(language.count("t"))#cuenta cuántas "t" tiene
print(language.isnumeric())#nos dice si es un número(bool)
print(language.lower())#todas minúsculas
print(language.upper().isupper())#nos dice si es upper o no
print(language.lower().isupper())
print(language.startswith("py"))#nos dice si empieza por...
