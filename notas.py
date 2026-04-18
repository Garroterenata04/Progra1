from funciones import limpiar_pantalla

#----------------------------MENU NOTAS----------------------------

def menu_notas(notas, estudiantes, materias):

    seleccion = ""

    while seleccion != "0":

        limpiar_pantalla()

        print("1 - Ingresar nota")
        print("2 - Modificar nota")
        print("3 - Promedio de notas")
        print("4 - Lista de notas")
        print("5 - Eliminar nota")
        print("0 - Volver")

        seleccion = input("Opcion: ")

        if seleccion == "1":
            agregar_nota(notas, estudiantes, materias)

        elif seleccion == "2":
            modificar_nota(notas)

        elif seleccion == "3":
            promedio_nota(notas)

        elif seleccion == "4":
            lista_nota(notas)

        elif seleccion == "5":
            eliminar_nota(notas)

        elif seleccion == "0":
            input("Volviendo...")

        else:
            input("Opcion invalida")


#----------------------------AGREGAR NOTA----------------------------

def agregar_nota(notas, estudiantes, materias):

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
        print(f"ID : {e['id']} - Nombre: {e['nombre']}")

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

def lista_nota(notas):

    if len(notas) == 0:
        input("No hay notas")
        return

    for n in notas:
        print("ID:", n["id"])
        print("Alumno:", n["id_estudiante"])
        print("Materia:", n["id_materia"])
        print("Nota:", n["nota"])
        print("Tipo:", n["descripcion"])

    input()


#----------------------------MODIFICAR NOTA----------------------------

def modificar_nota(notas):

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


#----------------------------PROMEDIO----------------------------
def promedio_nota(notas):

    if len(notas) == 0:
        input("No hay notas")
        return

    alumno_id = int(input("ID estudiante: "))
    materia_id = int(input("ID materia: "))

    suma = 0
    contador = 0

    for n in notas:
        if n["id_estudiante"] == alumno_id and n["id_materia"] == materia_id:
            suma += n["nota"]
            contador += 1

    if contador == 0:
        input("No hay notas para ese alumno/materia")
        return

    promedio = suma / contador

    print("Promedio:", promedio)
    input()