# función para agregar un estudiante
def agregar_estudiante(estudiantes):

    estudianteNuevo = []
    
    legajo = estudiantes[-1][0] + 1
    nombre = input('Ingrese el nombre y apellido: \n')
    email = input('Ingrese el mail: \n')

    estudianteNuevo.append(legajo)
    estudianteNuevo.append(nombre)
    estudianteNuevo.append(email)
    
    return(estudianteNuevo)



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


# baja estudiante
def eliminar_estudiante(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return
    mostrar_estudiantes(estudiantes)

    pos=int(input("ingrese el indice a eliminar: "))

    if 0<= pos <len(estudiantes):
        eliminado=estudiantes.pop(pos) #elimina el legajo en esa posicion y lo guarda en la variable
        print("estudiante eliminado correctamente: ", eliminado[1], "\n")
    else:
        print("indice ingresado incorrecto. ")