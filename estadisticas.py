from funciones import limpiar_pantalla, validar_numero
from functools import reduce
from matrices import cargar_estudiantes, cargar_materias, cargar_notas

# Módulo de reportes/estadísticas sobre estudiantes, materias y notas.
# Usa programación funcional (map, filter, reduce, lambdas) en vez de
# bucles for tradicionales para calcular promedios.


#------- PROMEDIO RECURSIVO -------

def calcular_promedio_recursivo(valores, indice=0, acumulado=0.0):
    """Calcula el promedio de una lista de números de forma recursiva.
    Caso base: se procesaron todos los elementos → devuelve el promedio.
    Caso recursivo: suma el elemento actual y avanza al siguiente."""
    if not valores:
        return 0.0
    # Caso base: se procesaron todos los valores
    if indice >= len(valores):
        return acumulado / len(valores)
    # Caso recursivo: acumular el valor actual y avanzar
    return calcular_promedio_recursivo(valores, indice + 1, acumulado + valores[indice])


#------- ESTADISTICAS GENERALES -------

def estadisticas_generales(estudiantes, materias, notas):
    """Muestra un resumen estadístico general: totales, porcentajes,
    distribución por tipo de evaluación y cruce por conjuntos."""
    limpiar_pantalla()
    print("=== ESTADISTICAS GENERALES ===")
    print()

    estudiantes_activos = [e for e in estudiantes if e["activo"]]
    materias_activas    = [m for m in materias if m["activo"]]

    # Tupla inmutable con los totales del sistema para acceder por índice:
    # resumen[0] = total estudiantes, [1] = activos, [2] = materias activas, [3] = total notas
    resumen = (len(estudiantes), len(estudiantes_activos), len(materias_activas), len(notas))

    print(f"  Estudiantes totales  : {resumen[0]}  (activos: {resumen[1]})")
    print(f"  Materias activas     : {resumen[2]}")
    print(f"  Notas registradas    : {resumen[3]}")

    if resumen[0] > 0:
        pct_activos = resumen[1] / resumen[0] * 100
        print(f"  Alumnos activos      : {pct_activos:.1f}% del total")

    if resumen[3] > 0:
        calificaciones   = list(map(lambda n: n["nota"], notas))
        promedio_general = calcular_promedio_recursivo(calificaciones)
        print(f"\n  Promedio general     : {promedio_general:.2f}")

        print("\n  Distribucion por tipo de evaluacion:")
        for tipo in ["Primer parcial", "Segundo parcial", "Final"]:
            cantidad = len(list(filter(lambda n: n["descripcion"] == tipo, notas)))
            pct_tipo = cantidad / resumen[3] * 100
            print(f"    {tipo:<18}: {cantidad} ({pct_tipo:.1f}%)")

    # Conjuntos: cruzar alumnos activos con los que tienen al menos una nota
    legajos_activos   = {e['legajo'] for e in estudiantes if e['activo']}
    legajos_con_notas = {n['id_estudiante'] for n in notas}
    activos_con_notas = legajos_activos & legajos_con_notas  # intersección
    activos_sin_notas = legajos_activos - legajos_con_notas  # diferencia

    print(f"\n  Con notas cargadas   : {len(activos_con_notas)} alumnos")
    print(f"  Sin notas todavía    : {len(activos_sin_notas)} alumnos")

    input("\nPresione enter para continuar...")


#------- PROMEDIO GENERAL DE ESTUDIANTES -------

def promedio_general_estudiantes(estudiantes, notas):
    """Muestra el promedio de todas las notas de cada estudiante activo."""
    limpiar_pantalla()
    print("=== PROMEDIO GENERAL DE ESTUDIANTES ===")
    print()

    if len(notas) == 0:
        print("[x] No hay notas registradas")
    else:
        for estudiante in estudiantes:
            if estudiante["activo"]:
                notas_filtradas = [n for n in notas if n["id_estudiante"] == estudiante["legajo"]]
                notas_alumno = list(map(lambda n: n["nota"], notas_filtradas))
                if notas_alumno:
                    # Promedio calculado de forma recursiva
                    promedio = calcular_promedio_recursivo(notas_alumno)
                    print(f"{estudiante['nombre']} (Legajo {estudiante['legajo']}): {promedio:.2f}")
                else:
                    print(f"{estudiante['nombre']} (Legajo {estudiante['legajo']}): Sin notas")

    input("Presione enter para continuar...")


