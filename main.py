# importa todas las funciones del archivo funciones.py
from funciones import *
from matrices import *

# función principal del programa
def main():

    estudiantes = [[1, 'juan Netto', 'jnetto@uade.edu.ar', True], [2, 'fulano', 'fulano@uade.edu.ar', True]]
    materias = [[1, 'matematicas', True]]
    # lista donde se guardan los estudiantes
    # cada elemento será: [legajo, nombre, email]


    opcion = ""

    # menú que se repite hasta que el usuario elija salir
    while opcion != "0":
        

        limpiar_pantalla()

        print("1 - Menu estudiantes")
        print("2 - Menu materias")
        print("3 - Menu notas")
        print("4 - Estadisticas")
        print("0 - Salir")

        opcion = input('Opcion: ')

        if opcion == '1':

            menu_estudiantes(estudiantes)


        elif opcion == '2':

            menu_materias(materias)

        elif opcion == '3':

            print('opcion 3')
            input()
            #menu_notas()

        elif opcion == '4':

            print('opcion 4')
            input()
            #menu_estadisticas()
        
        elif opcion == '0':

            print('Saliendo...')

        else:

            print('opcion invalida')
            input()
            #menu estadisticas()

        




# ejecuta el programa
main()