# LISTAS
# Métodos integrados

# a. Métodos para agregar elementos
print("a. Métodos para agregar elementos:")
nombres = ["María", "Luis", "Diego"]
nombres.append("Luciana") #agrega el valor de a uno al final de la lista
print("   > Append:", nombres) # ['María', 'Luis', 'Diego', 'Luciana']

numeros = [1, 2, 3]
numeros.extend([4, 5, 6]) # extener la lista con otra lista, sigue agregando al final
print("   > Extend:", numeros) # [1, 2, 3, 4, 5, 6]

estaciones = ["Verano", "Otoño", "Primavera"]
estaciones.insert(2, "Invierno") # inserta en el orden de la lista que quieras, si no pones el numero de posicion se agrega al final
print("   > Insert:", estaciones) # ['Verano', 'Otoño', 'Invierno', 'Primavera']

# Si no existe la posición lo agrega al final
colores = ["Verde", "Rojo", "Azul"]
colores.insert(4, "Naranja")
print("   > Insert:", colores) # ['Verde', 'Rojo', 'Azul', 'Naranja']
print()

# b. Métodos para quitar elementos
print("b. Métodos para quitar elementos:")
estaciones = ["Verano", "Otoño", "Invierno", "Primavera"]
estaciones.remove("Otoño") 
print("   > Remove:", estaciones) # ['Verano', 'Invierno', 'Primavera']

colores = ["Rojo", "Azul", "Verde", "Naranja"]
color_eliminado = colores.pop() #elimina el ultimo y devuelve
print("Color eliminado:", color_eliminado) # Color eliminado: Naranja
print("   > Pop:", colores) # ['Rojo', 'Azul', 'Verde']

meses = ["Abril", "Mayo", "Junio", "Julio"]
mes_eliminado = meses.pop(2) #elimina directamente la posicion que elegis
print("Mes eliminado:", mes_eliminado) # Mes eliminado: Junio
print("   > Pop:",meses) # ['Abril', 'Mayo', 'Julio']

nombres = ["María", "Luis", "Diego"]
nombres.clear()
print("   > Clear:", nombres) # []
print()

print("c. Otros métodos:")
vocales = ['a','e','i','o','u']
pos_i = vocales.index('i') #buscando la posicion de i en la lista . Ideal para busqueda de valores
print("   > Posición de i:", pos_i) # Posición de i: 2

nombres = ["Ana", "Luis", "Pedro", "Ana", "Carlos", "Ana", "Luis"]
cantidad_ana = nombres.count("Ana")
print("   > Apariciones de 'Ana':", cantidad_ana) # Apariciones de 'Ana': 3
print()

print("d. Métodos para invertir el orden 'in situ':")
numeros = [4, 2, 9, 1, 5, 6]
print("   > Original:", numeros) # [4, 2, 9, 1, 5, 6]
numeros.sort() #afecta a numeros, ordena la lista de menor a mayor 
print("   > Ordenada (0-9):", numeros) # [1, 2, 4, 5, 6, 9]
numeros.sort(reverse=True) # es falso por defecto, 
print("   > Ordenada (9-0):", numeros) # [9, 6, 5, 4, 2, 1]
numeros.sort(key=lambda x:x%2) # primero pares, luego impares. Al sort se le pasa una clave de ordenamiento
print("   > Por lambda:", numeros) # [6, 4, 2, 9, 5, 1]

vocales = ['a','e','i','o','u']
vocales.reverse()
print("   > Invertida:", vocales) # ['u', 'o', 'i', 'e', 'a']