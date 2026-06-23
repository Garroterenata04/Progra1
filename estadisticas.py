from funciones import limpiar_pantalla, validar_numero
from functools import reduce

# Módulo de reportes/estadísticas sobre estudiantes, materias y notas.
# Usa programación funcional (map, filter, reduce, lambdas) en vez de
# bucles for tradicionales para calcular promedios.


#------- ESTADISTICAS GENERALES -------

def estadisticas_generales(estudiantes, materias, notas):
    limpiar_pantalla()
    print("=== ESTADISTICAS GENERALES ===")
    print()

    estudiantes_activos = [e for e in estudiantes if e["activo"]]
    materias_activas = [m for m in materias if m["activo"]]

    print(f"Total estudiantes activos: {len(estudiantes_activos)}")
    print(f"Total materias activas: {len(materias_activas)}")
    print(f"Total notas registradas: {len(notas)}")

    if len(notas) > 0:
        # map aplica la lambda a cada nota y devuelve solo el valor numérico.
        calificaciones = list(map(lambda n: n["nota"], notas))
        # reduce acumula la suma de todas las calificaciones, partiendo de 0.
        total_notas = reduce(lambda acc, nota: acc + nota, calificaciones, 0)
        promedio_general = total_notas / len(calificaciones)
        print(f"Promedio general de notas: {promedio_general:.2f}")

    input("Presione enter para continuar")


#------- PROMEDIO GENERAL DE ESTUDIANTES -------

def promedio_general_estudiantes(estudiantes, notas):
    # Muestra, para cada estudiante activo, el promedio de todas sus notas
    # (sin distinguir por materia).
    limpiar_pantalla()
    print("=== PROMEDIO GENERAL DE ESTUDIANTES ===")
    print()

    if len(notas) == 0:
        print("No hay notas registradas")
    else:
        for estudiante in estudiantes:
            if estudiante["activo"]:
                notas_filtradas = [n for n in notas if n["id_estudiante"] == estudiante["legajo"]]
                notas_alumno = list(map(lambda n: n["nota"], notas_filtradas))
                if notas_alumno:
                    promedio = sum(notas_alumno) / len(notas_alumno)
                    print(f"{estudiante['nombre']} (Legajo {estudiante['legajo']}): {promedio:.2f}")
                else:
                    print(f"{estudiante['nombre']} (Legajo {estudiante['legajo']}): Sin notas")

    input("Presione enter para continuar")


#------- PROMEDIO POR MATERIA (ESTUDIANTE ESPECIFICO) -------

def promedio_estudiante_materias(estudiantes, materias, notas):
    # Pide un legajo y muestra el promedio de ese estudiante en cada
    # materia por separado, más un promedio total.
    limpiar_pantalla()
    legajo = validar_numero("Ingrese el legajo del estudiante: ")

    # Buscar estudiante
    estudiante = None
    for e in estudiantes:
        if e["legajo"] == legajo:
            estudiante = e
            break

    if estudiante is None:
        print("Estudiante no encontrado")
        input()
        return

    limpiar_pantalla()
    print(f"=== PROMEDIOS DE {estudiante['nombre'].upper()} ===")
    print()

    notas_alumno = [n for n in notas if n["id_estudiante"] == legajo]

    if not notas_alumno:
        print("No hay notas para este estudiante")
    else:
        for materia in materias:
            if materia["activo"]:
                notas_filtradas = [n for n in notas_alumno if n["id_materia"] == materia["id"]]
                notas_materia = list(map(lambda n: n["nota"], notas_filtradas))
                if notas_materia:
                    promedio = sum(notas_materia) / len(notas_materia)
                    print(f"{materia['nombre']}: {promedio:.2f}")

        # Promedio general del alumno contando todas sus notas, sin
        # separar por materia.
        calificaciones_total = list(map(lambda n: n["nota"], notas_alumno))
        promedio_total = sum(calificaciones_total) / len(calificaciones_total)
        print(f"\nPromedio total: {promedio_total:.2f}")

    input("Presione enter para continuar")


#------- PROMEDIO DE MATERIA -------

