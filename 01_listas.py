# LISTAS se recomiendan correrla con for in range
# Creación, acceso a elementos y actualización de valores
print("Creación, acceso a elementos y actualización de valores:")
frutas = ["manzana", "banana", "cereza", "durazno"]
print("Lista:", frutas)
print("Primer elemento:", frutas[0]) # manzana
print("Tercer elemento:",frutas[2]) # cereza
print("Último elemento (largo-1):", frutas[len(frutas)-1]) # durazno
print("Último elemento [-1]:", frutas[-1]) # durazno
print("Primer elemento:", frutas[-len(frutas)]) # manzana
print()
frutas[1] = "naranja" # Asignación de valor
print(frutas) # ['manzana', 'naranja', 'cereza', 'durazno']
# print(frutas[4]) # IndexError: list index out of range

print()

# Otros ejemplos de listas
print("Otros ejemplos de listas:")
listaNumeros = [1,2,3,4]
listaTexto = ["Hola", "Mundo", "!"]
listaDistintosTipos = ["A", True, 123, 123.12]
listaDeListas = [ [1,2,3], [4,5,6] ]
listaVacia = [ ] # También puede usarse list()
print(listaNumeros)
print(listaTexto)
print(listaDistintosTipos)
print(listaDeListas)
print(listaVacia)

lista = [ ]
for i in range(4):
    lista.append(i**2) # Resultado: [0, 1, 4, 9]
print()

print("Impresión de listas con for y while:")
# Impresión de listas con for y while
print("> For:")
for i in range(len(lista)):
    print(lista[i], end=' ')
print()
# Resultado: 0 1 4 9 

print("> While:")
pos = 0
while pos < len(lista):
    print(lista[pos], end=' ')
    pos += 1
print()
# Resultado: 0 1 4 9

# También es posible iterar una lista utilizando el operador in
print("> For in:")
for valor in lista:
    print(valor, end=" ")
# Resultado: 0 1 4 9