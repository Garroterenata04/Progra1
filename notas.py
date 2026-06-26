from funciones import limpiar_pantalla, validar_no_vacio, validar_numero, validar_nota, imprimir_tabla
from matrices import guardar_notas

# Módulo CRUD de notas. Cada nota relaciona un estudiante (id_estudiante)
# con una materia (id_materia) y un tipo de evaluación (descripcion).
# A diferencia de estudiantes/materias, eliminar_nota borra realmente el
# registro (no hay baja lógica para notas).


#----------------------------BUSQUEDA RECURSIVA----------------------------

def buscar_nota_recursiva(notas, nota_id, indice=0):
    """Busca una nota por id de forma recursiva. Devuelve el índice o -1.
    Caso base 1: se recorrió toda la lista → devuelve -1.
    Caso base 2: se encontró la nota en la posición actual → devuelve indice.
    Caso recursivo: avanzar al siguiente elemento."""
    if indice >= len(notas):
        return -1
    if notas[indice]["id"] == nota_id:
        return indice
    return buscar_nota_recursiva(notas, nota_id, indice + 1)


#----------------------------MENU NOTAS----------------------------

def menu_notas(notas, estudiantes, materias, rol):
    """Submenú de notas. Admin tiene CRUD completo; viewer solo puede listar."""
    seleccion = ""

    while seleccion != "0":
        limpiar_pantalla()
        print("=== MENU NOTAS ===")
        print()

        if rol == 'admin':
            print("1 - Ingresar nota")
            print("2 - Modificar nota")
            print("3 - Lista de notas")
            print("4 - Eliminar nota")
        else:
            print("1 - Lista de notas")

        print("0 - Volver")
        print()
        seleccion = input("Opcion: ")

        if seleccion == "1" and rol == 'admin':
            agregar_nota(notas, estudiantes, materias)
        elif seleccion == "2" and rol == 'admin':
            modificar_nota(notas)
        elif (seleccion == "3" and rol == 'admin') or (seleccion == "1" and rol == 'viewer'):
            lista_nota(notas, estudiantes, materias)
        elif seleccion == "4" and rol == 'admin':
            eliminar_nota(notas)
        elif seleccion == "0":
            input("[✓] Volviendo... Presione enter...")
        else:
            input("[x] Opcion invalida. Presione enter...")


#----------------------------AGREGAR NOTA----------------------------

def agregar_nota(notas, estudiantes, materias):
    """Solicita datos por consola y registra una nueva nota para un estudiante."""
    limpiar_pantalla()
    print("=== ALTA DE NOTA ===")
    print()

    if len(estudiantes) == 0:
        input("[x] No hay estudiantes cargados. Presione enter...")
        return

    if len(materias) == 0:
        input("[x] No hay materias cargadas. Presione enter...")
        return

    nota_id = 1 if len(notas) == 0 else notas[-1]["id"] + 1

    print("--- ESTUDIANTES ACTIVOS ---")
    imprimir_tabla(['Legajo', 'Nombre'], [[e['legajo'], e['nombre']] for e in estudiantes if e['activo']])
    print()
    print("--- MATERIAS ACTIVAS ---")
    imprimir_tabla(['ID', 'Nombre'], [[m['id'], m['nombre']] for m in materias if m['activo']])
    print()

    alumno_id = validar_numero("Legajo del alumno : ")
    estudiante_existe = any(e['legajo'] == alumno_id and e['activo'] for e in estudiantes)
    if not estudiante_existe:
        input("[x] El estudiante no existe o está inactivo. Presione enter...")
        return

    materia_id = validar_numero("ID de la materia  : ")
    materia_existe = any(m['id'] == materia_id and m['activo'] for m in materias)
    if not materia_existe:
        input("[x] La materia no existe o está inactiva. Presione enter...")
        return

    nota = validar_nota("Nota (0-10)       : ")

    print()
    print("Tipo de evaluacion:")
    print("  1 - Primer parcial")
    print("  2 - Segundo parcial")
    print("  3 - Final")
    print()

    opcion = input("Seleccione tipo : ")
    while not validar_no_vacio(opcion):
        print("[x] Debe seleccionar un tipo.")
        opcion = input("Seleccione tipo : ")

    if opcion == "1":
        tipo = "Primer parcial"
    elif opcion == "2":
        tipo = "Segundo parcial"
    elif opcion == "3":
        tipo = "Final"
    else:
        input("[x] Tipo inválido. Presione enter...")
        return

    # No se permite cargar dos veces la misma evaluación (mismo alumno,
    # misma materia y mismo tipo) para evitar notas duplicadas.
    existe = list(filter(
        lambda n: n["id_estudiante"] == alumno_id
               and n["id_materia"] == materia_id
               and n["descripcion"] == tipo,
        notas
    ))

    if existe:
        input("[x] Esa nota ya existe para este alumno. Presione enter...")
        return

    notas.append({
        "id":           nota_id,
        "id_estudiante": alumno_id,
        "id_materia":    materia_id,
        "nota":          nota,
        "descripcion":   tipo
    })

    try:
        guardar_notas(notas)
        input(f"\n[✓] Nota cargada correctamente (ID {nota_id}). Presione enter...")
    except OSError as e:
        notas.pop()
        input(f"[x] Error al guardar la nota: {e}")


