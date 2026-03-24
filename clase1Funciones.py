#Declaracion de una funcion 
def sumar(a,b):
    suma=a+b
    print("La suma de los valores es ",suma)


def areaTriangulo(base,altura):
    return (base*altura)/2


def agregarElementoLista(lista):
    lista.append(58)

def modificarValor(x):
    x=15
    print("Valor adentro de la funcion de x ",x)


def saludar(nombre):
    """"Objetivo: Saludar a alguien
    Parametros Entrada: 
      - Nombre de persona: string
    Parametros de Salida: Ninguno """
    print("Hola ",nombre)

def cambiarValorNumero():
    global numero 
    numero=10

print("SCOPE VARIABLES")
numero=20
print(numero)
cambiarValorNumero()
print(numero)
print("#######################")

num1=20
num2=25

num3=88
num4=47

#Invocacion de una funcion
print(sumar(num1,num2))
sumar(num3,num4)

print("Area de triangulo",areaTriangulo(200,14))

##Mutables
lista=[6,7,8,9]

agregarElementoLista(lista)

print(lista)


#Inmutables 
a=25
print("Valor de a antes de invocar la funcion: ",a)
modificarValor(a)
print("Valor de a despues de invocar la funcion: ",a)



help(saludar)


