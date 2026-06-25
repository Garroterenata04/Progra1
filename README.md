# Sistema de Gestión Académica

Sistema de gestión universitaria por consola desarrollado en Python.  
Trabajo Práctico Obligatorio — Programación 1 / Algoritmos y Estructuras de Datos 1  
UADE · Primer cuatrimestre 2026

---

## Estrategia de ramas

- `main` — versión estable del proyecto
- `guido` — desarrollo individual de Guido
- `renata` — desarrollo individual de Renata
- `teo` — desarrollo individual de Teo
- `juani` — desarrollo individual de Juani

Cada integrante trabajó en su rama propia y mergeó directamente a `main`.

---

## Cómo ejecutar

```bash
python main.py
```

**Requisitos:** Python 3.8 o superior. No requiere librerías externas.

---

## Credenciales de acceso

| Email | Contraseña | Rol |
|---|---|---|
| admin@uade.edu.ar | admin | admin |
| uade@uade.com | 1234 | viewer |

También se pueden crear nuevos usuarios desde la pantalla de login (siempre con rol viewer).

---

## Roles

| Rol | Permisos |
|---|---|
| **admin** | Alta, modificación, baja y listado de estudiantes, materias y notas |
| **viewer** | Solo consulta (listados) |

---

## Estructura del proyecto

```
Progra1/
├── main.py            # Punto de entrada: login y menú principal
├── estudiantes.py     # CRUD de estudiantes
├── materias.py        # CRUD de materias
├── notas.py           # CRUD de notas
├── estadisticas.py    # Reportes y estadísticas
├── funciones.py       # Validaciones y utilidades (regex, email, notas)
├── matrices.py        # Capa de persistencia (JSON y texto plano)
├── test_funciones.py  # Pruebas unitarias (45 tests)
├── estudiantes.json   # Datos de estudiantes
├── materias.json      # Datos de materias
├── notas.json         # Datos de notas
└── usuarios.txt       # Usuarios del sistema (texto plano)
```

---

## Funcionalidades

### Estudiantes
- Alta con legajo autogenerado, nombre y mail validado
- Modificación de nombre y mail
- Baja lógica (el registro se conserva, `activo = False`)
- Reactivación de estudiantes dados de baja
- Listado completo y listado de inactivos

### Materias
- Alta con ID autogenerado
- Modificación de nombre
- Baja lógica
- Listado completo

### Notas
- Alta vinculada a un estudiante y materia activos
- Tipos: Primer parcial, Segundo parcial, Final
- Validación de duplicados (mismo alumno + materia + tipo)
- Modificación del valor numérico
- Eliminación definitiva
- Listado con nombre de alumno y materia resueltos

### Estadísticas
- Totales de estudiantes, materias y notas
- Porcentaje de alumnos activos sobre el total
- Distribución de notas por tipo de evaluación
- Alumnos activos con/sin notas (operaciones de conjuntos)
- Promedio general del sistema
- Promedio por estudiante y por materia
- Identificación del mejor y peor estudiante

---

## Persistencia

| Entidad | Archivo | Formato |
|---|---|---|
| Estudiantes | `estudiantes.json` | JSON |
| Materias | `materias.json` | JSON |
| Notas | `notas.json` | JSON |
| Usuarios | `usuarios.txt` | Texto plano (`email;password;rol`) |

---

## Pruebas unitarias

```bash
python -m unittest test_funciones -v
```

45 tests organizados en 9 clases que cubren:

| Clase | Qué verifica |
|---|---|
| `TestValidarEmail` | Formatos válidos e inválidos de email |
| `TestValidarNoVacio` | Cadenas vacías, con espacios y con contenido |
| `TestBuscarPorEstudiante` | Búsqueda iterativa de estudiantes por legajo |
| `TestBuscarPorMateria` | Búsqueda iterativa de materias por ID |
| `TestBuscarEstudianteRecursivo` | Búsqueda recursiva de estudiantes |
| `TestBuscarNotaRecursiva` | Búsqueda recursiva de notas |
| `TestCalcularPromedioRecursivo` | Cálculo recursivo de promedio |
| `TestDeteccionNotaDuplicada` | Lógica de filtro para notas duplicadas |
| `TestCalculoPromedios` | Cálculo de promedios por estudiante y materia |

---

## Conceptos aplicados

| Concepto | Dónde |
|---|---|
| **Recursividad (×3)** | `buscar_nota_recursiva` · `buscar_estudiante_recursivo` · `calcular_promedio_recursivo` |
| **Lambda + map + filter + reduce** | `estadisticas.py` — promedios y distribución por tipo |
| **Conjuntos (sets)** | `estadisticas_generales` — intersección y diferencia de legajos |
| **Tuplas** | `estadisticas_generales` (resumen de totales) · `promedio_general_materias` (nombre, valor) |
| **Expresiones regulares (×3)** | `funciones.py` — email, campo vacío, formato de nota |
| **Manejo de excepciones** | `try/except OSError` en guardado · `try/except ValueError` en validaciones |
| **Archivos JSON** | Estudiantes, materias y notas |
| **Archivos de texto plano** | Usuarios del login (`usuarios.txt`) |
| **Control de acceso por roles** | Admin y viewer en todos los submenús |
| **Docstrings** | Todas las funciones del sistema |
