# importa todas las funciones del archivo funciones.py
from funciones import *
from matrices import *
from os import system

# función principal del programa
def main():

    estudiantes = [[1, 'Juan Netto', 'jnetto@uade.edu.ar'], [2, 'Fulano', 'fulano@uade.edu.ar']]
    # lista donde se guardan los estudiantes
    # cada elemento será: [legajo, nombre, email]

    estudiantenuevo = []
    #lista temporal para guardar alumno nuevo

    opcion = ""

    # menú que se repite hasta que el usuario elija salir
    while opcion != "0":

        '''print("Sistema de Evaluación Académica")
        print("1 - Agregar estudiante")
        print("2 - Mostrar estudiantes")
        print("3 - Modificar estudiante")
        print("4 - Eliminar estudiante") #baja logica true/false
        print("5 - Ver promedio")
        print("6 - Mejor estudiante")
        print("0 - Salir")

        # pedir opción al usuario
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante(estudiantes)

        elif opcion == "2":
            mostrar_estudiantes(estudiantes)

        elif opcion == "3":
            modificar_estudiante(estudiantes)

        elif opcion == "4":
            eliminar_estudiante(estudiantes)

        elif opcion == "5":
            print("Programa finalizado")
        #elif opcion == "6":
            #prom = calcular_promedio(estudiantes)
            #print("Promedio:", prom, "\n")

        #elif opcion == "7":
            #mejor = mejor_estudiante(estudiantes)
            #if mejor:
                #print("Mejor estudiante:", mejor[0], "-", mejor[1], "-", mejor[2], "\n")
        #else:
            #print("Opción inválida\n")'''
        

        system('clear')

        print("1 - Menu estudiantes")
        print("2 - Menu materias")
        print("3 - Menu notas")
        print("4 - Estadisticas")
        print("0 - Salir")

        opcion = input('Opcion: ')

        if opcion == '1':

            menu_estudiantes(estudiantes)


        elif opcion == '2':

            print('Opcion 2')
            input()
            #menu_materias()

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