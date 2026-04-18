from funciones import limpiar_pantalla


def cargar_notas():
    return [
        {"id": 1, "id_estudiante": 1, "id_materia": 1, "nota": 8, "descripcion": "Primer parcial"},
        {"id": 2, "id_estudiante": 1, "id_materia": 2, "nota": 9, "descripcion": "Segundo parcial"},
        {"id": 3, "id_estudiante": 2, "id_materia": 1, "nota": 7, "descripcion": "Primer parcial"},
        {"id": 4, "id_estudiante": 2, "id_materia": 3, "nota": 10, "descripcion": "Final"},
        {"id": 5, "id_estudiante": 3, "id_materia": 4, "nota": 6, "descripcion": "Primer parcial"}
    ]


#----------------------------MENU NOTAS----------------------------

def menu_notas(notas, estudiantes, materias, rol):

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
        else:  # viewer
            print("1 - Lista de notas")
        
        print("0 - Volver")

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
            input("Volviendo...")

        else:
            input("Opcion invalida")


#----------------------------AGREGAR NOTA----------------------------

def agregar_nota(notas, estudiantes, materias):
    limpiar_pantalla()
    print("=== ALTA DE NOTA ===")
    print()

    if len(estudiantes) == 0:
        input("No hay estudiantes cargados")
        return

    if len(materias) == 0:
        input("No hay materias cargadas")
        return

    if len(notas) == 0:
        nota_id = 1
    else:
        nota_id = notas[-1]["id"] + 1

    print("\n--- ESTUDIANTES ---")
    for e in estudiantes:
        print(f"ID : {e['legajo']} - Nombre: {e['nombre']}")

    print("\n--- MATERIAS ---")
    for m in materias:
        print(f"ID: {m['id']} - Nombre: {m['nombre']}")

    alumno_id = int(input("Ingrese el legajo del alumno: "))
    materia_id = int(input("Ingrese el ID de la materia: "))
    nota = int(input("Ingrese la nota: "))

    print("Tipo de nota:")
    print("1 - Primer parcial")
    print("2 - Segundo parcial")
    print("3 - Final")

    opcion = input("Seleccione: ")

    if opcion == "1":
        tipo = "Primer parcial"
    elif opcion == "2":
        tipo = "Segundo parcial"
    elif opcion == "3":
        tipo = "Final"
    else:
        input("Tipo invalido")
        return
    
    existe = list(filter(lambda n: n["id_estudiante"] == alumno_id  #no existe si esta vacia
                               and n["id_materia"] == materia_id 
                               and n["descripcion"] == tipo, notas))

    if existe: #lambda, filter
        input("Esa nota ya existe para este alumno")
        return

    notas.append({#diccionarios y para que el acceso sea mas claro
        "id": nota_id,
        "id_estudiante": alumno_id,
        "id_materia": materia_id,
        "nota": nota,
        "descripcion": tipo
    })

    input("Nota cargada correctamente")


#----------------------------LISTAR NOTAS----------------------------

def lista_nota(notas, estudiantes, materias):

    if len(notas) == 0:
        input("No hay notas")
        return

    limpiar_pantalla()
    print("=== LISTA DE NOTAS ===")
    print()
    for n in notas:
        # Buscar nombre del estudiante
        nombre_alumno = str(n["id_estudiante"])  # Si no encuentra, muestra el ID
        for e in estudiantes:
            if e["legajo"] == n["id_estudiante"]:
                nombre_alumno = e["nombre"]
                break
        
        # Buscar nombre de la materia
        nombre_materia = str(n["id_materia"])  # Si no encuentra, muestra el ID
        for m in materias:
            if m["id"] == n["id_materia"]:
                nombre_materia = m["nombre"]
                break
        
        print(f"ID: {n['id']}")
        print(f"Alumno: {nombre_alumno}")
        print(f"Materia: {nombre_materia}")
        print(f"Nota: {n['nota']}")
        print(f"Tipo: {n['descripcion']}")
        print("-" * 30)

    input()


#----------------------------MODIFICAR NOTA----------------------------

def modificar_nota(notas):
    limpiar_pantalla()
    print("=== MODIFICACION DE NOTA ===")
    print()

    if len(notas) == 0:
        input("No hay notas")
        return

    for n in notas:
        print("ID:", n["id"])
        print("Nota:", n["nota"])
        print("Tipo:", n["descripcion"])

    nota_id = int(input("Ingrese el ID de la nota a modificar: "))

    posicion = -1

    for i in range(len(notas)):
        if notas[i]["id"] == nota_id:
            posicion = i
            break

    if posicion == -1:
        input("No se encontro la nota")
        return

    nueva = int(input("Nueva nota: "))
    notas[posicion]["nota"] = nueva

    input("Nota modificada")


#----------------------------ELIMINAR NOTA----------------------------

def eliminar_nota(notas):
    limpiar_pantalla()
    print("=== ELIMINACION DE NOTA ===")
    print()

    if len(notas) == 0:
        input("No hay notas")
        return

    for n in notas:
        print("ID:", n["id"])
        print("Nota:", n["nota"])
        print("Tipo:", n["descripcion"])
    nota_id = int(input("Ingrese el ID de la nota a eliminar: "))

    posicion = -1

    for i in range(len(notas)):
        if notas[i]["id"] == nota_id:
            posicion = i
            break

    if posicion == -1:
        input("No se encontro la nota")
        return

    notas.pop(posicion)

    input("Nota eliminada correctamente")