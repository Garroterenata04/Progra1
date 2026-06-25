import os
import json

# Módulo de persistencia: centraliza la lectura y escritura de datos en JSON.
# Toda la lógica de I/O pasa por _guardar/_cargar para que los módulos CRUD
# nunca interactúen directamente con el sistema de archivos.

ESTUDIANTES_JSON = "estudiantes.json"
MATERIAS_JSON    = "materias.json"
NOTAS_JSON       = "notas.json"
USUARIOS_JSON    = "usuarios.json"

_USUARIOS_DEFAULT = [
    {'email': 'admin@uade.edu.ar', 'password': 'admin',   'rol': 'admin'},
    {'email': 'guido@guido.com',   'password': '123',     'rol': 'viewer'},
    {'email': 'uade@uade.com',     'password': '1234',    'rol': 'viewer'},
    {'email': '1@gmail.com',       'password': '123456',  'rol': 'viewer'},
    {'email': 'garrote@gmail.com', 'password': 'garrote', 'rol': 'viewer'},
]


# ---------------------------------------------------------------------------
# Helpers internos — toda la I/O pasa por aquí
# ---------------------------------------------------------------------------

def _guardar(archivo, datos):
    """Serializa una lista de diccionarios a un archivo JSON."""
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def _cargar(archivo):
    """Deserializa una lista de diccionarios desde un archivo JSON.
    Devuelve lista vacía si el archivo no existe."""
    if not os.path.exists(archivo):
        return []
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# API pública por entidad
# ---------------------------------------------------------------------------

def guardar_estudiantes(datos): _guardar(ESTUDIANTES_JSON, datos)
def cargar_estudiantes():       return _cargar(ESTUDIANTES_JSON)

def guardar_materias(datos): _guardar(MATERIAS_JSON, datos)
def cargar_materias():       return _cargar(MATERIAS_JSON)

def guardar_notas(datos): _guardar(NOTAS_JSON, datos)
def cargar_notas():       return _cargar(NOTAS_JSON)

def guardar_usuarios(datos): _guardar(USUARIOS_JSON, datos)


def cargar_usuarios():
    """Carga usuarios desde JSON. En la primera ejecución persiste los defaults."""
    datos = _cargar(USUARIOS_JSON)
    if not datos:
        guardar_usuarios(_USUARIOS_DEFAULT)
        return list(_USUARIOS_DEFAULT)
    return datos
