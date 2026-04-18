from funciones import limpiar_pantalla, validar_email
from estudiantes import cargar_estudiantes, menu_estudiantes
from materias import cargar_materias, menu_materias
from notas import cargar_notas, menu_notas
from estadisticas import mostrar_estadisticas


def cargar_usuarios():
    return [
        {'email': 'admin@uade.edu.ar', 'password': 'admin', 'rol': 'admin'},
        {'email': 'guido@guido.com', 'password': '123', 'rol': 'viewer'},
        {'email': 'uade@uade.com', 'password': '1234', 'rol': 'viewer'},
        {'email': '1@gmail.com', 'password': '123456', 'rol': 'viewer'},
        {'email': 'garrote@gmail.com', 'password': 'garrote', 'rol': 'viewer'}
    ]


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
            password = input('Contraseña: ')
            for user in users:
                if user['email'] == email and user['password'] == password:
                    print("Login exitoso")
                    input("Presione enter para continuar")
                    return user['rol']
            print("Email o contraseña incorrectos")
            input("Presione enter para continuar")
        elif opcion == '2':
            email = input('Email: ')
            if not validar_email(email):
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
    # lista donde se guardan los estudiantes
    # cada elemento será: {legajo, nombre, mail, estado}


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