#------- PROMEDIO POR MATERIA (ESTUDIANTE ESPECIFICO) -------

def promedio_estudiante_materias(estudiantes, materias, notas):
    """Pide un legajo y muestra el promedio del estudiante en cada materia."""
    limpiar_pantalla()
    legajo = validar_numero("Ingrese el legajo del estudiante: ")

    estudiante = None
    for e in estudiantes:
        if e["legajo"] == legajo:
            estudiante = e
            break

    if estudiante is None:
        print("[x] Estudiante no encontrado")
        input()
        return

    limpiar_pantalla()
    print(f"=== PROMEDIOS DE {estudiante['nombre'].upper()} ===")
    print()

    notas_alumno = [n for n in notas if n["id_estudiante"] == legajo]

    if not notas_alumno:
        print("[x] No hay notas para este estudiante")
    else:
        for materia in materias:
            if materia["activo"]:
                notas_filtradas = [n for n in notas_alumno if n["id_materia"] == materia["id"]]
                notas_materia = list(map(lambda n: n["nota"], notas_filtradas))
                if notas_materia:
                    promedio = sum(notas_materia) / len(notas_materia)
                    print(f"{materia['nombre']}: {promedio:.2f}")

        calificaciones_total = list(map(lambda n: n["nota"], notas_alumno))
        promedio_total = calcular_promedio_recursivo(calificaciones_total)
        print(f"\nPromedio total: {promedio_total:.2f}")

    input("Presione enter para continuar...")


#------- PROMEDIO DE MATERIA -------

def promedio_materia(materias, notas):
    """Pide un ID de materia y muestra el promedio general de sus notas."""
    limpiar_pantalla()
    print("[✓] Materias disponibles:")
    print()

    for m in materias:
        if m["activo"]:
            print(f"{m['id']} - {m['nombre']}")

    print()
    materia_id = validar_numero("Ingrese el ID de la materia: ")

    materia = None
    for m in materias:
        if m["id"] == materia_id:
            materia = m
            break

    if materia is None:
        print("[x] Materia no encontrada")
        input()
        return

    limpiar_pantalla()
    notas_materia = [n for n in notas if n["id_materia"] == materia_id]

    print(f"=== {materia['nombre'].upper()} ===")
    print()

    if not notas_materia:
        print(f" [x] No hay notas para {materia['nombre']}")
    else:
        calificaciones = list(map(lambda n: n["nota"], notas_materia))
        total_notas = reduce(lambda acc, nota: acc + nota, calificaciones, 0)
        promedio = total_notas / len(calificaciones)
        print(f"Promedio general: {promedio:.2f}")
        print(f"Total notas: {len(notas_materia)}")

    input("Presione enter para continuar...")


#------- PROMEDIO GENERAL DE MATERIAS -------

def promedio_general_materias(materias, notas):
    """Muestra la materia con mejor y peor promedio general."""
    limpiar_pantalla()
    print("=== PROMEDIO GENERAL DE MATERIAS ===")
    print()

    materias_activas = [m for m in materias if m["activo"]]

    if not materias_activas or not notas:
        print("No hay datos suficientes para calcular promedios")
        input("Presione enter para continuar...")
        return

    # Cada valor del dict es una tupla (nombre, promedio) — datos inmutables por materia
    promedios = {}
    for materia in materias_activas:
        notas_materia = [n["nota"] for n in notas if n["id_materia"] == materia["id"]]
        if notas_materia:
            promedios[materia["id"]] = (materia["nombre"], sum(notas_materia) / len(notas_materia))

    if not promedios:
        print("No hay notas registradas para ninguna materia")
        input("Presione enter para continuar...")
        return

    mejor_id = max(promedios, key=lambda x: promedios[x][1])
    peor_id  = min(promedios, key=lambda x: promedios[x][1])

    print(f"Materia con mejor promedio: {promedios[mejor_id][0]} ({promedios[mejor_id][1]:.2f})")
    print(f"Materia con peor promedio:  {promedios[peor_id][0]} ({promedios[peor_id][1]:.2f})")

    input("\nPresione enter para continuar")


