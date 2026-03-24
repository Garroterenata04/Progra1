# LISTAS

# Concatenación
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print("Concatenación:", lista_concatenada) # [1, 2, 3, 4, 5, 6]
print()

# Copia
print("Copia de listas:")
lista_original = [1, 2, 3]
print("Original:", lista_original, "\t", id(lista_original)) 
lista_copia = lista_original.copy()
print("> Copia 1:", lista_copia, "\t", id(lista_copia)) 
lista_copia2 = lista_original[:]
print("> Copia 2:", lista_copia2, "\t", id(lista_copia2)) 
lista_copia3 = list(lista_original) 
print("> Copia 3:", lista_copia3, "\t", id(lista_copia3)) 
print()

# Multiplicación
listaNumeros = [1,2,3,4]
listaNumeros = listaNumeros * 2
print("Multiplicación:", listaNumeros) # [1, 2, 3, 4, 1, 2, 3, 4]
print()

# Pertenencia
print("Pertenencia:")
listaNumeros = [1,2,3,4]
print("¿4 está en la lista?", 4 in listaNumeros) # True
print("¿3 no está en la lista?", 3 not in listaNumeros) # False
print()

# Desempaquetado
print("Desempaquetado:")
listaNumeros = [1,2,3,4] #saca de la lista los elementos y los guarda en variables
print("Lista:", listaNumeros)
num1, num2, num3, num4 = listaNumeros
print("> Primer elemento:", num1) # 1
print("> Segundo elemento:",num2) # 2
print("> Tercer elemento:",num3) # 3
print("> Cuarto elemento:",num4) # 4