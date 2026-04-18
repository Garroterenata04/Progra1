from funciones import limpiar_pantalla


def cargar_materias():
    return [
        {"id": 1, "nombre": "Matematicas", "estado": True},
        {"id": 2, "nombre": "Fisica", "estado": True},
        {"id": 3, "nombre": "Quimica", "estado": True},
        {"id": 4, "nombre": "Programacion", "estado": True},
        {"id": 5, "nombre": "Ingles", "estado": True}
    ]


def agregar_materia(materias):
    nueva_id = materias[-1]['id'] + 1 if materias else 1
    nombre = input('Ingrese el nombre de la materia: \n')

    materiaNueva = {
        'id': nueva_id,
        'nombre': nombre,
        'estado': True
    }

    input(f"Se agregó correctamente la materia: {materiaNueva} presione enter para continuar")
    return materiaNueva


def menu_materias(materias, rol):
    seleccion = ""

    while seleccion != '0':
        limpiar_pantalla()
        print("=== MENU MATERIAS ===")
        print()

        if rol == 'admin':
            print("1. Alta de materias")
            print("2. Modificacion de materias")
            print("3. Baja de materia")
            print("4. Lista de materias")
        else:  # viewer
            print("1. Lista de materias")
        
        print("0. Volver\n")

        seleccion = input('Opcion: ')

        if (seleccion == '1' and rol == 'admin') or (seleccion == '1' and rol == 'viewer'):
            limpiar_pantalla()
            print('Lista de materias:')
            for materia in materias:
                print(materia)
            input()

        elif seleccion == '2' and rol == 'admin':
            input('Función de modificación aún no implementada. Presione enter para continuar.')

        elif seleccion == '3' and rol == 'admin':
            input('Función de baja aún no implementada. Presione enter para continuar.')

        elif seleccion == '4' and rol == 'admin':
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
