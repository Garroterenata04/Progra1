# LISTAS
# Listas por comprensión

# Forma de crear una lista tradicional
numeros = [0,1,2,3,4,5]
cuadrados = []
for num in numeros:
    cuadrados.append(num**2)
print("Lista tradicional:", cuadrados)
# [0, 1, 4, 9, 16, 25]

# A través de listas por comprensión
numeros = [0,1,2,3,4,5]
cubos = [num**3 for num in numeros]
print("Lista por comprensión:", cubos) # [0, 1, 8, 27, 64, 125]

# Es posible filtrar elementos, incorporando if / if-else
lista = [1,-2,5,0,3,4]
listaCuadradosParesPorComp = [num**2 for num in lista if num%2==0]
print("Lista filtrada:", listaCuadradosParesPorComp) # [4, 0, 16]

# Elevo al cuadrado los pares y los impares quedan igual
lista = [1,-2,5,0,3,4] #es igual (para el examen)
listaPorComp = [num**2 if num%2==0 else num for num in lista]
print("lista modificada:", listaPorComp) # [1, 4, 5, 0, 3, 16]
