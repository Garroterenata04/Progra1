import os
import json

#========================================
# MÓDULO DE MATRICES - BASE DE DATOS
#========================================
# Centraliza todas las matrices (listas de diccionarios) del sistema.
# La persistencia se hace en archivos de texto plano, un archivo por entidad,
# con los campos de cada diccionario separados por ';'. Además, cada entidad
# se guarda en paralelo en un archivo .json (mismos datos, formato JSON),
# que se usa para cargar si está disponible.
#
# estudiantes.txt -> legajo;nombre;mail;activo
# materias.txt    -> id;nombre;activo
# notas.txt       -> id;id_estudiante;id_materia;nota;descripcion

ESTUDIANTES_FILE = "estudiantes.txt"
MATERIAS_FILE = "materias.txt"
NOTAS_FILE = "notas.txt"

ESTUDIANTES_JSON_FILE = "estudiantes.json"
MATERIAS_JSON_FILE = "materias.json"
NOTAS_JSON_FILE = "notas.json"


def guardar_json(nombre_archivo, datos):
    """Escribe una lista de diccionarios en un archivo JSON"""
    # json.dump serializa la lista de diccionarios directamente al archivo.
    # indent=2 -> lo deja prolijo (con sangría) para poder leerlo a simple vista.
    # ensure_ascii=False -> permite guardar tildes/ñ como caracteres normales
    # en vez de escaparlos (ej: "Pérez" en vez de "Pérez").
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)


def cargar_json(nombre_archivo):
    """Lee una lista de diccionarios desde un archivo JSON, o None si no existe"""
    if not os.path.exists(nombre_archivo):
        return None

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        # json.load reconstruye directamente la lista de diccionarios,
        # respetando los tipos originales (int, float, bool, str).
        return json.load(archivo)


#========================================
# MATRIZ: ESTUDIANTES
#========================================
def guardar_estudiantes(estudiantes):
    """Escribe la lista de estudiantes en estudiantes.txt y estudiantes.json"""
    with open(ESTUDIANTES_FILE, 'w', encoding='utf-8') as archivo:
        for e in estudiantes:
            # Una línea de texto por estudiante, campos separados por ';'.
            archivo.write(f"{e['legajo']};{e['nombre']};{e['mail']};{e['activo']}\n")
    # Se guarda también en JSON para tener ambos formatos sincronizados.
    guardar_json(ESTUDIANTES_JSON_FILE, estudiantes)


def cargar_estudiantes():
    """Lee la lista de estudiantes desde estudiantes.json si existe, sino desde estudiantes.txt"""
    # El JSON tiene prioridad porque conserva los tipos de datos tal cual
    # (bool, int) sin tener que parsearlos a mano como en el .txt.
    desde_json = cargar_json(ESTUDIANTES_JSON_FILE)
    if desde_json is not None:
        return desde_json

    if not os.path.exists(ESTUDIANTES_FILE):
        return []

    estudiantes = []
    with open(ESTUDIANTES_FILE, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # strip() sacar el salto de línea final; split(';') separa los campos.
            legajo, nombre, mail, activo = linea.strip().split(';')
            estudiantes.append({
                'legajo': int(legajo),          # en el txt todo es texto, hay que convertir a int
                'nombre': nombre,
                'mail': mail,
                'activo': activo == 'True'      # el texto "True"/"False" se convierte a bool
            })
    return estudiantes


#========================================
# MATRIZ: MATERIAS
#========================================
def guardar_materias(materias):
    """Escribe la lista de materias en materias.txt y materias.json"""
    with open(MATERIAS_FILE, 'w', encoding='utf-8') as archivo:
        for m in materias:
            archivo.write(f"{m['id']};{m['nombre']};{m['activo']}\n")
    guardar_json(MATERIAS_JSON_FILE, materias)


def cargar_materias():
    """Lee la lista de materias desde materias.json si existe, sino desde materias.txt"""
    desde_json = cargar_json(MATERIAS_JSON_FILE)
    if desde_json is not None:
        return desde_json

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
    """Escribe la lista de notas en notas.txt y notas.json"""
    with open(NOTAS_FILE, 'w', encoding='utf-8') as archivo:
        for n in notas:
            archivo.write(f"{n['id']};{n['id_estudiante']};{n['id_materia']};{n['nota']};{n['descripcion']}\n")
    guardar_json(NOTAS_JSON_FILE, notas)


def cargar_notas():
    """Lee la lista de notas desde notas.json si existe, sino desde notas.txt"""
    desde_json = cargar_json(NOTAS_JSON_FILE)
    if desde_json is not None:
        return desde_json

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
                'nota': float(nota),            # la nota puede tener decimales (ej: 8.5)
                'descripcion': descripcion
            })
    return notas


#========================================
# MATRIZ: USUARIOS
#========================================
def cargar_usuarios():
    """Matriz de usuarios - módulo main.py"""
    # Los usuarios (login) no persisten en archivo: viven solo en memoria
    # durante la ejecución, por eso siempre se devuelve esta lista fija.
    return [
        {'email': 'admin@uade.edu.ar', 'password': 'admin', 'rol': 'admin'},
        {'email': 'guido@guido.com', 'password': '123', 'rol': 'viewer'},
        {'email': 'uade@uade.com', 'password': '1234', 'rol': 'viewer'},
        {'email': '1@gmail.com', 'password': '123456', 'rol': 'viewer'},
        {'email': 'garrote@gmail.com', 'password': 'garrote', 'rol': 'viewer'}
    ]
