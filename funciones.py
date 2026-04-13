#----------------------------RECURSOS----------------------------
import os

from pathlib import Path

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')      # Windows
    else:
        os.system('clear')    # Mac / Linux


# ----------------------------FUNCIONES ESTUDIANTES----------------------------

def cargar_estudiantes():
    
    alumnos = []
    alumno_actual = {}

    with open("estudiantes.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea == "":
                if alumno_actual:
                    alumnos.append(alumno_actual)
                    alumno_actual = {}
            else:
                clave, valor = linea.split(": ")

                if clave == "Legajo":
                    alumno_actual["legajo"] = int(valor)
                elif clave == "Nombre":
                    alumno_actual["nombre"] = valor
                elif clave == "Mail":
                    alumno_actual["mail"] = valor
                elif clave == "Estado":
                    alumno_actual["estado"] = True if valor == "True" else False


    if alumno_actual:
        alumnos.append(alumno_actual)

    return alumnos

def listar_estudiantes_archivo(alumnos):

    print("\n===== LISTA DE ALUMNOS =====\n")

    for alumno in alumnos:
        print(f"Legajo : {alumno['legajo']}")
        print(f"Nombre : {alumno['nombre']}")
        print(f"Mail   : {alumno['mail']}")
        print(f"Estado : {'Activo' if alumno['estado'] else 'Inactivo'}")
        print("-" * 30)

    input()


# función para agregar un estudiante
def agregar_estudiante(estudiantes):

    nombre = input('Ingrese el nombre del alumno: ')
    mail = input('Ingrese el mail: ')

    if len(estudiantes) == 0:
        nuevo_legajo = 1
    else:
        nuevo_legajo = estudiantes[-1]['legajo'] + 1

    nuevo_estudiante = {
        'legajo': nuevo_legajo,
        'nombre': nombre,
        'mail': mail,
        'estado': True 
    }

    estudiantes.append(nuevo_estudiante)

    with open('estudiantes.txt', "w") as archivo:
        for alumno in estudiantes:
            archivo.write(f"Legajo: {alumno['legajo']}\n")
            archivo.write(f"Nombre: {alumno['nombre']}\n")
            archivo.write(f"Mail: {alumno['mail']}\n")
            archivo.write(f"Estado: {alumno['estado']}\n\n")
    
    input('Alumno cargado exitosamente, presione enter para continuar...')




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

#Otra versión de modificar estudiantes, separo la busqueda de la modificacion

def prueba_modificar_estudiante(estudiantes):

    mostrar_estudiantes(estudiantes)

    legajo_busqueda = int(input('Ingrese el legajo a modificar'))

    posicion = buscar_pos_estudiante(estudiantes, legajo_busqueda)

    if posicion != -1:

        nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ")
        nuevo_mail = input("Ingrese el nuevo mail: ")

        estudiantes[posicion][1] = nuevo_nombre
        estudiantes[posicion][2] = nuevo_mail


        print("Alumno modificado:", estudiantes[posicion])
        input()

    else:
        print("No existe un alumno con ese legajo.")
        input ()


# Funcion para devolver la posicion del estudiante buscado por numero de legajo

def buscar_pos_estudiante(estudiantes, legajo_buscado):
     
    i = 0

    while i < len(estudiantes) and estudiantes [i][0] != legajo_buscado:
         
         i += 1

    if i < len(estudiantes):
        return i
    else:
        return -1



# baja estudiante
def eliminar_estudiante(estudiantes):
    
    mostrar_estudiantes(estudiantes)

    legajo_buscar = int(input("ingrese el legajo a eliminar: "))

    posicion = buscar_pos_estudiante(estudiantes, legajo_buscar)

    if posicion != -1:
        estudiantes[posicion][3] = False
        input(f'el estudiante {estudiantes[posicion][0]} {estudiantes[posicion][1]} fue eliminado correctamente.')

    else:
        input(f'No se encontro un estudiante con el legajo: {legajo_buscar}')

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
            agregar_estudiante(estudiantes)

        elif seleccion == '2':

            limpiar_pantalla()
            prueba_modificar_estudiante(estudiantes)
            #modificar_estudiante(estudiantes)

        elif seleccion == '3':
            eliminar_estudiante (estudiantes)
        
            
        elif seleccion == '4':

            limpiar_pantalla()
            listar_estudiantes_archivo(estudiantes)      
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
