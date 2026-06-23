from funciones import limpiar_pantalla, validar_email, validar_no_vacio, validar_numero
from matrices import guardar_estudiantes

# Módulo CRUD de estudiantes: alta, baja, modificación, listados y reactivación.
# La lista "estudiantes" se pasa siempre por parámetro y se modifica in-place
# (append, asignación de claves), por eso no hace falta devolverla ni reasignarla.


def listar_estudiantes(alumnos):
    # Listado completo (activos e inactivos) con todos los datos.
    if len(alumnos) == 0:
        input("No hay estudiantes")
        return

    limpiar_pantalla()
    print("=== LISTA DE ESTUDIANTES ===")
    print()
    for alumno in alumnos:
            print(f"Legajo: {alumno['legajo']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Mail: {alumno['mail']}")
            print(f"Activo: {'Sí' if alumno['activo'] else 'No'}")
            print("-" * 30)

    input()


def agregar_estudiante(estudiantes):
    limpiar_pantalla()
    print("=== ALTA DE ESTUDIANTE ===")
    print()

    nombre = input('Ingrese el nombre del alumno: ')
    while not validar_no_vacio(nombre):
        print("Nombre inválido (no puede estar vacío)")
        nombre = input('Ingrese el nombre del alumno: ')

    mail = input('Ingrese el mail: ')

    while not validar_email(mail) or not validar_no_vacio(mail):
        print("Email inválido")
        mail = input('Ingrese el mail: ')

    # El legajo se autogenera: si no hay estudiantes empieza en 1,
    # sino es el legajo del último cargado + 1.
    if len(estudiantes) == 0:
        nuevo_legajo = 1
    else:
        nuevo_legajo = estudiantes[-1]['legajo'] + 1

    nuevo_estudiante = {
        'legajo': nuevo_legajo,
        'nombre': nombre,
        'mail': mail,
        'activo': True
    }

    estudiantes.append(nuevo_estudiante)
    guardar_estudiantes(estudiantes)  # persiste el cambio en .txt y .json

    input('Alumno cargado exitosamente, presione enter para continuar...')


def mostrar_estudiantes(estudiantes):
    # Listado resumido (solo legajo y nombre), usado como ayuda visual antes
    # de pedir un legajo para modificar/eliminar/reactivar.
    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    for alumno in estudiantes:
        if alumno['activo']:
            print(f"{alumno['legajo']} - {alumno['nombre']}")

    print()


def buscar_por_estudiante(estudiantes, legajo_buscado):
    # Búsqueda lineal: recorre la lista y devuelve la posición (índice) del
    # estudiante con ese legajo, o -1 si no lo encuentra.
    for index, alumno in enumerate(estudiantes):
        if alumno['legajo'] == legajo_buscado:
            return index
    return -1


def prueba_modificar_estudiante(estudiantes):
    limpiar_pantalla()
    print("=== MODIFICACION DE ESTUDIANTE ===")
    print()
    mostrar_estudiantes(estudiantes)

    legajo_busqueda = validar_numero('Ingrese el legajo a modificar: ')
    posicion = buscar_por_estudiante(estudiantes, legajo_busqueda)

    if posicion != -1:
        nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ")
        while not validar_no_vacio(nuevo_nombre):
            print("Nombre inválido (no puede estar vacío)")
            nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ")

        nuevo_mail = input("Ingrese el nuevo mail: ")

        while not validar_email(nuevo_mail) or not validar_no_vacio(nuevo_mail):
            print("Email inválido")
            nuevo_mail = input("Ingrese el nuevo mail: ")

        # Se modifica el diccionario en la posición encontrada (in-place).
        estudiantes[posicion]['nombre'] = nuevo_nombre
        estudiantes[posicion]['mail'] = nuevo_mail
        guardar_estudiantes(estudiantes)

        print("Alumno modificado:", estudiantes[posicion])
        input()
    else:
        print("No existe un alumno con ese legajo.")
        input()


