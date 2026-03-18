# importa funciones del CRUD
from funciones import *

# importa funciones de matrices (estadísticas)
from matrices import *


def main():

    estudiantes = []  # lista de listas → [nombre, nota]
    opcion = ""

    # menú principal
    while opcion != "6":

        print("=== Sistema de Evaluación Académica ===")
        print("1 - Agregar estudiante")
        print("2 - Mostrar estudiantes")
        print("3 - Modificar estudiante")
        print("4 - Eliminar estudiante")
        print("5 - Ver estadísticas")
        print("6 - Salir")

        opcion = input("Seleccione una opción: ").strip()

        # CREATE
        if opcion == "1":
            agregar_estudiante(estudiantes)

        # READ
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)

        # UPDATE
        elif opcion == "3":
            modificar_estudiante(estudiantes)

        # DELETE
        elif opcion == "4":
            eliminar_estudiante(estudiantes)

        # ESTADÍSTICAS (uso de matrices)
        elif opcion == "5":

            if len(estudiantes) == 0:
                print("No hay datos\n")
            else:
                prom = calcular_promedio(estudiantes)
                mejor = mejor_estudiante(estudiantes)
                peor = peor_estudiante(estudiantes)

                print("Promedio:", prom)
                print("Mejor:", mejor[0], "-", mejor[1])
                print("Peor:", peor[0], "-", peor[1])
                print()

        elif opcion == "6":
            print("Programa finalizado")

        else:
            print("Opción inválida\n")


# ejecuta el programa
main()