#----------------------------LISTAR NOTAS----------------------------

def _filas_notas(notas_filtradas, estudiantes, materias):
    """Convierte una lista de notas en filas para imprimir_tabla."""
    filas = []
    for n in notas_filtradas:
        nombre_alumno  = next((e["nombre"] for e in estudiantes if e["legajo"] == n["id_estudiante"]), str(n["id_estudiante"]))
        nombre_materia = next((m["nombre"] for m in materias   if m["id"]     == n["id_materia"]),    str(n["id_materia"]))
        filas.append([n['id'], nombre_alumno, nombre_materia, n['nota'], n['descripcion']])
    return filas


def _notas_por_alumno(notas, estudiantes, materias):
    """Muestra notas filtradas por el legajo que ingrese el usuario."""
    legajos_con_notas = list({n["id_estudiante"] for n in notas})
    alumnos_con_notas = [e for e in estudiantes if e["legajo"] in legajos_con_notas]

    if len(alumnos_con_notas) == 0:
        input("[x] No hay alumnos con notas registradas. Presione enter...")
        return

    print("--- ALUMNOS CON NOTAS ---")
    imprimir_tabla(['Legajo', 'Nombre'], [[e['legajo'], e['nombre']] for e in alumnos_con_notas])
    print()

    legajo = validar_numero("Legajo del alumno : ")

    notas_alumno = [n for n in notas if n["id_estudiante"] == legajo]
    if len(notas_alumno) == 0:
        input(f"[x] No hay notas para el legajo {legajo}. Presione enter...")
        return

    nombre = next((e["nombre"] for e in estudiantes if e["legajo"] == legajo), str(legajo))
    print(f"\nNotas de {nombre}:")
    imprimir_tabla(['ID', 'Alumno', 'Materia', 'Nota', 'Tipo'], _filas_notas(notas_alumno, estudiantes, materias))
    input("\nPresione enter para continuar...")


def lista_nota(notas, estudiantes, materias):
    """Submenú de listado de notas: ver todas o buscar por alumno."""
    if len(notas) == 0:
        input("[x] No hay notas registradas. Presione enter...")
        return

    seleccion = ""
    while seleccion != "0":
        limpiar_pantalla()
        print("=== LISTA DE NOTAS ===")
        print()
        print("1 - Ver todas las notas")
        print("2 - Buscar por alumno")
        print("0 - Volver")
        print()
        seleccion = input("Opcion: ")

        if seleccion == "1":
            limpiar_pantalla()
            print("=== TODAS LAS NOTAS ===")
            print()
            imprimir_tabla(['ID', 'Alumno', 'Materia', 'Nota', 'Tipo'], _filas_notas(notas, estudiantes, materias))
            input("\nPresione enter para continuar...")
        elif seleccion == "2":
            limpiar_pantalla()
            print("=== BUSCAR NOTAS POR ALUMNO ===")
            print()
            _notas_por_alumno(notas, estudiantes, materias)
        elif seleccion == "0":
            pass
        else:
            input("[x] Opcion invalida. Presione enter...")


#----------------------------MODIFICAR NOTA----------------------------

def modificar_nota(notas):
    """Permite cambiar el valor numérico de una nota existente."""
    limpiar_pantalla()
    print("=== MODIFICACION DE NOTA ===")
    print()

    if len(notas) == 0:
        input("[x] No hay notas registradas. Presione enter...")
        return

    imprimir_tabla(['ID', 'Tipo', 'Nota'], [[n['id'], n['descripcion'], n['nota']] for n in notas])
    print()

    nota_id  = validar_numero("ID de la nota a modificar : ")
    posicion = buscar_nota_recursiva(notas, nota_id)

    if posicion == -1:
        input("[x] No se encontró la nota. Presione enter...")
        return

    nueva          = validar_nota("Nueva nota (0-10)         : ")
    nota_anterior  = notas[posicion]["nota"]
    notas[posicion]["nota"] = nueva

    try:
        guardar_notas(notas)
        input(f"\n[✓] Nota actualizada de {nota_anterior} a {nueva}. Presione enter...")
    except OSError as e:
        notas[posicion]["nota"] = nota_anterior
        input(f"[x] Error al guardar los cambios: {e}")


#----------------------------ELIMINAR NOTA----------------------------

def eliminar_nota(notas):
    """Elimina definitivamente una nota de la lista (no hay baja lógica para notas)."""
    limpiar_pantalla()
    print("=== ELIMINACION DE NOTA ===")
    print()

    if len(notas) == 0:
        input("[x] No hay notas registradas. Presione enter...")
        return

    imprimir_tabla(['ID', 'Tipo', 'Nota'], [[n['id'], n['descripcion'], n['nota']] for n in notas])
    print()

    nota_id  = validar_numero("ID de la nota a eliminar : ")
    posicion = buscar_nota_recursiva(notas, nota_id)

    if posicion == -1:
        input("[x] No se encontró la nota. Presione enter...")
        return

    nota_eliminada = notas.pop(posicion)

    try:
        guardar_notas(notas)
        input(f"[✓] Nota ID {nota_id} eliminada. Presione enter...")
    except OSError as e:
        notas.insert(posicion, nota_eliminada)
        input(f"[x] Error al guardar los cambios: {e}")
