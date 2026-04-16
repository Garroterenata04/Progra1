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
        nota_id = notas[-1][0] + 1

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

    notas.append([nota_id, alumno_id, materia_id, nota, tipo])

    input("Nota cargada correctamente")


#----------------------------LISTAR NOTAS----------------------------

def lista_nota(notas):

    if len(notas) == 0:
        input("No hay notas")
        return

    for n in notas:
        print("ID:", n[0])
        print("Alumno:", n[1])
        print("Materia:", n[2])
        print("Nota:", n[3])
        print("Tipo:", n[4])

    input()


#----------------------------MODIFICAR NOTA----------------------------

def modificar_nota(notas):

    if len(notas) == 0:
        input("No hay notas")
        return

    for n in notas:
        print("ID:", n[0])
        print("Nota:", n[3])
        print("Tipo:", n[4])

    nota_id = int(input("Ingrese el ID de la nota a modificar: "))

    posicion = -1

    for i in range(len(notas)):
        if notas[i][0] == nota_id:
            posicion = i
            break

    if posicion == -1:
        input("No se encontro la nota")
        return

    nueva = int(input("Nueva nota: "))
    notas[posicion][3] = nueva

    input("Nota modificada")


#----------------------------ELIMINAR NOTA----------------------------

def eliminar_nota(notas):

    if len(notas) == 0:
        input("No hay notas")
        return

    for n in notas:
        print("ID:", n[0])
        print("Nota:", n[3])
        print("Tipo:", n[4])

    nota_id = int(input("Ingrese el ID de la nota a eliminar: "))

    posicion = -1

    for i in range(len(notas)):
        if notas[i][0] == nota_id:
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

    suma = 0

    for n in notas:
        suma += n[3]

    promedio = suma / len(notas)

    input("Promedio: " + str(promedio))