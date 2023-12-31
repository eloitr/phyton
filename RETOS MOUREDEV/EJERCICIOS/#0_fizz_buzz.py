print ("Reto #0")
numeros = 0
def subimos (): 
    global numeros 
    numeros += 1
    if numeros%5 ==0 and numeros%3 == 0:
        print("fizzbuzz \n")
    if numeros%3 == 0:
        print("fizz \n")
    if numeros%5 == 0:
        print("buzz \n")
    
    else:
        print (f"{numeros} \n")
while numeros <100:
    subimos()

#SOLUCIÓN:

def fizzbuzz():

    for number in range(1, 101):

        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


fizzbuzz()