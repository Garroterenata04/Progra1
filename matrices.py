import os

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
    """Lee la lista de estudiantes desde estudiantes.txt"""
    if not os.path.exists(ESTUDIANTES_FILE):
        return []

    estudiantes = []
    with open(ESTUDIANTES_FILE, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            legajo, nombre, mail, activo = linea.strip().split(';')
            estudiantes.append({
                'legajo': int(legajo),
                'nombre': nombre,
                'mail': mail,
                'activo': activo == 'True'
            })
    return estudiantes


#========================================
# MATRIZ: MATERIAS
#========================================
def guardar_materias(materias):
    """Escribe la lista de materias en materias.txt"""
    with open(MATERIAS_FILE, 'w', encoding='utf-8') as archivo:
        for m in materias:
            archivo.write(f"{m['id']};{m['nombre']};{m['activo']}\n")


def cargar_materias():
    """Lee la lista de materias desde materias.txt"""
    if not os.path.exists(MATERIAS_FILE):
        return []

    materias = []
    with open(MATERIAS_FILE, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            id_materia, nombre, activo = linea.strip().split(';')
            materias.append({
                'id': int(id_materia),
                'nombre': nombre,
                'activo': activo == 'True'
            })
    return materias


#========================================
# MATRIZ: NOTAS
#========================================
def guardar_notas(notas):
    """Escribe la lista de notas en notas.txt"""
    with open(NOTAS_FILE, 'w', encoding='utf-8') as archivo:
        for n in notas:
            archivo.write(f"{n['id']};{n['id_estudiante']};{n['id_materia']};{n['nota']};{n['descripcion']}\n")


def cargar_notas():
    """Lee la lista de notas desde notas.txt"""
    if not os.path.exists(NOTAS_FILE):
        return []

    notas = []
    with open(NOTAS_FILE, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            id_nota, id_estudiante, id_materia, nota, descripcion = linea.strip().split(';')
            notas.append({
                'id': int(id_nota),
                'id_estudiante': int(id_estudiante),
                'id_materia': int(id_materia),
                'nota': float(nota),
                'descripcion': descripcion
            })
    return notas


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
