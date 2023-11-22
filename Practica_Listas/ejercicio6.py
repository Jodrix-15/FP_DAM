#Creamos el menú
print("\nDel siguiente menú:\n")
print(f"\n[1]. AÑADIR PALABRA: Pide una cadena al usuario y la inserta en la lista\n"
      f"[2]. CONTAR: Pide una cadena y dice cuántas veces aparace en la lista\n"
      f"[3]. MODIFICAR: Pide una cadena y otra cadena a modificar, y modificará todas las apariciones de la primera en la segunda\n"
      f"[4]. ELIMINAR: Pide una cadena y la elimina de la lista\n"
      f"[5]. MOSTRAR PALABRAS: Muestra todas las palabras de la lista separadas por tabulaciones\n"
      f"[6]. ACABAR: Finalizar el programa\n")

opcion = int(input("Escoge una opción: ")) #pedimos al usuario que marque una opción del menú

listaPalabras = []
while opcion != 6: #se ejecuta mientras la opción no sea 6, si es 6 finaliza

    if opcion == 1:
        palabra = input("Introduce una palabra: ").lower()
        listaPalabras.append(palabra) #añadimos la palabra a la lista
        print("Palabra añadida correctamente")
        input("\nPULSA ENTER")

    elif opcion == 2:
        if len(listaPalabras) > 0: #comprobamos si la longitud de la lista es mayor que 0
            palabra = input("Introduce la palabra que quieras contar: ").lower()
            contador = 0
            for n in listaPalabras:#recorremos la lista
                if n == palabra: #comprueba si el valor de la lista coincide con la palabra que ha introducido el usuario
                    contador += 1 #contamos las veces que aparece la palabra en la lista
            print(f"La palabra '{palabra}' aparece {contador} veces en la lista")
            input("\nPULSA ENTER")
        else: #si la longitud de la lista es 0, no hay elementos en la lista
            print("Primero debes añadir palabras a la lista")
            input("\nPULSA ENTER")

    elif opcion == 3:
        if len(listaPalabras) > 0:
            palabra = input("Introduce la palabra que quieras modificar: ").lower()
            if palabra not in listaPalabras: #si la palabra no está en la lista
                print(f"La palabra {palabra} no se encuentra en la lista")
                input("\nPULSA ENTER")

            else: #si la palabra está en la lista
                palabraNueva = input("Introduce la palabra por la que quieras modicar la lista: ").lower()
                for i in range(len(listaPalabras)): #ejecutamos el bucle tantas veces como la longitud de la lista
                    if listaPalabras[i] == palabra: #comprobamos si la la palabra en la posición i, es igual a la palabra introducida por el usuario
                        listaPalabras[i] = palabraNueva #si se cumple la condición, en la posición i asignamos la modificación
                        palabraModificada = True
                if palabraModificada == True:
                    print("Palabra modificada correctamente")
                input("\nPULSA ENTER")
        else:
            print("Primero debes añadir palabras a la lista")
            input("\nPULSA ENTER")

    elif opcion == 4:
        existePalabra = False
        if len(listaPalabras) > 0:
            palabra = input("Introduce la palabra que deseas eliminar de la lista: ").lower()
            for p in listaPalabras:
                if p == palabra:
                    listaPalabras.remove(p) #eliminamos de la lista el elemento en la posición n
                    existePalabra = True

            if existePalabra == True:
                print(f"La palabra {palabra} se ha eliminado correctamente de la lista")

            if existePalabra == False: #si la palabra no está en la lista
                print(f"La palabra {palabra} no se encuentra en la lista")
            input("\nPULSA ENTER")
        else:
            print("Primero debes añadir palabras a la lista")
            input("\nPULSA ENTER")

    elif opcion == 5:
        if len(listaPalabras) > 0:
            for n in listaPalabras: #recorremos la lista e imprimimos cada uno de los elemntos que tiene
                print(n, end="\t")
            input("\n\nPULSA ENTER")
        else:
            print("No hay elementos en la lista")
            input("\nPULSA ENTER")

    else:
        print(f"ERROR. La opcion {opcion} no es válida")
        input("\nPULSA ENTER")

    print("\nDel siguiente menú:\n")
    print(f"\n[1]. AÑADIR PALABRA: Pide una cadena al usuario y la inserta en la lista\n"
          f"[2]. CONTAR: Pide una cadena y dice cuántas veces aparace en la lista\n"
          f"[3]. MODIFICAR: Pide una cadena y otra cadena a modificar, y modificará todas las apariciones de la primera en la segunda\n"
          f"[4]. ELIMINAR: Pide una cadena y la elimina de la lista\n"
          f"[5]. MOSTRAR PALABRAS: Muestra todas las palabras de la lista separadas por tabulaciones\n"
          f"[6]. ACABAR: Finalizar el programa\n")

    opcion = int(input("Escoge una opción: "))

print("Programa finalizado")