# LISTAS
# Funciones de listas

print("Funciones en listas:")
numeros = [5, 3, 8, 6, 2, 7, 4, 1] #sepuede hacer con numeros negativos tambien 
largo = len(numeros) 
print("Largo de la lista:", largo) # Largo de la lista: 8
suma_total = sum(numeros)
print("Suma:", suma_total) # Suma: 36
valor_minimo = min(numeros)
print("Valor mínimo:", valor_minimo) # Valor mínimo: 1
valor_maximo = max(numeros)
print("Valor máximo:", valor_maximo) # Valor máximo: 8
cadena_vocales = "aeiou"
lista_vocales = list(cadena_vocales)
print("Cadena:", cadena_vocales)
print("Cadena a lista:", lista_vocales) # ['a', 'e', 'i', 'o', 'u']