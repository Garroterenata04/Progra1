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
    estudiantes.append([nombre, nota])

    print("Estudiante agregado\n")


# MUESTRA todos los estudiantes
def mostrar_estudiantes(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    # recorre la matriz
    for i in range(len(estudiantes)):
        print(i, "-", estudiantes[i][0], "-", estudiantes[i][1])

    print()


# MODIFICA datos
def modificar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

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

    print("Datos modificados\n")


# ELIMINA un estudiante
def eliminar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    mostrar_estudiantes(estudiantes)

    try:
        pos = int(input("Ingrese el índice a eliminar: "))

        if pos < 0 or pos >= len(estudiantes):
            print("Índice inválido\n")
            return

    except:
        print("Error: debe ingresar un número\n")
        return

    estudiantes.pop(pos)  # elimina la fila

    print("Estudiante eliminado\n")