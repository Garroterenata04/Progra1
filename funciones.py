import os
import re

# Módulo de funciones auxiliares reutilizadas por todo el sistema:
# limpiar pantalla y validar las distintas entradas del usuario.


def limpiar_pantalla():
    # os.name es 'nt' en Windows y 'posix' en Mac/Linux, por eso el comando
    # de limpiar consola cambia según el sistema operativo.
    if os.name == 'nt':
        os.system('cls')      # Windows
    else:
        os.system('clear')    # Mac / Linux


def validar_email(email):
    """Valida que el texto sea un email con formato correcto"""
    # Expresión regular: usuario@dominio.extension
    # [a-zA-Z0-9_.+-]+  -> parte antes del @ (letras, números, . _ + -)
    # @[a-zA-Z0-9-]+    -> dominio (sin espacios)
    # \.[a-zA-Z0-9-.]+$ -> al menos una extensión después de un punto
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None


def validar_no_vacio(texto):
    """Valida que el texto no esté vacío ni contenga solo espacios"""
    # texto.strip() sacar los espacios de los costados; luego se chequea
    # que quede al menos un caracter (^.+$).
    return re.match(r'^.+$', texto.strip()) is not None


def validar_numero(prompt):
    """Solicita un número al usuario y valida que sea un número entero válido"""
    while True:
        entrada = input(prompt)
        if not validar_no_vacio(entrada):
            print("Número inválido (no puede estar vacío)")
            continue
        try:
            # int() puede tirar ValueError si el texto no es un entero
            # (ej: "abc" o "3.5"), por eso se usa try/except.
            return int(entrada)
        except ValueError:
            print("Debe ingresar un número válido")


def validar_nota(prompt):
    """Valida que la nota sea un número entre 0 y 10, puede tener decimales"""
    while True:
        entrada = input(prompt)
        if not validar_no_vacio(entrada):
            print("Nota inválida (no puede estar vacía)")
            continue

        # Validar formato con expresión regular: acepta números 0-10 con decimales opcionales
        # ([0-9]|10) -> un dígito (0 a 9) o el número 10 completo
        # (\.[0-9]+)? -> parte decimal opcional, ej: ".5"
        if not re.match(r'^([0-9]|10)(\.[0-9]+)?$', entrada):
            print("Nota inválida (debe estar entre 0 y 10, ejemplo: 8 ó 8.5)")
            continue

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                # Caso límite: el regex deja pasar números como "10.5" porque
                # coinciden con "10" + ".5"; este chequeo extra los descarta.
                print("Nota inválida (debe estar entre 0 y 10)")
        except ValueError:
            print("Debe ingresar un número válido")
