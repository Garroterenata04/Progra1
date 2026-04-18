import os
import re

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')      # Windows
    else:
        os.system('clear')    # Mac / Linux


def validar_email(email):
    """Valida que el texto sea un email con formato correcto"""
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None


def validar_no_vacio(texto):
    """Valida que el texto no esté vacío ni contenga solo espacios"""
    return re.match(r'^.+$', texto.strip()) is not None


def validar_numero(prompt):
    """Solicita un número al usuario y valida que sea un número entero válido"""
    while True:
        entrada = input(prompt)
        if not validar_no_vacio(entrada):
            print("Entrada no puede estar vacía")
            continue
        try:
            return int(entrada)
        except ValueError:
            print("Debe ingresar un número válido")
