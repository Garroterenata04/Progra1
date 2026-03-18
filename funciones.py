<<<<<<< HEAD
# AGREGA un estudiante
def agregar_estudiante(estudiantes):

    nombre = input("Ingrese el nombre: ").strip()

    # validación con try/except
    try:
        nota = float(input("Ingrese la nota: "))
    except:
        print("Error: la nota debe ser un número\n")
        return

    # se guarda como [nombre, nota]
=======
# función para agregar un estudiante a la matriz
def agregar_estudiante(estudiantes):

    nombre = input("Ingrese el nombre: ")
    nota = float(input("Ingrese la nota: "))

    # se agrega una nueva fila a la matriz
>>>>>>> e95abe58162d8c2875e3dce239e1b7ec1f7ecb39
    estudiantes.append([nombre, nota])

    print("Estudiante agregado\n")


<<<<<<< HEAD
# MUESTRA todos los estudiantes
def mostrar_estudiantes(estudiantes):

=======
# función para mostrar todos los estudiantes
def mostrar_estudiantes(estudiantes):

    # si la matriz está vacía
>>>>>>> e95abe58162d8c2875e3dce239e1b7ec1f7ecb39
    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    # recorre la matriz
    for i in range(len(estudiantes)):
<<<<<<< HEAD
=======

        # estudiantes[i][0] → nombre
        # estudiantes[i][1] → nota
>>>>>>> e95abe58162d8c2875e3dce239e1b7ec1f7ecb39
        print(i, "-", estudiantes[i][0], "-", estudiantes[i][1])

    print()


<<<<<<< HEAD
# MODIFICA datos
=======
# función para modificar datos de un estudiante
>>>>>>> e95abe58162d8c2875e3dce239e1b7ec1f7ecb39
def modificar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

<<<<<<< HEAD
    mostrar_estudiantes(estudiantes)

    try:
        pos = int(input("Ingrese el índice del estudiante: "))

        # validación de rango
        if pos < 0 or pos >= len(estudiantes):
            print("Índice inválido\n")
            return

    except:
        print("Error: debe ingresar un número\n")
        return

    opcion = input("Modificar (n)ombre o (t)nota: ").lower()

    # cambiar nombre
    if opcion == "n":
        estudiantes[pos][0] = input("Nuevo nombre: ")

    # cambiar nota
    elif opcion == "t":
        try:
            estudiantes[pos][1] = float(input("Nueva nota: "))
        except:
            print("Error: la nota debe ser un número\n")
            return

    else:
        print("Opción inválida\n")
        return
=======
    # muestra la lista para elegir
    mostrar_estudiantes(estudiantes)

    pos = int(input("Ingrese el índice del estudiante: "))

    opcion = input("Modificar (n)ombre o (t)nota: ")

    # modificar nombre
    if opcion == "n":
        nuevo = input("Nuevo nombre: ")
        estudiantes[pos][0] = nuevo

    # modificar nota
    elif opcion == "t":
        nueva = float(input("Nueva nota: "))
        estudiantes[pos][1] = nueva
>>>>>>> e95abe58162d8c2875e3dce239e1b7ec1f7ecb39

    print("Datos modificados\n")


<<<<<<< HEAD
# ELIMINA un estudiante
=======
# función para eliminar un estudiante
>>>>>>> e95abe58162d8c2875e3dce239e1b7ec1f7ecb39
def eliminar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    mostrar_estudiantes(estudiantes)

<<<<<<< HEAD
    try:
        pos = int(input("Ingrese el índice a eliminar: "))

        if pos < 0 or pos >= len(estudiantes):
            print("Índice inválido\n")
            return

    except:
        print("Error: debe ingresar un número\n")
        return

    estudiantes.pop(pos)  # elimina la fila
=======
    pos = int(input("Ingrese el índice a eliminar: "))

    # elimina la fila de la matriz
    estudiantes.pop(pos)
>>>>>>> e95abe58162d8c2875e3dce239e1b7ec1f7ecb39

    print("Estudiante eliminado\n")