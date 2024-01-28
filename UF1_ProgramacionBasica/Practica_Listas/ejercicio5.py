
numPruebas = int(input("Cuántas veces quieres probar el ejercicio?: "))

for prueba in range(numPruebas): #ejecutamos el bucle numPruebas veces
    valores = input().split() #crearemos una lista con n elementos que le pediremos al usuario separados por un espacio
    numCamiones = int(valores[0])#la posición 0 es el numero de camiones
    suma = 0
    esCorrecto = True
    for v in valores:# recorremos los valores
        if int(v) < 0: #miramos si hay algún valor negativo
            esCorrecto = False

    if esCorrecto == False:
        print("ERROR. Ni cantidad de patatas ni el número de camiones puede ser negativa")

    while esCorrecto == False or len(valores) - 1 != numCamiones:
        if len(valores) - 1 != numCamiones:
            print("ERROR. El primer valor es el numero de camiones, después debes dar tantos valores (seguidos de un espacio) como camiones hay")
        valores = input().split()  # crearemos una lista con n elementos que le pediremos al usuario separados por un espacio
        numCamiones = int(valores[0])
        esCorrecto = True

        for v in valores:
            if int(v) < 0:
                esCorrecto = False

        if esCorrecto == False:
            print("ERROR. Ni cantidad de patatas ni el número de camiones puede ser negativa")

    for numPatatas in valores[1:numCamiones+1]: #recorremos los valores desde la posición 1 hasta numCamiones+1, el cual se excluye
        suma += int(numPatatas) #sumamos las patatas que lleva el camión
    print(f"Patatas descargadas en el dia: {suma}")


print("Vuelve cuando quieras")