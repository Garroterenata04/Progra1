from funciones import limpiar_pantalla, validar_no_vacio, validar_numero, validar_nota
from matrices import guardar_notas

# Módulo CRUD de notas. Cada nota relaciona un estudiante (id_estudiante)
# con una materia (id_materia) y un tipo de evaluación (descripcion).
# A diferencia de estudiantes/materias, eliminar_nota borra realmente el
# registro (no hay baja lógica para notas).

SEP = "-" * 40


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

    # Se muestran los estudiantes y materias activos para facilitar la selección.
    print("--- ESTUDIANTES ACTIVOS ---")
    for e in estudiantes:
        if e['activo']:
            print(f"  {e['legajo']} - {e['nombre']}")

    print()
    print("--- MATERIAS ACTIVAS ---")
    for m in materias:
        if m['activo']:
            print(f"  {m['id']} - {m['nombre']}")
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

def lista_nota(notas, estudiantes, materias):
    """Muestra el listado de notas con nombre del alumno y de la materia."""
    if len(notas) == 0:
        input("[x] No hay notas registradas. Presione enter...")
        return

    limpiar_pantalla()
    print("=== LISTA DE NOTAS ===")
    print()

    for n in notas:
        # Resolver ids a nombres para mostrar información legible
        nombre_alumno  = next((e["nombre"] for e in estudiantes if e["legajo"] == n["id_estudiante"]), str(n["id_estudiante"]))
        nombre_materia = next((m["nombre"] for m in materias   if m["id"]     == n["id_materia"]),    str(n["id_materia"]))

        print(f"  ID       : {n['id']}")
        print(f"  Alumno   : {nombre_alumno}")
        print(f"  Materia  : {nombre_materia}")
        print(f"  Nota     : {n['nota']}")
        print(f"  Tipo     : {n['descripcion']}")
        print(SEP)

    input("\nPresione enter para continuar...")


#----------------------------MODIFICAR NOTA----------------------------

def modificar_nota(notas):
    """Permite cambiar el valor numérico de una nota existente."""
    limpiar_pantalla()
    print("=== MODIFICACION DE NOTA ===")
    print()

    if len(notas) == 0:
        input("[x] No hay notas registradas. Presione enter...")
        return

    for n in notas:
        print(f"  ID {n['id']} - {n['descripcion']} : {n['nota']}")
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

    for n in notas:
        print(f"  ID {n['id']} - {n['descripcion']} : {n['nota']}")
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
