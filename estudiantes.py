from funciones import limpiar_pantalla, validar_email, validar_no_vacio, validar_numero
from matrices import guardar_estudiantes

# Módulo CRUD de estudiantes: alta, baja, modificación, listados y reactivación.
# La lista "estudiantes" se pasa siempre por parámetro y se modifica in-place
# (append, asignación de claves), por eso no hace falta devolverla ni reasignarla.

SEP = "-" * 40


def _imprimir_estudiante(alumno):
    """Imprime los datos de un estudiante con labels alineadas."""
    print(f"  Legajo : {alumno['legajo']}")
    print(f"  Nombre : {alumno['nombre']}")
    print(f"  Mail   : {alumno['mail']}")
    print(f"  Activo : {'Si' if alumno['activo'] else 'No'}")
    print(SEP)


def listar_estudiantes(alumnos):
    """Muestra el listado completo de estudiantes (activos e inactivos) con todos sus datos."""
    if len(alumnos) == 0:
        input("[x] No hay estudiantes. Presione enter...")
        return

    limpiar_pantalla()
    print("=== LISTA DE ESTUDIANTES ===")
    print()
    for alumno in alumnos:
        _imprimir_estudiante(alumno)

    input("\nPresione enter para continuar...")


def agregar_estudiante(estudiantes):
    """Solicita datos por consola y agrega un nuevo estudiante a la lista."""
    limpiar_pantalla()
    print("=== ALTA DE ESTUDIANTE ===")
    print()

    nombre = input("Nombre del alumno : ")
    while not validar_no_vacio(nombre):
        print("[x] El nombre no puede estar vacío.")
        nombre = input("Nombre del alumno : ")

    mail = input("Mail              : ")
    while not validar_email(mail) or not validar_no_vacio(mail):
        print("[x] Email inválido.")
        mail = input("Mail              : ")

    # El legajo se autogenera: si no hay estudiantes empieza en 1,
    # sino es el legajo del último cargado + 1.
    nuevo_legajo = 1 if len(estudiantes) == 0 else estudiantes[-1]['legajo'] + 1

    nuevo_estudiante = {
        'legajo': nuevo_legajo,
        'nombre': nombre,
        'mail':   mail,
        'activo': True
    }

    estudiantes.append(nuevo_estudiante)

    try:
        guardar_estudiantes(estudiantes)
        input(f"\n[✓] Alumno cargado con legajo {nuevo_legajo}. Presione enter...")
    except OSError as e:
        estudiantes.pop()
        input(f"[x] Error al guardar: {e}")


def mostrar_estudiantes(estudiantes):
    """Muestra un listado resumido (legajo - nombre) de los estudiantes activos."""
    if len(estudiantes) == 0:
        print("[x] No hay estudiantes\n")
        return

    for alumno in estudiantes:
        if alumno['activo']:
            print(f"  {alumno['legajo']} - {alumno['nombre']}")

    print()


def buscar_por_estudiante(estudiantes, legajo_buscado):
    """Búsqueda iterativa por legajo. Devuelve el índice en la lista o -1 si no existe."""
    for index, alumno in enumerate(estudiantes):
        if alumno['legajo'] == legajo_buscado:
            return index
    return -1


def buscar_estudiante_recursivo(estudiantes, legajo_buscado, indice=0):
    """Búsqueda recursiva por legajo. Devuelve el índice en la lista o -1 si no existe.
    Caso base 1: se recorrió toda la lista → devuelve -1.
    Caso base 2: el legajo coincide → devuelve el índice actual.
    Caso recursivo: avanzar al siguiente elemento."""
    if indice >= len(estudiantes):
        return -1
    if estudiantes[indice]['legajo'] == legajo_buscado:
        return indice
    return buscar_estudiante_recursivo(estudiantes, legajo_buscado, indice + 1)


def prueba_modificar_estudiante(estudiantes):
    """Permite modificar el nombre y mail de un estudiante existente."""
    limpiar_pantalla()
    print("=== MODIFICACION DE ESTUDIANTE ===")
    print()
    mostrar_estudiantes(estudiantes)

    legajo_busqueda = validar_numero("Legajo a modificar : ")
    posicion = buscar_por_estudiante(estudiantes, legajo_busqueda)

    if posicion == -1:
        input("[x] No existe un alumno con ese legajo. Presione enter...")
        return

    nuevo_nombre = input("Nuevo nombre       : ")
    while not validar_no_vacio(nuevo_nombre):
        print("[x] El nombre no puede estar vacío.")
        nuevo_nombre = input("Nuevo nombre       : ")

    nuevo_mail = input("Nuevo mail         : ")
    while not validar_email(nuevo_mail) or not validar_no_vacio(nuevo_mail):
        print("[x] Email inválido.")
        nuevo_mail = input("Nuevo mail         : ")

    estudiantes[posicion]['nombre'] = nuevo_nombre
    estudiantes[posicion]['mail']   = nuevo_mail

    try:
        guardar_estudiantes(estudiantes)
        print(f"\n[✓] Alumno actualizado:")
        _imprimir_estudiante(estudiantes[posicion])
    except OSError as e:
        print(f"[x] Error al guardar: {e}")
    input("\nPresione enter para continuar...")


