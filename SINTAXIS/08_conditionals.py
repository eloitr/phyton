### CONDITIONALS ###


my_condition = True

if my_condition: #Es lo mismo que if my_condition == True:
    print ("Se ejecuta la condicion del if")


my_other_condition = 5 * 3

if my_other_condition == 10: 
    print ("Se ejecuta la condicion del segundo if")

if my_other_condition > 10 and my_other_condition < 20: 
    print ("Es mayor que 10 y menor que 20")
elif my_other_condition == 15: # --> no lo pone porqué salta cuando cumple una condición de todo el if entero
    print("Es igual a 15")
else:
    print("Es menor o igual que 10")


my_string = ""
if my_string: #es False 
    print("Mi cadena de texto no es vacía")

my_string = ""
if not my_string: #es False 
    print("Mi cadena de texto no es vacía")

my_bool = False  
if not my_bool: #--> comprueva si no falso es true o no. Es decir, no nada -->true
    print("Mi cadena de texto no es vacía")