#------- MEJOR ESTUDIANTE -------

def mejor_estudiante(estudiantes, notas):
    """Identifica y muestra al estudiante con el mayor promedio de notas."""
    limpiar_pantalla()
    print("=== MEJOR ESTUDIANTE ===")
    print()

    if len(notas) == 0:
        print("[x] No hay notas registradas")
    else:
        promedios = {}
        for n in notas:
            if n["id_estudiante"] not in promedios:
                promedios[n["id_estudiante"]] = []
            promedios[n["id_estudiante"]].append(n["nota"])

        mejor_legajo = max(promedios, key=lambda x: reduce(lambda acc, nota: acc + nota, promedios[x], 0) / len(promedios[x]))
        suma_notas   = reduce(lambda acc, nota: acc + nota, promedios[mejor_legajo], 0)
        mejor_promedio = suma_notas / len(promedios[mejor_legajo])

        for e in estudiantes:
            if e["legajo"] == mejor_legajo:
                print(f"Nombre: {e['nombre']}")
                print(f"Legajo: {e['legajo']}")
                print(f"Promedio: {mejor_promedio:.2f}")

    input("Presione enter para continuar...")


#------- PEOR ESTUDIANTE -------

def peor_estudiante(estudiantes, notas):
    """Identifica y muestra al estudiante con el menor promedio de notas."""
    limpiar_pantalla()
    print("=== PEOR ESTUDIANTE ===")
    print()

    if len(notas) == 0:
        print("[x] No hay notas registradas")
    else:
        promedios = {}
        for n in notas:
            if n["id_estudiante"] not in promedios:
                promedios[n["id_estudiante"]] = []
            promedios[n["id_estudiante"]].append(n["nota"])

        peor_legajo   = min(promedios, key=lambda x: sum(promedios[x]) / len(promedios[x]))
        peor_promedio = sum(promedios[peor_legajo]) / len(promedios[peor_legajo])

        for e in estudiantes:
            if e["legajo"] == peor_legajo:
                print(f"Nombre: {e['nombre']}")
                print(f"Legajo: {e['legajo']}")
                print(f"Promedio: {peor_promedio:.2f}")

    input("Presione enter para continuar...")


#------- MENU PRINCIPAL ESTADISTICAS -------

def mostrar_estadisticas():
    """Submenú de estadísticas. Recarga los datos en cada vuelta para reflejar
    cambios hechos desde otros menús. Accesible para cualquier rol."""
    while True:
        estudiantes = cargar_estudiantes()
        materias    = cargar_materias()
        notas       = cargar_notas()

        limpiar_pantalla()
        print("=== ESTADISTICAS ===")
        print()
        print("1 - Estadisticas generales")
        print("2 - Promedio general de estudiantes")
        print("3 - Promedio de un estudiante en todas las materias")
        print("4 - Promedio de una materia")
        print("5 - Promedio general de materias")
        print("6 - Mejor estudiante")
        print("7 - Peor estudiante")
        print("0 - Volver")
        print()

        opcion = input("Opcion: ")

        if opcion == '1':
            estadisticas_generales(estudiantes, materias, notas)
        elif opcion == '2':
            promedio_general_estudiantes(estudiantes, notas)
        elif opcion == '3':
            promedio_estudiante_materias(estudiantes, materias, notas)
        elif opcion == '4':
            promedio_materia(materias, notas)
        elif opcion == '5':
            promedio_general_materias(materias, notas)
        elif opcion == '6':
            mejor_estudiante(estudiantes, notas)
        elif opcion == '7':
            peor_estudiante(estudiantes, notas)
        elif opcion == '0':
            break
        else:
            limpiar_pantalla()
            print("Opcion invalida")
            input()
