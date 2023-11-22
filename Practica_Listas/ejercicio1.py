
num = int(input("Introduce un número (introduce un número negativo para finalizar): "))
numList = []
if num > -1:
    while num > -1: #ejecutamos el bucle mientras el número no sea negativo
        numList.append(num) #añadimos el número a la lista
        num = int(input("Introduce un número (introduce un número negativo para finalizar): "))

    print("Lista de números: ")
    for n in numList: #recorremos la lista e imprimimos el valor
        print(n, end=" ")

    noDuplicadosList = []

    print("\nLista números sin repeticiones: ")
    for n in numList: #recorremos la lista
        if n not in noDuplicadosList: #si el valor de n no está en la lista noDuplicadosList
            noDuplicadosList.append(n) #añade el valor de n en la lista noDuplicadosList

            print(n, end=" ") #imprime el valor de n
else:
    print("Programa finalizado")