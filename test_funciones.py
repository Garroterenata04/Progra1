import unittest
from unittest.mock import patch

from funciones import validar_email, validar_no_vacio
from estudiantes import buscar_por_estudiante, buscar_estudiante_recursivo
from materias import buscar_por_materia
from notas import buscar_nota_recursiva
from estadisticas import calcular_promedio_recursivo


# ---------------------------------------------------------------------------
# 1. Tests de validar_email (funciones.py)
# ---------------------------------------------------------------------------

class TestValidarEmail(unittest.TestCase):

    def test_email_valido(self):
        self.assertTrue(validar_email("juan@gmail.com"))

    def test_email_valido_con_punto_en_usuario(self):
        self.assertTrue(validar_email("juan.perez@uade.edu.ar"))

    def test_email_sin_arroba(self):
        self.assertFalse(validar_email("juangmail.com"))

    def test_email_sin_dominio(self):
        self.assertFalse(validar_email("juan@"))

    def test_email_vacio(self):
        self.assertFalse(validar_email(""))

    def test_email_sin_extension(self):
        self.assertFalse(validar_email("juan@gmail"))


# ---------------------------------------------------------------------------
# 2. Tests de validar_no_vacio (funciones.py)
# ---------------------------------------------------------------------------

class TestValidarNoVacio(unittest.TestCase):

    def test_texto_con_contenido(self):
        self.assertTrue(validar_no_vacio("Algoritmos"))

    def test_cadena_vacia(self):
        self.assertFalse(validar_no_vacio(""))

    def test_solo_espacios(self):
        self.assertFalse(validar_no_vacio("   "))

    def test_texto_con_espacios_alrededor(self):
        # Tiene contenido real aunque tenga espacios a los costados
        self.assertTrue(validar_no_vacio("  hola  "))

    def test_texto_numerico(self):
        self.assertTrue(validar_no_vacio("123"))


# ---------------------------------------------------------------------------
# 3. Tests de buscar_por_estudiante (estudiantes.py)
# ---------------------------------------------------------------------------

class TestBuscarPorEstudiante(unittest.TestCase):

    def setUp(self):
        self.estudiantes = [
            {"legajo": 1, "nombre": "Ana García",   "mail": "ana@gmail.com",   "activo": True},
            {"legajo": 2, "nombre": "Luis Pérez",   "mail": "luis@gmail.com",  "activo": True},
            {"legajo": 3, "nombre": "María López",  "mail": "maria@gmail.com", "activo": False},
        ]

    def test_estudiante_existente_devuelve_indice_correcto(self):
        self.assertEqual(buscar_por_estudiante(self.estudiantes, 1), 0)
        self.assertEqual(buscar_por_estudiante(self.estudiantes, 2), 1)
        self.assertEqual(buscar_por_estudiante(self.estudiantes, 3), 2)

    def test_estudiante_inexistente_devuelve_menos_uno(self):
        self.assertEqual(buscar_por_estudiante(self.estudiantes, 99), -1)

    def test_lista_vacia_devuelve_menos_uno(self):
        self.assertEqual(buscar_por_estudiante([], 1), -1)

    def test_estudiante_inactivo_sigue_siendo_encontrado(self):
        # buscar_por_estudiante no filtra por activo, solo busca por legajo
        self.assertEqual(buscar_por_estudiante(self.estudiantes, 3), 2)


# ---------------------------------------------------------------------------
# 4. Tests de buscar_por_materia (materias.py)
# ---------------------------------------------------------------------------

class TestBuscarPorMateria(unittest.TestCase):

    def setUp(self):
        self.materias = [
            {"id": 10, "nombre": "Algoritmos 1",  "activo": True},
            {"id": 20, "nombre": "Bases de Datos", "activo": True},
            {"id": 30, "nombre": "Redes",          "activo": False},
        ]

    def test_materia_existente_devuelve_indice_correcto(self):
        self.assertEqual(buscar_por_materia(self.materias, 10), 0)
        self.assertEqual(buscar_por_materia(self.materias, 20), 1)
        self.assertEqual(buscar_por_materia(self.materias, 30), 2)

    def test_materia_inexistente_devuelve_menos_uno(self):
        self.assertEqual(buscar_por_materia(self.materias, 999), -1)

    def test_lista_vacia_devuelve_menos_uno(self):
        self.assertEqual(buscar_por_materia([], 10), -1)


