import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')      # Windows
    else:
        os.system('clear')    # Mac / Linux
