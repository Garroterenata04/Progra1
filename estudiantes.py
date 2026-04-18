from funciones import limpiar_pantalla, validar_email


def cargar_estudiantes():
    return [
        {'legajo': 1, 'nombre': 'Juan Pérez', 'mail': 'juan@mail.com', 'estado': True},
        {'legajo': 2, 'nombre': 'María Gómez', 'mail': 'maria@mail.com', 'estado': True},
        {'legajo': 3, 'nombre': 'Lucía Fernández', 'mail': 'lucia@mail.com', 'estado': False},
    ]


def guardar_estudiantes(estudiantes):
    # Los datos se mantienen en memoria durante la ejecución del programa.
    pass


def listar_estudiantes_archivo(alumnos):
    print("\n===== LISTA DE ALUMNOS =====\n")

    for alumno in alumnos:
        print(f"Legajo : {alumno['legajo']}")
        print(f"Nombre : {alumno['nombre']}")
        print(f"Mail   : {alumno['mail']}")
        print(f"Estado : {'Activo' if alumno['estado'] else 'Inactivo'}")
        print("-" * 30)

    input()


def agregar_estudiante(estudiantes):
    nombre = input('Ingrese el nombre del alumno: ')
    mail = input('Ingrese el mail: ')
    
    while not validar_email(mail):
        print("Email inválido")
        mail = input('Ingrese el mail: ')

    if len(estudiantes) == 0:
        nuevo_legajo = 1
    else:
        nuevo_legajo = estudiantes[-1]['legajo'] + 1

    nuevo_estudiante = {
        'legajo': nuevo_legajo,
        'nombre': nombre,
        'mail': mail,
        'estado': True
    }

    estudiantes.append(nuevo_estudiante)
    guardar_estudiantes(estudiantes)

    input('Alumno cargado exitosamente, presione enter para continuar...')


def mostrar_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    for alumno in estudiantes:
        print(alumno['legajo'], alumno['nombre'])

    print()


def buscar_pos_estudiante(estudiantes, legajo_buscado):
    for index, alumno in enumerate(estudiantes):
        if alumno['legajo'] == legajo_buscado:
            return index
    return -1


def prueba_modificar_estudiante(estudiantes):
    mostrar_estudiantes(estudiantes)

    legajo_busqueda = int(input('Ingrese el legajo a modificar: '))
    posicion = buscar_pos_estudiante(estudiantes, legajo_busqueda)

    if posicion != -1:
        nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ")
        nuevo_mail = input("Ingrese el nuevo mail: ")
        
        while not validar_email(nuevo_mail):
            print("Email inválido")
            nuevo_mail = input("Ingrese el nuevo mail: ")

        estudiantes[posicion]['nombre'] = nuevo_nombre
        estudiantes[posicion]['mail'] = nuevo_mail
        guardar_estudiantes(estudiantes)

        print("Alumno modificado:", estudiantes[posicion])
        input()
    else:
        print("No existe un alumno con ese legajo.")
        input()


def eliminar_estudiante(estudiantes):
    mostrar_estudiantes(estudiantes)

    legajo_buscar = int(input("Ingrese el legajo a eliminar: "))
    posicion = buscar_pos_estudiante(estudiantes, legajo_buscar)

    if posicion != -1:
        estudiantes[posicion]['estado'] = False
        guardar_estudiantes(estudiantes)
        input(f'El estudiante {estudiantes[posicion]["legajo"]} {estudiantes[posicion]["nombre"]} fue eliminado correctamente.')
    else:
        input(f'No se encontro un estudiante con el legajo: {legajo_buscar}')


def menu_estudiantes(estudiantes, rol):
    seleccion = ""

    while seleccion != '0':
        limpiar_pantalla()

        if rol == 'admin':
            print("1. Alta de estudiante")
            print("2. Modificacion de estudiante")
            print("3. Baja de estudiante")
            print("4. Lista de estudiantes")
        else:  # viewer
            print("1. Lista de estudiantes")
        
        print("0. Volver")

        seleccion = input('Opcion: ')

        if (seleccion == '1' and rol == 'admin') or (seleccion == '1' and rol == 'viewer'):
            limpiar_pantalla()
            listar_estudiantes_archivo(estudiantes)
            input()

        elif seleccion == '2' and rol == 'admin':
            limpiar_pantalla()
            prueba_modificar_estudiante(estudiantes)

        elif seleccion == '3' and rol == 'admin':
            eliminar_estudiante(estudiantes)

        elif seleccion == '4' and rol == 'admin':
            limpiar_pantalla()
            listar_estudiantes_archivo(estudiantes)
            input()

        elif seleccion == '0':
            print('Volviendo al menu anterior...')
            input()

        else:
            limpiar_pantalla()
            print('Opcion invalida')
            input()
