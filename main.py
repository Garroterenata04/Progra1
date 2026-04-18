import getpass
from funciones import limpiar_pantalla, validar_email, validar_no_vacio
from matrices import cargar_estudiantes, cargar_materias, cargar_notas, cargar_usuarios
from estudiantes import menu_estudiantes
from materias import menu_materias
from notas import menu_notas
from estadisticas import mostrar_estadisticas


def login_menu():
    users = cargar_usuarios()
    while True:
        limpiar_pantalla()
        print("=== SISTEMA DE GESTIÓN ACADÉMICA ===")
        print()
        print("1 - Iniciar sesión")
        print("2 - Crear usuario")
        print("0 - Salir")
        opcion = input('Opción: ')
        if opcion == '1':
            email = input('Email: ')
            while not validar_no_vacio(email):
                print("Email no puede estar vacío")
                email = input('Email: ')
            
            password = getpass.getpass('Contraseña: ')
            while not validar_no_vacio(password):
                print("Contraseña no puede estar vacía")
                password = getpass.getpass('Contraseña: ')
            for user in users:
                if user['email'] == email and user['password'] == password:
                    print("Login exitoso")
                    input("Presione enter para continuar")
                    return user['rol']
            print("Email o contraseña incorrectos")
            input("Presione enter para continuar")
        elif opcion == '2':
            email = input('Email: ')
            while not validar_no_vacio(email):
                print("Email no puede estar vacío")
                email = input('Email: ')
            
            if not validar_email(email):
                print("Email inválido")
                input("Presione enter para continuar")
                continue
            if any(u['email'] == email for u in users):
                print("Email ya registrado")
                input("Presione enter para continuar")
                continue
            password = getpass.getpass('Contraseña: ')
            while not validar_no_vacio(password):
                print("Contraseña no puede estar vacía")
                password = getpass.getpass('Contraseña: ')
            
            confirm = getpass.getpass('Confirmar contraseña: ')
            while not validar_no_vacio(confirm):
                print("Confirmar contraseña no puede estar vacío")
                confirm = getpass.getpass('Confirmar contraseña: ')
            if password != confirm:
                print("Contraseñas no coinciden")
                input("Presione enter para continuar")
                continue
            users.append({'email': email, 'password': password, 'rol': 'viewer'})
            print("Usuario creado exitosamente")
            input("Presione enter para continuar")
        elif opcion == '0':
            return None
        else:
            print("Opción inválida")
            input("Presione enter para continuar")

# función principal del programa
def main():
    rol = login_menu()
    if rol is None:
        return

    estudiantes = cargar_estudiantes()
    materias = cargar_materias()
    notas = cargar_notas()


    opcion = ""

    # menú que se repite hasta que el usuario elija salir
    while opcion != "0":
        

        limpiar_pantalla()
        print("=== MENU PRINCIPAL ===")
        print()

        print("1 - Menu estudiantes")
        print("2 - Menu materias")
        print("3 - Menu notas")
        print("4 - Estadisticas")
        print("0 - Salir")

        opcion = input('Opcion: ')

        if opcion == '1':

            menu_estudiantes(estudiantes, rol)


        elif opcion == '2':

            menu_materias(materias, rol)

        elif opcion == '3':

            menu_notas(notas, estudiantes, materias, rol)

        elif opcion == '4':

            mostrar_estadisticas(estudiantes, materias, notas)
        
        elif opcion == '0':

            print('Saliendo...')

        else:

            print('opcion invalida')
            input()


if __name__ == '__main__':
    main()