# importa todas las funciones del archivo funciones.py
from funciones import *
from matrices import *
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
USERS_FILE = SCRIPT_DIR / 'users.txt'

def load_users():
    users = []
    try:
        with open(USERS_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    email, password = line.strip().split(',')
                    users.append({'email': email, 'password': password})
    except FileNotFoundError:
        pass
    return users

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        for user in users:
            f.write(f"{user['email']},{user['password']}\n")

def login_menu():
    users = load_users()
    while True:
        limpiar_pantalla()
        print("Sistema de Gestión Académica")
        print("1 - Iniciar sesión")
        print("2 - Crear usuario")
        print("0 - Salir")
        opcion = input('Opción: ')
        if opcion == '1':
            email = input('Email: ')
            password = input('Contraseña: ')
            for user in users:
                if user['email'] == email and user['password'] == password:
                    print("Login exitoso")
                    input("Presione enter para continuar")
                    return True
            print("Email o contraseña incorrectos")
            input("Presione enter para continuar")
        elif opcion == '2':
            email = input('Email: ')
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                print("Email inválido")
                input("Presione enter para continuar")
                continue
            if any(u['email'] == email for u in users):
                print("Email ya registrado")
                input("Presione enter para continuar")
                continue
            password = input('Contraseña: ')
            confirm = input('Confirmar contraseña: ')
            if password != confirm:
                print("Contraseñas no coinciden")
                input("Presione enter para continuar")
                continue
            users.append({'email': email, 'password': password})
            save_users(users)
            print("Usuario creado exitosamente")
            input("Presione enter para continuar")
        elif opcion == '0':
            return False
        else:
            print("Opción inválida")
            input("Presione enter para continuar")

# función principal del programa
def main():
    if not login_menu():
        return

    estudiantes = [[1, 'juan Netto', 'jnetto@uade.edu.ar', True], [2, 'fulano', 'fulano@uade.edu.ar', True]]
    materias = [[1, 'matematicas', True]]
    notas = []
    # lista donde se guardan los estudiantes
    # cada elemento será: [legajo, nombre, email]


    opcion = ""

    # menú que se repite hasta que el usuario elija salir
    while opcion != "0":
        

        limpiar_pantalla()

        print("1 - Menu estudiantes")
        print("2 - Menu materias")
        print("3 - Menu notas")
        print("4 - Estadisticas")
        print("0 - Salir")

        opcion = input('Opcion: ')

        if opcion == '1':

            menu_estudiantes(estudiantes)


        elif opcion == '2':

            menu_materias(materias)

        elif opcion == '3':

            menu_notas(notas)

        elif opcion == '4':

            print('opcion 4')
            input()
            #menu_estadisticas()
        
        elif opcion == '0':

            print('Saliendo...')

        else:

            print('opcion invalida')
            input()
            #menu estadisticas()

        




# ejecuta el programa
main()