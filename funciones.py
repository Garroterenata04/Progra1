# función para agregar un estudiante
def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre: ")

    # se agrega como [nombre, legajo]
    estudiantes.append([nombre])

    print("Estudiante agregado\n")


# función para mostrar estudiantes
def mostrar_estudiantes(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    # recorre la lista
    for i in range(len(estudiantes)):
        print(i, estudiantes[i][0])

    print()


# función para modificar estudiante
def modificar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    mostrar_estudiantes(estudiantes)

    pos= int(input("Ingrese el índice: ")) #posicion en la tabla 

    opcion = input("Modificar (n)ombre: ")

    if opcion == "n":
        nuevo = input("Nuevo nombre: ")
        estudiantes[pos][0] = nuevo

    elif opcion == "t":
        nueva = float(input("Nueva nota: "))
        estudiantes[pos][1] = nueva

    print("Datos modificados\n")


# Baja de alumno
def eliminar_estudiante(estudiante):
    if len (estudiante) == 0:
        print("no hay estudiantes \n")
        return
    mostrar_estudiantes(estudiante)
    pos=int(input("ingrese el legajo a eliminar: ")) #posicion 

    if 0 <= pos <len(estudiante):
        eliminado = estudiante.pop(pos) #elimina el elemento en la posicion que elige el usuario.
        print("El estudiante fue eliminado con exito: ", eliminado[0], "\n") #en baja logica CREO que seria asi
    else:
        print("indice ingresado invalido. \n")                              #if len(estudiante[pos]) == 1:
                                                                            #estudiante[pos].append(False)
                                                                            #(else)estudiante[pos][1] = False
