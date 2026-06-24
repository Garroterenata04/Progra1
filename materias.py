from funciones import limpiar_pantalla, validar_no_vacio, validar_numero
from matrices import guardar_materias

# Módulo CRUD de materias: alta, baja, modificación y listados.
# A diferencia de estudiantes.py, no tiene función de reactivar.


def agregar_materia(materias):
    limpiar_pantalla()
    print("=== ALTA DE MATERIA ===")
    print()
    # El id se autogenera igual que el legajo de estudiantes: el siguiente
    # número después del último id cargado (o 1 si la lista está vacía).
    nueva_id = materias[-1]['id'] + 1 if materias else 1
    nombre = input('Ingrese el nombre de la materia: \n')

    while not validar_no_vacio(nombre):
        print(" [x] Nombre inválido (no puede estar vacío)")
        nombre = input('Ingrese el nombre de la materia: \n')

    materiaNueva = {
        'id': nueva_id,
        'nombre': nombre,
        'activo': True
    }

    materias.append(materiaNueva)
    guardar_materias(materias)  # persiste el cambio en .txt y .json
    input(f"[✓] Se agregó correctamente la materia: {materiaNueva['nombre']} presione enter para continuar")


def mostrar_materias(materias):
    """Muestra lista simple para selección"""
    # Listado resumido (id y nombre), usado como ayuda visual antes de pedir
    # un id para modificar/eliminar.
    if len(materias) == 0:
        print("[x] No hay materias\n")
        return

    for materia in materias:
        if materia['activo']:
            print(f"{materia['id']} - {materia['nombre']}")

    print()


def listar_materias(materias):
    """Muestra lista detallada de materias con header"""
    if len(materias) == 0:
        input("[x] No hay materias")
        return

    limpiar_pantalla()
    print("=== LISTA DE MATERIAS ===")
    print()

    print(f"{'ID':<5}{'NOMBRE':<20}{'ACTIVO':<10}")
    print("-" * 35)

    for materia in materias:
        print(f"ID: {materia['id']}")
        print(f"Nombre: {materia['nombre']}")
        print(f"Activo: {'Sí' if materia['activo'] else 'No'}")
        print("-" * 30)
    
    input()


def buscar_por_materia(materias, id_buscado):
    # Búsqueda lineal: devuelve la posición (índice) de la materia con ese
    # id, o -1 si no la encuentra.
    for index, materia in enumerate(materias):
        if materia['id'] == id_buscado:
            return index
    return -1


def modificar_materia(materias):
    limpiar_pantalla()
    print("=== MODIFICACION DE MATERIA ===")
    print()
    mostrar_materias(materias)

    id_busqueda = validar_numero('Ingrese el ID de la materia a modificar: ')
    posicion = buscar_por_materia(materias, id_busqueda)

    if posicion != -1:
        nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
        while not validar_no_vacio(nuevo_nombre):
            print("[x] Nombre inválido (no puede estar vacío)")
            nuevo_nombre = input("Ingrese el nuevo nombre de la materia: ")
        materias[posicion]['nombre'] = nuevo_nombre
        guardar_materias(materias)

        print(f"Materia modificada: {materias[posicion]}")
        input()
    else:
        print(" [x] No existe una materia con ese ID.")
        input()


def eliminar_materia(materias):
    # Baja lógica: no se borra de la lista, solo se marca activo=False,
    # para no perder las notas que ya referencian a esta materia.
    limpiar_pantalla()
    print("=== BAJA DE MATERIA ===")
    print()
    mostrar_materias(materias)

    id_buscar = validar_numero("Ingrese el ID de la materia a eliminar: ")
    posicion = buscar_por_materia(materias, id_buscar)

    if posicion != -1:
        materias[posicion]['activo'] = False
        input(f'La materia {materias[posicion]["id"]} {materias[posicion]["nombre"]} fue eliminada correctamente.')
    else:
        input(f'[x] No se encontro una materia con el ID: {id_buscar}')


def menu_materias(materias, rol):
    # Submenú de materias. El admin tiene CRUD completo;
    # el viewer solo puede consultar el listado.
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

        # Cada opción chequea también el rol, porque el número "1" significa
        # cosas distintas según si es admin (alta) o viewer (listar).
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
            print('[✓] Volviendo al menú anterior...')
            input()

        else:
            input('[x] Opcion invalida. Presione enter para continuar.')
