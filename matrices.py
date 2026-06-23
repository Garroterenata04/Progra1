#========================================
# MÓDULO DE MATRICES - BASE DE DATOS
#========================================
# Centraliza todas las matrices (listas de diccionarios) del sistema.
# La persistencia se hace en archivos de texto plano, un archivo por entidad,
# con los campos de cada diccionario separados por ';'.
#
# estudiantes.txt -> legajo;nombre;mail;activo
# materias.txt    -> id;nombre;activo
# notas.txt       -> id;id_estudiante;id_materia;nota;descripcion

ESTUDIANTES_FILE = "estudiantes.txt"
MATERIAS_FILE = "materias.txt"
NOTAS_FILE = "notas.txt"


#========================================
# MATRIZ: ESTUDIANTES
#========================================
def guardar_estudiantes(estudiantes):
    """Escribe la lista de estudiantes en estudiantes.txt"""
    with open(ESTUDIANTES_FILE, 'w', encoding='utf-8') as archivo:
        for e in estudiantes:
            archivo.write(f"{e['legajo']};{e['nombre']};{e['mail']};{e['activo']}\n")


def cargar_estudiantes():
    """Matriz de estudiantes - módulo estudiantes.py"""
    return [
        {'legajo': 1, 'nombre': 'Juan Pérez', 'mail': 'juan@mail.com', 'activo': True},
        {'legajo': 2, 'nombre': 'María Gómez', 'mail': 'maria@mail.com', 'activo': True},
        {'legajo': 3, 'nombre': 'Lucía Fernández', 'mail': 'lucia@mail.com', 'activo': False},
    ]


#========================================
# MATRIZ: MATERIAS
#========================================
def guardar_materias(materias):
    """Escribe la lista de materias en materias.txt"""
    with open(MATERIAS_FILE, 'w', encoding='utf-8') as archivo:
        for m in materias:
            archivo.write(f"{m['id']};{m['nombre']};{m['activo']}\n")


def cargar_materias():
    """Matriz de materias - módulo materias.py"""
    return [
        {"id": 1, "nombre": "Matematicas", "activo": True},
        {"id": 2, "nombre": "Fisica", "activo": True},
        {"id": 3, "nombre": "Quimica", "activo": True},
        {"id": 4, "nombre": "Programacion", "activo": True},
        {"id": 5, "nombre": "Ingles", "activo": True}
    ]


#========================================
# MATRIZ: NOTAS
#========================================
def guardar_notas(notas):
    """Escribe la lista de notas en notas.txt"""
    with open(NOTAS_FILE, 'w', encoding='utf-8') as archivo:
        for n in notas:
            archivo.write(f"{n['id']};{n['id_estudiante']};{n['id_materia']};{n['nota']};{n['descripcion']}\n")


def cargar_notas():
    """Matriz de notas - módulo notas.py"""
    return [
        {"id": 1, "id_estudiante": 1, "id_materia": 1, "nota": 8, "descripcion": "Primer parcial"},
        {"id": 2, "id_estudiante": 1, "id_materia": 2, "nota": 9, "descripcion": "Segundo parcial"},
        {"id": 3, "id_estudiante": 2, "id_materia": 1, "nota": 7, "descripcion": "Primer parcial"},
        {"id": 4, "id_estudiante": 2, "id_materia": 3, "nota": 10, "descripcion": "Final"},
        {"id": 5, "id_estudiante": 3, "id_materia": 4, "nota": 6, "descripcion": "Primer parcial"}
    ]


#========================================
# MATRIZ: USUARIOS
#========================================
def cargar_usuarios():
    """Matriz de usuarios - módulo main.py"""
    return [
        {'email': 'admin@uade.edu.ar', 'password': 'admin', 'rol': 'admin'},
        {'email': 'guido@guido.com', 'password': '123', 'rol': 'viewer'},
        {'email': 'uade@uade.com', 'password': '1234', 'rol': 'viewer'},
        {'email': '1@gmail.com', 'password': '123456', 'rol': 'viewer'},
        {'email': 'garrote@gmail.com', 'password': 'garrote', 'rol': 'viewer'}
    ]
