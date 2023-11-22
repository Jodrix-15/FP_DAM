
numPruebas = int(input("Cuántas veces quieres probar el ejercicio?: "))

for prueba in range(numPruebas): #el bucle se ejecuta numPruebas veces

    frase = input("Introduce una frase: ").split() #pedimos al usuario que imprima una frase

    for palabra in range(len(frase)-1): #ejecutamos el bucle la longitud del array frase - 1 veces
        if len(frase[palabra+1]) > len(frase[palabra]): #miramos si el valor en la posicion+1 del array tiene una longitud mayor al valor en la posición actual
            frase[palabra] += "..." #si se cumple la condición añadimos los puntos suspensivos

    for palabra in frase: #recorremos la lista frase
        print(palabra, end=" ")
    print("\n")

print("Vuelve cuando quieras")


