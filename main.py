# importa todas las funciones del archivo funciones.py
from funciones import *
from matrices import *
# función principal del programa
def main():

    estudiantes = []
    # lista donde se guardan los estudiantes
    # cada elemento será: [nombre, nota]

    opcion = ""

    # menú que se repite hasta que el usuario elija salir
    while opcion != "5":

        print("Sistema de Evaluación Académica")
        print("1 - Agregar estudiante")
        print("2 - Mostrar estudiantes")
        print("3 - Modificar estudiante")
        print("4 - Eliminar estudiante") #baja logica true/false
        print("5 - Ver promedio")
        print("6 - Mejor estudiante")
        print("7 - Salir")

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
            #print("Opción inválida\n")


# ejecuta el programa
main()