def eliminar_estudiante(estudiantes):
    """Realiza una baja lógica: marca al estudiante como inactivo sin borrarlo."""
    limpiar_pantalla()
    print("=== BAJA DE ESTUDIANTE ===")
    print()
    mostrar_estudiantes(estudiantes)

    legajo_buscar = validar_numero("Legajo a dar de baja : ")
    posicion = buscar_estudiante_recursivo(estudiantes, legajo_buscar)

    if posicion == -1:
        input(f"[x] No se encontró el legajo {legajo_buscar}. Presione enter...")
        return

    nombre = estudiantes[posicion]['nombre']
    estudiantes[posicion]['activo'] = False

    try:
        guardar_estudiantes(estudiantes)
        input(f"[✓] {nombre} (legajo {legajo_buscar}) dado de baja. Presione enter...")
    except OSError as e:
        estudiantes[posicion]['activo'] = True
        input(f"[x] Error al guardar: {e}")


def listar_estudiantes_inactivos(estudiantes):
    """Muestra la lista detallada de estudiantes con baja lógica (activo=False)."""
    inactivos = [alumno for alumno in estudiantes if not alumno['activo']]

    if len(inactivos) == 0:
        input("[x] No hay estudiantes inactivos. Presione enter...")
        return

    limpiar_pantalla()
    print("=== ESTUDIANTES INACTIVOS ===")
    print()
    for alumno in inactivos:
        print(f"  Legajo : {alumno['legajo']}")
        print(f"  Nombre : {alumno['nombre']}")
        print(f"  Mail   : {alumno['mail']}")
        print(SEP)

    input("\nPresione enter para continuar...")


def reactivar_estudiante(estudiantes):
    """Revierte una baja lógica: vuelve a poner activo=True al estudiante."""
    limpiar_pantalla()
    print("=== REACTIVAR ESTUDIANTE ===")
    print()
    listar_estudiantes_inactivos(estudiantes)

    inactivos = [alumno for alumno in estudiantes if not alumno['activo']]
    if len(inactivos) == 0:
        return

    legajo = validar_numero("Legajo a reactivar : ")
    posicion = buscar_estudiante_recursivo(estudiantes, legajo)

    if posicion == -1:
        input(f"[x] No se encontró el legajo {legajo}. Presione enter...")
        return

    if estudiantes[posicion]['activo']:
        input(f"[x] El legajo {legajo} ya está activo. Presione enter...")
        return

    nombre = estudiantes[posicion]['nombre']
    estudiantes[posicion]['activo'] = True

    try:
        guardar_estudiantes(estudiantes)
        input(f"[✓] {nombre} (legajo {legajo}) reactivado. Presione enter...")
    except OSError as e:
        estudiantes[posicion]['activo'] = False
        input(f"[x] Error al guardar: {e}")


def menu_estudiantes(estudiantes, rol):
    """Submenú de estudiantes. Admin tiene CRUD completo; viewer solo puede listar."""
    seleccion = ""

    while seleccion != '0':
        limpiar_pantalla()
        print("=== MENU ESTUDIANTES ===")
        print()

        if rol == 'admin':
            print("1 - Alta de estudiante")
            print("2 - Modificar estudiante")
            print("3 - Baja de estudiante")
            print("4 - Lista de estudiantes")
            print("5 - Reactivar estudiante")
        else:
            print("1 - Lista de estudiantes")

        print("0 - Volver")
        print()
        seleccion = input("Opcion: ")

        if seleccion == '1' and rol == 'admin':
            agregar_estudiante(estudiantes)
        elif seleccion == '1' and rol == 'viewer':
            listar_estudiantes(estudiantes)
        elif seleccion == '2' and rol == 'admin':
            prueba_modificar_estudiante(estudiantes)
        elif seleccion == '3' and rol == 'admin':
            eliminar_estudiante(estudiantes)
        elif seleccion == '4' and rol == 'admin':
            listar_estudiantes(estudiantes)
        elif seleccion == '5' and rol == 'admin':
            reactivar_estudiante(estudiantes)
        elif seleccion == '0':
            input("[✓] Volviendo... Presione enter...")
        else:
            input("[x] Opcion invalida. Presione enter...")
