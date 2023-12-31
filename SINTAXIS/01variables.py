### VARIABLES ###

my_string_variable = "My String variable" # sempre minúscula i _
    # o
my_string_variable_2 = 'My String variable 2' # comilla simple

print(my_string_variable)

my_int_variable = 5 # numeros enteros
print(my_int_variable)

my_int_to_str_variable = str (my_int_variable) # int a str, transfomando a una cadena de texto
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False # true/false
print(my_bool_variable)

# Concatenación de variables en un print:
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:",my_bool_variable)
#Probamos type del print
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))#no type

# len -->contar caracteres
print(len(my_string_variable))

# Variables en una sola línea, cuidado con abusar de esta sintaxis
name, surname, edad, resultado = "Eloi", "Traver", 15, False
print("Me llamo", name, surname, "y mi edad es de", edad, "años. Tu respuesta es de tipo", resultado, ".")

# input
name_player = input("Com et dius?")
age_player = input("Quina edat tens?")

print(name_player)
print(age_player)

# Cambiando tipos
name_player = 15
age_player = "Eloi"
print(name_player)
print(age_player)

# Forzando el tipo
adreça: str = "Mi dirección"
adreça = True
adreça = 3
adreça = 3.5
print(adreça)
print(type(adreça)) #se cambia