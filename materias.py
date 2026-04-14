from funciones import limpiar_pantalla


def agregar_materia(materias):
    materiaNueva = []

    id = materias[-1][0] + 1 if materias else 1
    nombre = input('Ingrese el nombre de la materia: \n')

    materiaNueva.append(id)
    materiaNueva.append(nombre)
    materiaNueva.append(True)

    input(f'Se agregó correctamente la materia: {materiaNueva} presione enter para continuar')
    return materiaNueva


def menu_materias(materias):
    seleccion = ""

    while seleccion != '0':
        limpiar_pantalla()

        print("1. Alta de materias")
        print("2. Modificacion de materias")
        print("3. Baja de materia")
        print("4. Lista de materias")
        print("0. Volver\n")

        seleccion = input('Opcion: ')

        if seleccion == '1':
            limpiar_pantalla()
            materias.append(agregar_materia(materias))

        elif seleccion == '2':
            input('Función de modificación aún no implementada. Presione enter para continuar.')

        elif seleccion == '3':
            input('Función de baja aún no implementada. Presione enter para continuar.')

        elif seleccion == '4':
            limpiar_pantalla()
            print('Lista de materias:')
            for materia in materias:
                print(materia)
            input()

        elif seleccion == '0':
            print('Volviendo al menú anterior...')
            input()

        else:
            input('Opcion invalida. Presione enter para continuar.')