def eliminar_estudiante(estudiantes):
    # Baja lógica: no se borra de la lista, solo se marca activo=False.
    # Así se conserva el historial y las notas asociadas siguen siendo válidas.
    limpiar_pantalla()
    print("=== BAJA DE ESTUDIANTE ===")
    print()
    mostrar_estudiantes(estudiantes)

    legajo_buscar = validar_numero("Ingrese el legajo a eliminar: ")
    posicion = buscar_por_estudiante(estudiantes, legajo_buscar)

    if posicion != -1:
        estudiantes[posicion]['activo'] = False
        guardar_estudiantes(estudiantes)
        input(f'El estudiante {estudiantes[posicion]["legajo"]} {estudiantes[posicion]["nombre"]} fue eliminado correctamente.')
    else:
        input(f'No se encontro un estudiante con el legajo: {legajo_buscar}')


def listar_estudiantes_inactivos(estudiantes):
    """Muestra lista detallada de estudiantes inactivos"""
    # List comprehension: filtra solo los que tienen activo == False.
    inactivos = [alumno for alumno in estudiantes if not alumno['activo']]

    if len(inactivos) == 0:
        input("No hay estudiantes inactivos")
        return

    limpiar_pantalla()
    print("=== LISTA DE ESTUDIANTES INACTIVOS ===")
    print()
    for alumno in inactivos:
        print(f"Legajo: {alumno['legajo']}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Mail: {alumno['mail']}")
        print("-" * 30)

    input()


def reactivar_estudiante(estudiantes):
    # Reactiva una baja lógica: vuelve a poner activo=True.
    limpiar_pantalla()
    print("=== REACTIVAR ESTUDIANTE ===")
    print()
    listar_estudiantes_inactivos(estudiantes)

    inactivos = [alumno for alumno in estudiantes if not alumno['activo']]

    if len(inactivos) == 0:
        return

    legajo = validar_numero("Ingrese el legajo a reactivar: ")
    posicion = buscar_por_estudiante(estudiantes, legajo)

    if posicion != -1:
        if estudiantes[posicion]['activo']:
            input(f'El estudiante {estudiantes[posicion]["legajo"]} ya está activo.')
        else:
            estudiantes[posicion]['activo'] = True
            guardar_estudiantes(estudiantes)
            input(f'El estudiante {estudiantes[posicion]["legajo"]} {estudiantes[posicion]["nombre"]} fue reactivado correctamente.')
    else:
        input(f'No se encontro un estudiante con el legajo: {legajo}')


def menu_estudiantes(estudiantes, rol):
    # Submenú de estudiantes. El admin tiene CRUD completo;
    # el viewer solo puede consultar el listado (rol llega desde el login).
    seleccion = ""

    while seleccion != '0':
        limpiar_pantalla()
        print("=== MENU ESTUDIANTES ===")
        print()

        if rol == 'admin':
            print("1. Alta de estudiante")
            print("2. Modificacion de estudiante")
            print("3. Baja de estudiante")
            print("4. Lista de estudiantes")
            print("5. Reactivar estudiante")
        else:  # viewer
            print("1. Lista de estudiantes")

        print("0. Volver")

        seleccion = input('Opcion: ')

        # Cada opción chequea también el rol, porque el número "1" significa
        # cosas distintas según si es admin (alta) o viewer (listar).
        if seleccion == '1' and rol == 'admin':
            agregar_estudiante(estudiantes)

        elif seleccion == '1' and rol == 'viewer':
            limpiar_pantalla()
            listar_estudiantes(estudiantes)
            input()

        elif seleccion == '2' and rol == 'admin':
            limpiar_pantalla()
            prueba_modificar_estudiante(estudiantes)

        elif seleccion == '3' and rol == 'admin':
            eliminar_estudiante(estudiantes)

        elif seleccion == '4' and rol == 'admin':
            limpiar_pantalla()
            listar_estudiantes(estudiantes)
            input()

        elif seleccion == '5' and rol == 'admin':
            reactivar_estudiante(estudiantes)

        elif seleccion == '0':
            print('Volviendo al menu anterior...')
            input()

        else:
            limpiar_pantalla()
            print('Opcion invalida')
            input()
