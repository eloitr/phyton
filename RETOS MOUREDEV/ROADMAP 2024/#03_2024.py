"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
"""

### ESTRUCTURAS DE DATOS ###

#LISTAS:
#Inserción
my_list = list(["dias", "Buenos", "dias"])
print(my_list)
print(my_list[0])

my_second_list = ["Hello", "Python"]
print(my_second_list)

my_list.append(15)
print(my_list)

#Borrado
my_second_list.insert(0, "Hola")
print(my_second_list)

my_list.remove("dias")
print(my_list)
