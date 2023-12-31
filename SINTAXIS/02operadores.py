### OPERADORES ###

### Aritméticos ###
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(10 % 2) # el residu
print(10 // 3) # aproximar a un int
print(2 ** 3) # exponent

print("Hola" + "Phyton") # ajunta lletres
print("Hola " + str(5)) # no "hola" + 5
print("Hola " + "5")
print("Hola " * 5) #print Hola Hola Hola Hola Hola, nomes int

my_float = 2.5 * 2 
print("Hola " * int(my_float))


### Comparativos ###
print(3 > 4)
print(3 < 4)
print(3 >= 4) # mayor o igual
print(3 <= 4)
print(3 != 4) #no igual
print(3 == 4) # 2 iguals
print(3 > 4 == 2) #false, aunque podemos juntar operadores comparativos

print("Hola" > "Phyton")
print("Hola" < "Phyton")
print("Hola" >= "Phyton")
print("Hola" <= "Phyton")
print("Hola" != "Phyton")
print("Hola" == "Phyton") # Ordenación ALFABÉTICA:
print("aaa" >= "bbb")
print("aaa">="aba")
print(len("aaa")>= len("aba")) # Cuenta de caracteres con len


### Operadores lógicos ###

"""

LÓGICA BOOLEANA:
FALSE and FALSE --> FALSE
FALSE and TRUE --> FALSE
FALSE or FALSE --> FALSE

TRUE and TRUE --> TRUE
TRUE or FALSE --> TRUE

"""

print(3 > 4 and "Hola" > "Phyton") 
print(3 > 4 or "Hola" > "Phyton")
print(3 < 4 or "Hola" < "Phyton")
print(3 < 4 or "Hola" > "Phyton")
print(3 < 4 or ("Hola" < "Phyton" and 4 == 4))
print(not(3 > 4)) # not --> para negar el resultado, not true --> false. Y vice.