# ---------------------------------------------------------------------------
# 5. Tests de lógica de notas: detección de duplicados
# ---------------------------------------------------------------------------
# La función agregar_nota usa filter + lambda para detectar si ya existe
# una nota para el mismo alumno, materia y tipo. Aquí se prueba esa lógica
# de forma aislada, sin depender de entrada del usuario.

class TestDeteccionNotaDuplicada(unittest.TestCase):

    def setUp(self):
        self.notas = [
            {"id": 1, "id_estudiante": 1, "id_materia": 10, "nota": 8.0, "descripcion": "Primer parcial"},
            {"id": 2, "id_estudiante": 1, "id_materia": 20, "nota": 7.5, "descripcion": "Final"},
            {"id": 3, "id_estudiante": 2, "id_materia": 10, "nota": 9.0, "descripcion": "Primer parcial"},
        ]

    def _nota_duplicada(self, alumno_id, materia_id, tipo):
        """Replica el filtro usado en agregar_nota."""
        return list(filter(
            lambda n: n["id_estudiante"] == alumno_id
                   and n["id_materia"] == materia_id
                   and n["descripcion"] == tipo,
            self.notas
        ))

    def test_nota_existente_es_detectada_como_duplicado(self):
        resultado = self._nota_duplicada(1, 10, "Primer parcial")
        self.assertTrue(len(resultado) > 0)

    def test_nota_nueva_no_es_duplicado(self):
        resultado = self._nota_duplicada(1, 10, "Final")
        self.assertEqual(len(resultado), 0)

    def test_mismo_alumno_distinta_materia_no_es_duplicado(self):
        resultado = self._nota_duplicada(1, 30, "Primer parcial")
        self.assertEqual(len(resultado), 0)

    def test_distinto_alumno_misma_materia_no_es_duplicado(self):
        resultado = self._nota_duplicada(99, 10, "Primer parcial")
        self.assertEqual(len(resultado), 0)


# ---------------------------------------------------------------------------
# 6. Tests de cálculo de promedio (lógica de estadisticas.py)
# ---------------------------------------------------------------------------
# Las funciones de estadísticas usan map + reduce para calcular promedios.
# Se prueba la misma lógica de forma directa sin llamar a las funciones
# que requieren input/print.

class TestCalculoPromedios(unittest.TestCase):

    def setUp(self):
        self.notas = [
            {"id": 1, "id_estudiante": 1, "id_materia": 10, "nota": 6.0,  "descripcion": "Primer parcial"},
            {"id": 2, "id_estudiante": 1, "id_materia": 10, "nota": 8.0,  "descripcion": "Segundo parcial"},
            {"id": 3, "id_estudiante": 2, "id_materia": 10, "nota": 10.0, "descripcion": "Final"},
            {"id": 4, "id_estudiante": 2, "id_materia": 20, "nota": 4.0,  "descripcion": "Primer parcial"},
        ]

    def _promedio_estudiante(self, legajo):
        notas_alumno = [n["nota"] for n in self.notas if n["id_estudiante"] == legajo]
        if not notas_alumno:
            return None
        return sum(notas_alumno) / len(notas_alumno)

    def _promedio_materia(self, materia_id):
        notas_materia = [n["nota"] for n in self.notas if n["id_materia"] == materia_id]
        if not notas_materia:
            return None
        return sum(notas_materia) / len(notas_materia)

    def test_promedio_estudiante_con_dos_notas(self):
        # Estudiante 1 tiene 6.0 y 8.0 → promedio 7.0
        self.assertAlmostEqual(self._promedio_estudiante(1), 7.0)

    def test_promedio_estudiante_con_una_nota(self):
        # Solo la nota 10.0 en materia 10 para estudiante 2 antes de filtrar
        notas = [n["nota"] for n in self.notas if n["id_estudiante"] == 2 and n["id_materia"] == 10]
        promedio = sum(notas) / len(notas)
        self.assertAlmostEqual(promedio, 10.0)

    def test_promedio_materia_con_varias_notas(self):
        # Materia 10 tiene notas 6.0, 8.0, 10.0 → promedio 8.0
        self.assertAlmostEqual(self._promedio_materia(10), 8.0)

    def test_promedio_materia_sin_notas_devuelve_none(self):
        self.assertIsNone(self._promedio_materia(999))

    def test_estudiante_sin_notas_devuelve_none(self):
        self.assertIsNone(self._promedio_estudiante(99))


# ---------------------------------------------------------------------------
# 7. Tests de buscar_nota_recursiva (notas.py)
# ---------------------------------------------------------------------------

