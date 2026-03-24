numeros=[1,2,3,4]
print(numeros)

listaVariada = ["Julian",1.3,25]

print(listaVariada)

print(listaVariada[0])
print(listaVariada[1])
print(listaVariada[2])

print(listaVariada[-1])
print(listaVariada[-2])
print(listaVariada[-3])


vocales =['a','e','i','o','u']

print(vocales[-3])

#Añadir nuevos elementos
listaVariada.append("Tomate")

print(listaVariada[3])

#Operador de concatenacion +

lista1=[1,2,3]
lista2=[4,5,6]

listaUnida = lista1+lista2

print(listaUnida)

listaUnida[5]="Pepe"

print(listaUnida)

#Eliminar un elmento de una lista

print(vocales)
del vocales[1] #Eliminar el segundo elemento de la lista de vocales

print(vocales)

#Metodo remove y el pop

#Remove elimina la primer ocurrencia del elemento que le pasamos. 

listaNombres=["Pepe", "Juan", "Lucia","Pepe","Pedro"]
print(listaNombres)
listaNombres.remove("Pepe")
print(listaNombres)

#pop le pasamos un indice y elimina el elemento que esta en ese indice de la lista. 

listaNombres.pop()
print(listaNombres)

#Clear
listaNombres.clear()
print(listaNombres)

#Funcion len

listaLegajos = [2589,14785,2596,1756]
print(len(listaLegajos))

for i in range(len(listaLegajos)):  #0,1,2,3
    print(listaLegajos[i])


##Operador in y not in

frutas=["manzana","pera","durazno","limon"]

if 'durazno' not in frutas:
    print("Tenemos duraznos")
else:
    print("Anda a otra verduleria")

#Empaquetado y desempaquetado 

n1=10
n2=11
n3=14

#Empaquetado 
listaDos = [n1,n2,n3]


#Desempaquetado 

fruta1,fruta2,fruta3,fruta4 = frutas 

print(fruta1)

#Replicar listas

listaOriginal=[1,2,3]
listaTriplicada=listaOriginal*3

print(listaTriplicada)