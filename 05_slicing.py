# LISTAS
# Slicing

numeros = [2, 34, 25, 1, 19, 23, 48, 19, 38, 9]

print("Lista Original:", numeros)
# Extraer una subsección de la lista 
print("Subsección:", numeros[2:5]) # [25, 1, 19]
print("Omitir 'inicio':", numeros[:4]) # [2, 34, 25, 1]
print("Omitir 'fin':", numeros[5:]) # [23, 48, 19, 38, 9]
print()

# Superar índice
print("Superar índice:", numeros[1:100]) # [34, 25, 1, 19, 23, 48, 19, 38, 9] #considera desde la posicion 1 no la 0 
print()

# Índices Negativos
print("Índices Negativos:", numeros[-5:-2]) # [23, 48, 19] #cuenta desde atras, el ultimo no se considera 
print()

# Incremento e incremento negativo
print("Incremento:", numeros[2:7:2]) # [25, 19, 48] de la posicion 2 a la 6 de dos en dos
print("Incremento negativo:", numeros[7:1:-2]) # [19, 23, 1] # desde la posicion 7 a la 2 de dos en dos 
print()

# Invertir una lista
print("Invertir una lista:", numeros[::-1]) # [9, 38, 19, 48, 23, 19, 1, 25, 34, 2]
print()

# Reemplazar elementos
lista = [19, 23, 48, 19, 38, 9]
lista[2:4] = [80,85] #reemplaxa los numeros que esten la posicion 2 y 4
print("Reemplazar elementos:", lista) # [19, 23, 80, 85, 38, 9]

# Eliminar elementos
lista[2:4] = []
print("Eliminar elementos:", lista) # [19, 23, 38, 9]

# Reemplazar e insertar elementos
lista = [19, 23, 48, 19, 38, 9]
lista[2:4] = [80, 85, 101]
print("Reemplazar elementos:", lista) # [19, 23, 80, 85, 101, 38, 9]
lista = [19, 23, 48, 19, 38, 9]
lista[2:4] = [99]
print("Insertar elementos:", lista) # [19, 23, 99, 38, 9]
print()

# Rebanadas nulas – insertar elementos
lista = [19, 23, 48, 19, 38, 9]
lista[2:2] = [110, 115, 118]
print("Rebanadas nulas - insertar elementos:", lista) # [19, 23, 110, 115, 118, 48, 19, 38, 9]
#rebanada nula es cuando el inicio y el fin es el mismo, se puede usar para meter elementos

# Rebanadas para realizar copias
print("Rebanadas para realizar copias:") #tomo una lista y no le paso valord e inciio ni de fin, entonces hace una copia en otra variable
listaOriginal = [2, 34, 25]
listaCopia = listaOriginal[:]
listaCopia.append(18)
print("> Original: ", listaOriginal) # [2, 34, 25]
print("> Copia: ", listaCopia) # [2, 34, 25, 18]
print()

# Recorrer parcialmente una lista utilizando rebanadas
print("Recorrer parcialmente una lista utilizando rebanadas:")
lista = [19, 23, 48, 19, 38, 9]
for i in lista:
    print(i, end=" ") # 19 23 48 19 38 9 
print()
for i in lista[2:5]:
    print(i, end=" ") # 48 19 38
print()

'''
print("¿Cuál es la salida?")
# ¿Cuál es la salida?
lista = [19, 23, 48, 19, 38, 9]
for i in lista[::2]: #de principio a fin y salta cada dos elementos 
    print(i, end=" ")
print()
'''

# Desafío
def partirLista(lista):
    # .....
    mitad = int(len(lista)/2)
    listaPrimeraParte = lista[:mitad]
    listaSegundaParte = lista[mitad:]
    return listaPrimeraParte, listaSegundaParte

#lista = [25,46,12,34]
#print(partirLista(lista))