class TestBuscarNotaRecursiva(unittest.TestCase):

    def setUp(self):
        self.notas = [
            {"id": 1, "id_estudiante": 1, "id_materia": 10, "nota": 8.0, "descripcion": "Primer parcial"},
            {"id": 2, "id_estudiante": 1, "id_materia": 20, "nota": 7.5, "descripcion": "Final"},
            {"id": 3, "id_estudiante": 2, "id_materia": 10, "nota": 9.0, "descripcion": "Segundo parcial"},
        ]

    def test_nota_al_inicio_devuelve_indice_cero(self):
        self.assertEqual(buscar_nota_recursiva(self.notas, 1), 0)

    def test_nota_al_final_devuelve_ultimo_indice(self):
        self.assertEqual(buscar_nota_recursiva(self.notas, 3), 2)

    def test_nota_en_el_medio_devuelve_indice_correcto(self):
        self.assertEqual(buscar_nota_recursiva(self.notas, 2), 1)

    def test_nota_inexistente_devuelve_menos_uno(self):
        self.assertEqual(buscar_nota_recursiva(self.notas, 99), -1)

    def test_lista_vacia_devuelve_menos_uno(self):
        self.assertEqual(buscar_nota_recursiva([], 1), -1)

    def test_indice_inicial_personalizado(self):
        # Buscar desde la mitad de la lista; no debe encontrar id=1 (está antes)
        self.assertEqual(buscar_nota_recursiva(self.notas, 1, indice=1), -1)


# ---------------------------------------------------------------------------
# 8. Tests de buscar_estudiante_recursivo (estudiantes.py)
# ---------------------------------------------------------------------------

class TestBuscarEstudianteRecursivo(unittest.TestCase):

    def setUp(self):
        self.estudiantes = [
            {"legajo": 10, "nombre": "Ana García",  "mail": "ana@mail.com",  "activo": True},
            {"legajo": 20, "nombre": "Luis Pérez",  "mail": "luis@mail.com", "activo": True},
            {"legajo": 30, "nombre": "María López", "mail": "maria@mail.com","activo": False},
        ]

    def test_estudiante_al_inicio(self):
        self.assertEqual(buscar_estudiante_recursivo(self.estudiantes, 10), 0)

    def test_estudiante_al_final(self):
        self.assertEqual(buscar_estudiante_recursivo(self.estudiantes, 30), 2)

    def test_estudiante_en_el_medio(self):
        self.assertEqual(buscar_estudiante_recursivo(self.estudiantes, 20), 1)

    def test_legajo_inexistente_devuelve_menos_uno(self):
        self.assertEqual(buscar_estudiante_recursivo(self.estudiantes, 99), -1)

    def test_lista_vacia_devuelve_menos_uno(self):
        self.assertEqual(buscar_estudiante_recursivo([], 10), -1)

    def test_indice_inicial_omite_elementos_anteriores(self):
        # Buscar desde indice=1: no debe encontrar legajo=10 (está en índice 0)
        self.assertEqual(buscar_estudiante_recursivo(self.estudiantes, 10, indice=1), -1)


# ---------------------------------------------------------------------------
# 9. Tests de calcular_promedio_recursivo (estadisticas.py)
# ---------------------------------------------------------------------------

class TestCalcularPromedioRecursivo(unittest.TestCase):

    def test_lista_con_valores_iguales(self):
        self.assertAlmostEqual(calcular_promedio_recursivo([5.0, 5.0, 5.0]), 5.0)

    def test_lista_con_valores_distintos(self):
        # (6 + 8 + 10) / 3 = 8.0
        self.assertAlmostEqual(calcular_promedio_recursivo([6.0, 8.0, 10.0]), 8.0)

    def test_lista_con_un_elemento(self):
        self.assertAlmostEqual(calcular_promedio_recursivo([7.5]), 7.5)

    def test_lista_vacia_devuelve_cero(self):
        self.assertAlmostEqual(calcular_promedio_recursivo([]), 0.0)

    def test_valores_con_decimales(self):
        # (7.5 + 8.5) / 2 = 8.0
        self.assertAlmostEqual(calcular_promedio_recursivo([7.5, 8.5]), 8.0)

    def test_nota_minima_y_maxima(self):
        # (0 + 10) / 2 = 5.0
        self.assertAlmostEqual(calcular_promedio_recursivo([0.0, 10.0]), 5.0)


if __name__ == "__main__":
    unittest.main()
