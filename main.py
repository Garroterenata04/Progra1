# importa todas las funciones del archivo funciones.py
from funciones import *

# función principal del programa
def main():

    estudiantes = []  
    # matriz vacía donde se guardarán los estudiantes
    # cada fila será: [nombre, nota]

    opcion = ""

    # bucle del menú, se repite hasta que el usuario elija salir
    while opcion != "5":

        print("Sistema de Evaluación Académica")
        print("1 - Agregar estudiante")
        print("2 - Mostrar estudiantes")
        print("3 - Modificar estudiante")
        print("4 - Eliminar estudiante")
        print("5 - Salir")

        # el usuario elige una opción
        opcion = input("Seleccione una opción: ")

        # según la opción se llama a una función distinta
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

        else:
            print("Opción inválida")

# ejecuta la función principal
main()