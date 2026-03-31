#----------------------------RECURSOS----------------------------
import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')      # Windows
    else:
        os.system('clear')    # Mac / Linux


# ----------------------------FUNCIONES ESTUDIANTES----------------------------

# función para agregar un estudiante
def agregar_estudiante(estudiantes):

    #asigno variable para el estudiante nuevo
    estudianteNuevo = []


    #Se autocompleta el legajo sumando uno al ultimo de la lista y se piden al usuario el resto de los datos
    legajo = estudiantes[-1][0] + 1
    nombre = input('Ingrese el nombre y apellido: \n')
    email = input('Ingrese el mail: \n')

    #Se agrega a la lista cada item y luego se devuelve la lista con el estudiante nuevo
    estudianteNuevo.append(legajo)
    estudianteNuevo.append(nombre)
    estudianteNuevo.append(email)
    estudianteNuevo.append(True)
    
    return(estudianteNuevo)



# función para mostrar estudiantes
def mostrar_estudiantes(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    # recorre la lista
    for i in range(len(estudiantes)):
        print(estudiantes[i][0], estudiantes[i][1])

    print()



# función para modificar estudiante



def modificar_estudiante(estudiantes):

    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        input()
        return

    mostrar_estudiantes(estudiantes)

    pos = int(input("Ingrese el índice del estudiante a modificar: "))

    if pos < 0 or pos >= len(estudiantes):
        print("Índice inválido\n")
        input()
        return

    print("\n¿Qué desea modificar?")
    print("1 - Nombre")
    print("2 - Email")
    print("3 - Ambos")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nuevo_nombre = input("Nuevo nombre: ")
        estudiantes[pos][1] = nuevo_nombre

    elif opcion == "2":
        nuevo_email = input("Nuevo email: ")
        estudiantes[pos][2] = nuevo_email

    elif opcion == "3":
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_email = input("Nuevo email: ")
        estudiantes[pos][1] = nuevo_nombre
        estudiantes[pos][2] = nuevo_email

    else:
        print("Opción inválida")
        input()
        return

    print("\nDatos modificados correctamente")
    input()






# baja estudiante
def eliminar_estudiante(estudiantes):
    
    mostrar_estudiantes(estudiantes)

    pos = int(input("ingrese el legajo a eliminar: "))

    for i in range (len(estudiantes)):

        if estudiantes [i][0] == pos:
            estudiantes [i][3] = False
            print("El estudiante fue eliminado correctamente: ", estudiantes [i][1])
            input()

    return

#----------------------------FUNCIONES MATERIAS----------------------------

def agregar_materia(materias):

    materiaNueva = []

    #Se autocompleta el id de materia y se pide al usuario el nombre
    id = materias[-1][0] + 1
    nombre = input('Ingrese el nombre de la materia: \n')

    #Se agregan a la lista los parametros de la materia para luego devolverla
    materiaNueva.append(id)
    materiaNueva.append(nombre)
    materiaNueva.append(True)

    input(f'Se agregó correctamente la materia: {materiaNueva} presione enter para continuar')
    
    return(materiaNueva)


#----------------------------FUNCIONES MENU----------------------------

def menu_estudiantes(estudiantes):
    

    seleccion = " "

    #Ciclo para el menu
    while seleccion != '0':

        limpiar_pantalla()        

        #Opciones
        print("1. Alta de estudiante")
        print("2. Modificacion de estudiante")
        print("3. Baja de estudiante")
        print("4. Lista de estudiantes")
        print("0. Volver")

        seleccion = input ('Opcion: ')


        #Asigno funcion en base a la opcion ingresada y capturo el error en un numero no esperado
        if seleccion == '1':
            
            limpiar_pantalla()
            estudiantes.append(agregar_estudiante(estudiantes))

        elif seleccion == '2':

            limpiar_pantalla()

            print('Funcion de modificar')
            #modificar_estudiante()
            input()

        elif seleccion == '3':
            eliminar_estudiante (estudiantes)
        
            
        elif seleccion == '4':

            limpiar_pantalla()

            print('2. Funcion listar')
            print(estudiantes)
            #Listar_estudiantes()        
            input()

        elif seleccion == '0':

            print('volviendo al menu anterior...')         
            input()
        
        else:
            limpiar_pantalla()
            print('Opcion invalida')
            input()

    return()

def menu_materias (materias):

    seleccion = ""

    #ciclo para el menu de materias
    while seleccion != '0':

        limpiar_pantalla()

        print("1. Alta de materias")
        print("2. Modificacion de materias")
        print("3. Baja de materia")
        print("4. Lista de materias")
        print("0. Volver\n")

        seleccion = input('Opcion:')

        #Asigno funcion en base a la opcion ingresada y capturo el error en un numero no esperado
        if seleccion == '1':

            limpiar_pantalla()

            materias.append(agregar_materia(materias))
        
        elif seleccion == '2':
            input()

        elif seleccion == '3':
            input()

        elif seleccion == '4':

            limpiar_pantalla()

            print('2. Funcion listar')
            print(materias)
            #Listar_estudiantes()        
            input()

        elif seleccion == '0':

            print('volviendo al menu anterior...')         
            input()

        else:
            input()