def promedio_materia(materias, notas):
    # Pide un id de materia y muestra el promedio general de todas las
    # notas registradas para esa materia (de cualquier estudiante).
    limpiar_pantalla()
    print("Materias disponibles:")
    print()

    for m in materias:
        if m["activo"]:
            print(f"{m['id']} - {m['nombre']}")

    print()
    materia_id = validar_numero("Ingrese el ID de la materia: ")

    # Buscar materia
    materia = None
    for m in materias:
        if m["id"] == materia_id:
            materia = m
            break

    if materia is None:
        print("Materia no encontrada")
        input()
        return

    limpiar_pantalla()
    notas_materia = [n for n in notas if n["id_materia"] == materia_id]

    print(f"=== {materia['nombre'].upper()} ===")
    print()

    if not notas_materia:
        print(f"No hay notas para {materia['nombre']}")
    else:
        calificaciones = list(map(lambda n: n["nota"], notas_materia))
        total_notas = reduce(lambda acc, nota: acc + nota, calificaciones, 0)
        promedio = total_notas / len(calificaciones)
        print(f"Promedio general: {promedio:.2f}")
        print(f"Total notas: {len(notas_materia)}")

    input("Presione enter para continuar")


#------- MEJOR ESTUDIANTE -------

def mejor_estudiante(estudiantes, notas):
    limpiar_pantalla()
    print("=== MEJOR ESTUDIANTE ===")
    print()

    if len(notas) == 0:
        print("No hay notas registradas")
    else:
        # Agrupar notas por estudiante
        # promedios queda como {legajo: [nota1, nota2, ...]} para poder
        # calcular el promedio de cada estudiante por separado.
        promedios = {}
        for n in notas:
            if n["id_estudiante"] not in promedios:
                promedios[n["id_estudiante"]] = []
            promedios[n["id_estudiante"]].append(n["nota"])

        # Calcular el mejor promedio
        # max() recorre las claves (legajos) del diccionario y se queda con
        # la que tenga mayor promedio, calculado al vuelo con la lambda.
        mejor_legajo = max(promedios, key=lambda x: reduce(lambda acc, nota: acc + nota, promedios[x], 0) / len(promedios[x]))
        suma_notas = reduce(lambda acc, nota: acc + nota, promedios[mejor_legajo], 0)
        mejor_promedio = suma_notas / len(promedios[mejor_legajo])

        # Mostrar resultado
        for e in estudiantes:
            if e["legajo"] == mejor_legajo:
                print(f"Nombre: {e['nombre']}")
                print(f"Legajo: {e['legajo']}")
                print(f"Promedio: {mejor_promedio:.2f}")

    input("Presione enter para continuar")


#------- PEOR ESTUDIANTE -------

def peor_estudiante(estudiantes, notas):
    # Misma lógica que mejor_estudiante() pero usando min() en vez de max().
    limpiar_pantalla()
    print("=== PEOR ESTUDIANTE ===")
    print()

    if len(notas) == 0:
        print("No hay notas registradas")
    else:
        # Agrupar notas por estudiante
        promedios = {}
        for n in notas:
            if n["id_estudiante"] not in promedios:
                promedios[n["id_estudiante"]] = []
            promedios[n["id_estudiante"]].append(n["nota"])

        # Calcular el peor promedio
        peor_legajo = min(promedios, key=lambda x: sum(promedios[x]) / len(promedios[x]))
        peor_promedio = sum(promedios[peor_legajo]) / len(promedios[peor_legajo])

        # Mostrar resultado
        for e in estudiantes:
            if e["legajo"] == peor_legajo:
                print(f"Nombre: {e['nombre']}")
                print(f"Legajo: {e['legajo']}")
                print(f"Promedio: {peor_promedio:.2f}")

    input("Presione enter para continuar")


#------- MENU PRINCIPAL ESTADISTICAS -------

def mostrar_estadisticas(estudiantes, materias, notas):
    # Submenú de estadísticas: no distingue por rol, cualquier usuario
    # logueado puede ver todos los reportes (son de solo lectura).
    while True:
        limpiar_pantalla()
        print("=== ESTADISTICAS ===")
        print()
        print("1 - Estadisticas generales")
        print("2 - Promedio general de estudiantes")
        print("3 - Promedio de un estudiante en todas las materias")
        print("4 - Promedio de una materia")
        print("5 - Mejor estudiante")
        print("6 - Peor estudiante")
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
            mejor_estudiante(estudiantes, notas)

        elif opcion == '6':
            peor_estudiante(estudiantes, notas)

        elif opcion == '0':
            break

        else:
            limpiar_pantalla()
            print("Opcion invalida")
            input()
