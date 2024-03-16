### CLASES ###

#Los noimbres de lasd clases: la primera en mayuscula todo junto, sin _ ni espacios.
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name): #tenemos la capacidad de que Person reciba algun parámetro -->constructor de clase
        self.nameeeee = name
        self.surname = "Traver" #se puede definir aquí


my_person = Person("Eloi")
print(my_person.nameeeee)
print(f"{my_person.nameeeee} {my_person.surname}")




class Person2:
    def __init__(self, name, surname): 
        self.full_name = f"{name} {surname}"

    def walk (self):
        print(f"{self.full_name} está caminando")
        
my_person = Person2("Eloi", "Traver")
print(my_person.full_name)
Person2("Eloi", "Traver").walk()


#8:36:13