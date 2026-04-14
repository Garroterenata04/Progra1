from pathlib import Path
from funciones import limpiar_pantalla

SCRIPT_DIR = Path(__file__).parent
ESTUDIANTES_FILE = SCRIPT_DIR / 'estudiantes.txt'


def cargar_estudiantes():
    alumnos = []
    alumno_actual = {}

    try:
        with open(ESTUDIANTES_FILE, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()

                if linea == "":
                    if alumno_actual:
                        alumnos.append(alumno_actual)
                        alumno_actual = {}
                else:
                    clave, valor = linea.split(": ", 1)
                    if clave == "Legajo":
                        alumno_actual["legajo"] = int(valor)
                    elif clave == "Nombre":
                        alumno_actual["nombre"] = valor
                    elif clave == "Mail":
                        alumno_actual["mail"] = valor
                    elif clave == "Estado":
                        alumno_actual["estado"] = valor == "True"

        if alumno_actual:
            alumnos.append(alumno_actual)
    except FileNotFoundError:
        pass

    return alumnos


def guardar_estudiantes(estudiantes):
    with open(ESTUDIANTES_FILE, 'w', encoding='utf-8') as archivo:
        for alumno in estudiantes:
            archivo.write(f"Legajo: {alumno['legajo']}\n")
            archivo.write(f"Nombre: {alumno['nombre']}\n")
            archivo.write(f"Mail: {alumno['mail']}\n")
            archivo.write(f"Estado: {alumno['estado']}\n\n")


def listar_estudiantes_archivo(alumnos):
    print("\n===== LISTA DE ALUMNOS =====\n")

    for alumno in alumnos:
        print(f"Legajo : {alumno['legajo']}")
        print(f"Nombre : {alumno['nombre']}")
        print(f"Mail   : {alumno['mail']}")
        print(f"Estado : {'Activo' if alumno['estado'] else 'Inactivo'}")
        print("-" * 30)

    input()


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
    guardar_estudiantes(estudiantes)

    input('Alumno cargado exitosamente, presione enter para continuar...')


def mostrar_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes\n")
        return

    for alumno in estudiantes:
        print(alumno['legajo'], alumno['nombre'])

    print()


def buscar_pos_estudiante(estudiantes, legajo_buscado):
    for index, alumno in enumerate(estudiantes):
        if alumno['legajo'] == legajo_buscado:
            return index
    return -1


def prueba_modificar_estudiante(estudiantes):
    mostrar_estudiantes(estudiantes)

    legajo_busqueda = int(input('Ingrese el legajo a modificar: '))
    posicion = buscar_pos_estudiante(estudiantes, legajo_busqueda)

    if posicion != -1:
        nuevo_nombre = input("Ingrese el nuevo nombre y apellido: ")
        nuevo_mail = input("Ingrese el nuevo mail: ")

        estudiantes[posicion]['nombre'] = nuevo_nombre
        estudiantes[posicion]['mail'] = nuevo_mail
        guardar_estudiantes(estudiantes)

        print("Alumno modificado:", estudiantes[posicion])
        input()
    else:
        print("No existe un alumno con ese legajo.")
        input()


def eliminar_estudiante(estudiantes):
    mostrar_estudiantes(estudiantes)

    legajo_buscar = int(input("Ingrese el legajo a eliminar: "))
    posicion = buscar_pos_estudiante(estudiantes, legajo_buscar)

    if posicion != -1:
        estudiantes[posicion]['estado'] = False
        guardar_estudiantes(estudiantes)
        input(f'El estudiante {estudiantes[posicion]["legajo"]} {estudiantes[posicion]["nombre"]} fue eliminado correctamente.')
    else:
        input(f'No se encontro un estudiante con el legajo: {legajo_buscar}')


def menu_estudiantes(estudiantes):
    seleccion = ""

    while seleccion != '0':
        limpiar_pantalla()

        print("1. Alta de estudiante")
        print("2. Modificacion de estudiante")
        print("3. Baja de estudiante")
        print("4. Lista de estudiantes")
        print("0. Volver")

        seleccion = input('Opcion: ')

        if seleccion == '1':
            limpiar_pantalla()
            agregar_estudiante(estudiantes)

        elif seleccion == '2':
            limpiar_pantalla()
            prueba_modificar_estudiante(estudiantes)

        elif seleccion == '3':
            eliminar_estudiante(estudiantes)

        elif seleccion == '4':
            limpiar_pantalla()
            listar_estudiantes_archivo(estudiantes)
            input()

        elif seleccion == '0':
            print('Volviendo al menu anterior...')
            input()

        else:
            limpiar_pantalla()
            print('Opcion invalida')
            input()
