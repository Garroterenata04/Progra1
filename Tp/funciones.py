# función para agregar un estudiante
def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre: ")
    nota = int(input("Ingrese el la nota: "))

    # se agrega como [nombre, legajo]
    estudiantes.append([nombre, nota])

    print("Estudiante agregado\n")


# función para mostrar estudiantes
def mostrar_estudiantes(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    # recorre la lista
    for i in range(len(estudiantes)):
        print(i, estudiantes[i][0], estudiantes[i][1])

    print()


# función para modificar estudiante
def modificar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    mostrar_estudiantes(estudiantes)

    pos= int(input("Ingrese el índice: ")) #posicion en la tabla 

    opcion = input("Modificar (n)ombre o (t)nota: ")

    if opcion == "n":
        nuevo = input("Nuevo nombre: ")
        estudiantes[pos][0] = nuevo

    elif opcion == "t":
        nueva = float(input("Nueva nota: "))
        estudiantes[pos][1] = nueva

    print("Datos modificados\n")


# función para eliminar estudiante
def eliminar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    mostrar_estudiantes(estudiantes)

    pos = int(input("Ingrese el índice a eliminar: ")) #posicion en la tabla 

    estudiantes.pop(pos)

    print("Estudiante eliminado\n")