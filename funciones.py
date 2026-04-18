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
            print("Número inválido (no puede estar vacío)")
            continue
        try:
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
        if not re.match(r'^([0-9]|10)(\.[0-9]+)?$', entrada):
            print("Nota inválida (debe estar entre 0 y 10, ejemplo: 8 ó 8.5)")
            continue
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida (debe estar entre 0 y 10)")
        except ValueError:
            print("Debe ingresar un número válido")
