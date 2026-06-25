from funciones import limpiar_pantalla, validar_no_vacio, validar_numero
from matrices import guardar_materias

# Módulo CRUD de materias: alta, baja, modificación y listados.
# A diferencia de estudiantes.py, no tiene función de reactivar.

SEP = "-" * 40


def _imprimir_materia(materia):
    """Imprime los datos de una materia con labels alineadas."""
    print(f"  ID     : {materia['id']}")
    print(f"  Nombre : {materia['nombre']}")
    print(f"  Activo : {'Si' if materia['activo'] else 'No'}")
    print(SEP)


def agregar_materia(materias):
    """Solicita un nombre por consola y agrega una nueva materia a la lista."""
    limpiar_pantalla()
    print("=== ALTA DE MATERIA ===")
    print()

    # El id se autogenera: el siguiente después del último (o 1 si la lista está vacía).
    nueva_id = materias[-1]['id'] + 1 if materias else 1

    nombre = input("Nombre de la materia : ")
    while not validar_no_vacio(nombre):
        print("[x] El nombre no puede estar vacío.")
        nombre = input("Nombre de la materia : ")

    nueva_materia = {
        'id':     nueva_id,
        'nombre': nombre,
        'activo': True
    }

    materias.append(nueva_materia)

    try:
        guardar_materias(materias)
        input(f"\n[✓] Materia '{nombre}' agregada con ID {nueva_id}. Presione enter...")
    except OSError as e:
        materias.pop()
        input(f"[x] Error al guardar: {e}")


def mostrar_materias(materias):
    """Muestra un listado resumido (id - nombre) de las materias activas."""
    if len(materias) == 0:
        print("[x] No hay materias\n")
        return

    for materia in materias:
        if materia['activo']:
            print(f"  {materia['id']} - {materia['nombre']}")

    print()


def listar_materias(materias):
    """Muestra el listado completo de materias (activas e inactivas) con todos sus datos."""
    if len(materias) == 0:
        input("[x] No hay materias. Presione enter...")
        return

    limpiar_pantalla()
    print("=== LISTA DE MATERIAS ===")
    print()
    for materia in materias:
        _imprimir_materia(materia)

    input("\nPresione enter para continuar...")


def buscar_por_materia(materias, id_buscado):
    """Búsqueda iterativa por id. Devuelve el índice en la lista o -1 si no existe."""
    for index, materia in enumerate(materias):
        if materia['id'] == id_buscado:
            return index
    return -1


def modificar_materia(materias):
    """Permite cambiar el nombre de una materia existente."""
    limpiar_pantalla()
    print("=== MODIFICACION DE MATERIA ===")
    print()
    mostrar_materias(materias)

    id_busqueda = validar_numero("ID de la materia a modificar : ")
    posicion = buscar_por_materia(materias, id_busqueda)

    if posicion == -1:
        input("[x] No existe una materia con ese ID. Presione enter...")
        return

    nuevo_nombre = input("Nuevo nombre                 : ")
    while not validar_no_vacio(nuevo_nombre):
        print("[x] El nombre no puede estar vacío.")
        nuevo_nombre = input("Nuevo nombre                 : ")

    materias[posicion]['nombre'] = nuevo_nombre

    try:
        guardar_materias(materias)
        print(f"\n[✓] Materia actualizada:")
        _imprimir_materia(materias[posicion])
    except OSError as e:
        print(f"[x] Error al guardar: {e}")
    input("\nPresione enter para continuar...")


def eliminar_materia(materias):
    """Realiza una baja lógica: marca la materia como inactiva sin borrarla."""
    limpiar_pantalla()
    print("=== BAJA DE MATERIA ===")
    print()
    mostrar_materias(materias)

    id_buscar = validar_numero("ID de la materia a dar de baja : ")
    posicion = buscar_por_materia(materias, id_buscar)

    if posicion == -1:
        input(f"[x] No se encontró la materia con ID {id_buscar}. Presione enter...")
        return

    nombre = materias[posicion]['nombre']
    materias[posicion]['activo'] = False

    try:
        guardar_materias(materias)
        input(f"[✓] '{nombre}' (ID {id_buscar}) dada de baja. Presione enter...")
    except OSError as e:
        materias[posicion]['activo'] = True
        input(f"[x] Error al guardar: {e}")


def menu_materias(materias, rol):
    """Submenú de materias. Admin tiene CRUD completo; viewer solo puede listar."""
    seleccion = ""

    while seleccion != '0':
        limpiar_pantalla()
        print("=== MENU MATERIAS ===")
        print()

        if rol == 'admin':
            print("1 - Alta de materia")
            print("2 - Modificar materia")
            print("3 - Baja de materia")
            print("4 - Lista de materias")
        else:
            print("1 - Lista de materias")

        print("0 - Volver")
        print()
        seleccion = input("Opcion: ")

        if seleccion == '1' and rol == 'admin':
            agregar_materia(materias)
        elif seleccion == '1' and rol == 'viewer':
            listar_materias(materias)
        elif seleccion == '2' and rol == 'admin':
            modificar_materia(materias)
        elif seleccion == '3' and rol == 'admin':
            eliminar_materia(materias)
        elif seleccion == '4' and rol == 'admin':
            listar_materias(materias)
        elif seleccion == '0':
            input("[✓] Volviendo... Presione enter...")
        else:
            input("[x] Opcion invalida. Presione enter...")
