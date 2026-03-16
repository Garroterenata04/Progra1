# función para agregar un estudiante a la matriz
def agregar_estudiante(estudiantes):

    nombre = input("Ingrese el nombre: ")
    nota = float(input("Ingrese la nota: "))

    # se agrega una nueva fila a la matriz
    estudiantes.append([nombre, nota])

    print("Estudiante agregado\n")


# función para mostrar todos los estudiantes
def mostrar_estudiantes(estudiantes):

    # si la matriz está vacía
    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    # recorre la matriz
    for i in range(len(estudiantes)):

        # estudiantes[i][0] → nombre
        # estudiantes[i][1] → nota
        print(i, "-", estudiantes[i][0], "-", estudiantes[i][1])

    print()


# función para modificar datos de un estudiante
def modificar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

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

    print("Datos modificados\n")


# función para eliminar un estudiante
def eliminar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    mostrar_estudiantes(estudiantes)

    pos = int(input("Ingrese el índice a eliminar: "))

    # elimina la fila de la matriz
    estudiantes.pop(pos)

    print("Estudiante eliminado\n")