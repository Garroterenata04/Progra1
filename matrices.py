# PROMEDIO de notas
def calcular_promedio(estudiantes):

    if len(estudiantes) == 0:
        return 0

    suma = 0

    # recorre todas las filas
    for i in range(len(estudiantes)):
        suma += estudiantes[i][1]  # columna 1 = nota

    return suma / len(estudiantes)


# MEJOR estudiante (nota más alta)
def mejor_estudiante(estudiantes):

    if len(estudiantes) == 0:
        return None

    mejor = estudiantes[0]

    for i in range(len(estudiantes)):
        if estudiantes[i][1] > mejor[1]:
            mejor = estudiantes[i]

    return mejor


# PEOR estudiante (nota más baja)
def peor_estudiante(estudiantes):

    if len(estudiantes) == 0:
        return None

    peor = estudiantes[0]

    for i in range(len(estudiantes)):
        if estudiantes[i][1] < peor[1]:
            peor = estudiantes[i]

    return peor