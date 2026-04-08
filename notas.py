def menu_notas(notas):
    seleccion = ""

    while seleccion != "0":
        print("1 - Ingrese la nota. ")
        print("2 - Modifique la nota. ")
        print("3 - Promedio de notas. ")
        print("4 - Lista de notas. ")
        print("5 - Eliminar nota. ")
        print("0 - Volver al inicio")

        seleccion = input("Opcion: ")

        if seleccion == "1":
            agregar_nota(notas)
        elif seleccion == "2":
            modificar_nota(notas)
        elif seleccion == "3":
            promedio_nota(notas)
        elif seleccion == "4":
            lista_nota(notas)
        elif seleccion == "5":
            eliminar_nota(notas)
        elif seleccion == "0":
            input("Volviendo al inicio...")

        else:
            input("Seleccion invalida, toque ENTER para continuar. ")

def agregar_nota(notas): #use listas
    opc = input("1 - Ambas notas de los parciales | 2 - Primer parcial | 3 - Segundo parcial. ") 

    if opc == "1":
        p1=int(input("Nota del primer parcial: "))
        p2=int(input("Nota del segundo parcial: "))
        notas.append([p1, p2])
    elif opc == "2":
        p1=int(input("Nota del primer parcial: "))
        notas.append([p1, 0]) #el 0 para que deje el espacio vacio
    elif opc == "3":
        p2=int(input("Nota del segundo parcial: "))
        notas.append([0, p2])
    else:
        print("Opcion ingresada invalida. ")

def modificar_nota(notas): #listas
    if len(notas) == 0: #chequear si hay notas
        print("No hay notas disponibles. ")
        return
    for i in range(len(notas)):
        print(i, "-", notas[i])
    indice= int(input("Ingrese el indice que quiere modificar: "))

    if indice <0 or indice>= len(notas):
        print("El indice ingresado es invalido")
        return
    
    opcion = input("¿Desea modificar el primer parcial (1) o el segundo parcial (2)?")

    if opcion == "1":
        nueva = int(input("Ingrese la nueva nota del primer parcial: "))
        notas [indice][0] = nueva

    elif opcion == "2":
        nueva = int(input("Ingrese la nueva nota del segundo parcial: "))
        notas [indice][1] = nueva
    else:
        print("El numero ingresado es invalido. ")
        return 

def promedio_nota(notas): #listas, map, lambda
    if len(notas) == 0: #chequear si hay notas
        print("No hay notas disponibles. ")
        return
    
    suma = 0
    cantidad = 0

    for x in notas:
        suma += x[0] + x[1]
        cantidad += 2

    promedio = suma // cantidad

    print("El promedio de las notas es: ", promedio)




def lista_nota(notas): #listas y for 
    if len(notas) == 0: #para saber si la lista esta vacia 
        print("No hay notas disponibles. ")
        return

    for x in notas:  #recorre la lista
        print("Primer parcial:", x[0], "- Segundo parcial:", x[1]) #imprime las notas correspondiente a cadas parcial


def eliminar_nota(notas): #listas 
    if len(notas) == 0: #chequear si hay notas
        print("No hay notas disponibles. ")
        return
    for i in range (len(notas)): 
        print(i,"Primer parcial: ", notas[i][0], "Segundo parcial: ", notas[i][1]) #muestra las notas al usario

    indice=int(input("Legajo del alumno: ")) 

    if indice <0 or indice >= len(notas):
        print("El indice ingresado es invalido. ")
        return
    parcial= int(input("¿Que nota queres eliminar? (1 - primer parcial.  2 - segundo parcial): "))
    
    if parcial == 1:
        notas[indice][0] = 0
    elif parcial == 2:
        notas[indice][1] = 0
    else:
        print("Opcion ingresada invalida. ")
        return
    
    notas.pop(indice) #elimina la nota elegida
    print("La nota fue eliminada con exito. ")
