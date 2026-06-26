import getpass
from funciones import limpiar_pantalla, validar_email, validar_no_vacio
from matrices import cargar_estudiantes, cargar_materias, cargar_notas, cargar_usuarios, guardar_usuarios
from estudiantes import menu_estudiantes
from materias import menu_materias
from notas import menu_notas
from estadisticas import mostrar_estadisticas

# Punto de entrada del sistema: login y menú principal.

titulo = r"""

   ____           _   _   __
  / ___| ___  ___| |_(_) /_/  _ __
 | |  _ / _ \/ __| __| |/ _ \| '_ \
 | |_| |  __/\__ \ |_| | (_) | | | |
  \____|\___||___/\__|_|\___/|_| |_|    _
    / \   ___ __ _  __| | ___ _ __ ___ (_) ___ __ _
   / _ \ / __/ _` |/ _` |/ _ \ '_ ` _ \| |/ __/ _` |
  / ___ \ (_| (_| | (_| |  __/ | | | | | | (_| (_| |
 /_/   \_\___\__,_|\__,_|\___|_| |_| |_|_|\___\__,_|

        """



def login_menu():
    """Pantalla de login y registro. Devuelve el rol ('admin' o 'viewer') si el
    login fue exitoso, o None si el usuario elige salir.
    Usa getpass para pedir la contraseña sin mostrarla en pantalla."""
    users = cargar_usuarios()
    while True:
        limpiar_pantalla()
        print(titulo)
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
            # Se busca un usuario cuyo email y password coincidan exactamente.
            for user in users:
                if user['email'] == email and user['password'] == password:
                    print("[✓] Login exitoso")
                    input("Presione enter para continuar...")
                    return user['rol']
            print(" [x] Email o contraseña incorrectos")
            input("Presione enter para continuar...")
        elif opcion == '2':
            email = input('Email: ')
            while not validar_no_vacio(email):
                print(" [x] Email no puede estar vacío")
                email = input('Email: ')

            if not validar_email(email):
                print("Email inválido")
                input("Presione enter para continuar...")
                continue
            if any(u['email'] == email for u in users):
                print("Email ya registrado")
                input("Presione enter para continuar...")
                continue
            password = getpass.getpass('Contraseña: ')
            while not validar_no_vacio(password):
                print(" [x] Contraseña no puede estar vacía")
                password = getpass.getpass('Contraseña: ')

            confirm = getpass.getpass('Confirmar contraseña: ')
            while not validar_no_vacio(confirm):
                print("Confirmar contraseña no puede estar vacío")
                confirm = getpass.getpass('Confirmar contraseña: ')
            if password != confirm:
                print(" [x] Contraseñas no coinciden")
                input("Presione enter para continuar...")
                continue
            print()
            print("Rol del usuario:")
            print("1 - Admin")
            print("2 - Viewer")
            opcion_rol = input("Opción: ")
            if opcion_rol == '1':
                rol_nuevo = 'admin'
            elif opcion_rol == '2':
                rol_nuevo = 'viewer'
            else:
                print(" [x] Opción inválida")
                input("Presione enter para continuar...")
                continue

            users.append({'email': email, 'password': password, 'rol': rol_nuevo})
            try:
                guardar_usuarios(users)
                print(f" [✓] Usuario creado exitosamente (rol: {rol_nuevo})")
            except OSError as e:
                users.pop()
                print(f" [x] Error al guardar el usuario: {e}")
            input("Presione enter para continuar...")
        elif opcion == '0':
            return None
        else:
            print(" [x] Opción inválida")
            input("Presione enter para continuar...")

def main():
    """Punto de entrada del sistema. Carga los datos, autentica al usuario
    y lanza el menú principal según el rol obtenido en el login."""
    estudiantes = cargar_estudiantes()
    materias = cargar_materias()
    notas = cargar_notas()

    rol = login_menu()
    if rol is None:
        return

    opcion = ""

    # menú que se repite hasta que el usuario elija salir
    # estudiantes, materias y notas son listas (mutables): se pasan por
    # referencia a cada submenú, así los cambios se reflejan en todos lados
    # sin necesidad de devolver y reasignar nada.
    while opcion != "0":


        limpiar_pantalla()
        print("=== MENU PRINCIPAL ===")
        print()
        print(titulo)
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

            mostrar_estadisticas()

        elif opcion == '0':

            print('Saliendo...')

        else:

            print('[x] opcion invalida')
            input()


if __name__ == '__main__':
    main()
