
finalizar = False
modulos = {}

while finalizar == False:

    print("Del siguiente menú: ")
    print(f"\n[1]. Alta módulo\n"
          f"[2]. Alta de nota de una unidad formativa de un módulo\n"
          f"[3]. Ver datos de un módulo\n"
          f"[4]. Ver % de unidades formativas aprobadas\n"
          f"[5]. Salir\n")

    opcion = int(input("Escoge una opcion: "))
    print()

    if opcion == 1:
        nombreModulo = input("Nombre módulo: ").upper()
        if nombreModulo not in modulos:
            modulos[nombreModulo] = {}
            print("Módulo agregado correctamente\n")
        else:
            print("El modulo ya se encuentra en la base de datos\n")

        input("PULSA ENTER")

    elif opcion == 2:
        if len(modulos)>0:
            modulo = input("A qué módulo quieres añadir la Unidad Formativa?: ").upper()
            if modulo in modulos:
                nombreUF = input("Nombre Unidad Formativa: ").upper()
                if nombreUF not in modulos[modulo]:
                    nota = int(input("Nota de la unidad formativa (entre 1 y 10): "))
                    while nota <1 or nota>10:
                        nota = int(input("ERROR. La nota de la unidad formativa debe estar entre 1 y 10: "))

                    modulos[modulo][nombreUF] = nota

                    print("Unidad formativa agregada correctamente\n")

                else:
                    print("La unidad formativa ya tiene una nota registrada\n")
            else:
                print("El módulo no se encuentra en la base de datos\n")
        else:
            print("Primero debes añadir modulos\n")

        input("PULSA ENTER")


    elif opcion == 3:
        if len(modulos)>0:
            modulo = input("Qué módulo quieres ver?: ").upper()
            sumarNotas = 0
            asignaturasSuspendidas = []

            if modulo in modulos:
                for k in modulos:
                    if k == modulo:
                        print(f"\nModulo: {k}\n"
                              f"Nº de Unidades Formativas registradas: {len(modulos[k])}")

                        for uf in modulos[k]:
                            print(f"{uf}: {modulos[k][uf]}")
                            if modulos[k][uf] < 5:
                                asignaturasSuspendidas.append(uf)

                if len(asignaturasSuspendidas) == 0:

                    for uf in modulos[modulo]:
                        sumarNotas += modulos[modulo][uf]

                    if(len(modulos[modulo]))>0:
                        notaMedia = sumarNotas / len(modulos[modulo])
                        print(f"Nota media: {int(notaMedia)}")

            else:
                print("El módulo no se encuentra en la base de datos")
        else:
            print("Primero debes añadir modulos")
        print()
        input("PULSA ENTER")

    elif opcion == 4:
        if len(modulos)>0:

            UFaprobadas = []
            UFTotales = 0

            for k in modulos:
                UFTotales += len(modulos[k])
                for n in modulos[k]:
                    if modulos[k][n] >= 5:
                        UFaprobadas.append(n)

            if UFTotales >0:
                porcentaje = (len(UFaprobadas) / UFTotales)*100

                print(f"Porcentaje de UFs aprobadas: {porcentaje}%\n")
            else:
                print("No se han añadido ninguna UF\n")
        else:
            print("Primero debes añadir modulos\n")

        input("PULSA ENTER")

    elif opcion == 5:
        print("Programa finalizado")
        finalizar = True

    else:
        print("Opcion no válida\n")
        input("PULSA ENTER")