import Biblioteca as b

def correctArguments(comList, numArguments):
    isCorrect = True

    if len(comList) != numArguments:
        print("ERROR: nº de argumentos incorrecto")
        isCorrect = False

    return isCorrect

def libraryEmpty():

    isEmpty = False
    if len(b.getLibros()) == 0:
        print("No hay ningún libro registrado")
        isEmpty = True

    return isEmpty


def IaddLlibre(comList):

    if correctArguments(comList, 6):

        codigo = comList[1].upper()
        isAlNum, exist, isNum = True, True, True

        if codigo.isalnum() == False:
            print("ERROR: El código debe ser alfanumérico")
            isAlNum = False

        if codigo in b.getLibros():
            print("ERROR. Ya existe un libro con el mismo código")
            exist = False

        numPag = comList[5]

        if numPag.isnumeric() == False:
            print("ERROR: El número de páginas debe contener un número mayor que cero")
            isNum = False


        if isAlNum == True and isNum == True and exist == True:
            b.addLlibre(codigo, comList[2], comList[3], comList[4], numPag)


def IListLlibres(comList):

    if correctArguments(comList, 1):
        if libraryEmpty() == False:
            b.listLibros()

def IListGenere(comList):

    if correctArguments(comList, 2):
        if libraryEmpty() == False:
            b.listGenere(comList[1])

def IMaxLlibre(comList):
    if correctArguments(comList, 1):
        if libraryEmpty() == False:
            b.maxLibros()

def Iinfo(comList):
    if correctArguments(comList, 2):
        if comList[1] in b.getAlumnos():

            if len(b.getAlumnos()[comList[1]]["En Prestec"]) == 0:
                print(f"El alumno {comList[1]} no tiene ningún libro en préstamo")
            else:
                b.info(comList[1])

                if len(b.getAlumnos()[comList[1]]["Incidencias"]) != 0:
                    print("\nIncidencias: ")
                    for incd in b.getAlumnos()[comList[1]]["Incidencias"]:
                        print(incd)
                else:
                    print(f"El alumno {comList[1].upper()} no tiene ninguna incidencia\n")
        else:
            print(f"El alumno {comList[1].upper()} no se encuentra en la base de datos")



def IStartPrestec(comList):

    if correctArguments(comList, 4):
        alumno = comList[2]
        startDate = b.fecha2Date(comList[3])
        if libraryEmpty() == False:
            if comList[1].upper() in b.getLibros():
                if b.getLibros()[comList[1].upper()]["Estado"].lower() == "disponible":
                    b.startPrestec(comList[1].upper(), alumno, startDate)

                else:
                    print(f"ERROR. El libro con el código {comList[1]} ya está en préstamo")

            else:
                print(f"El libro con el código {comList[1]} no existe")

def IListPrestec(comList):

    if correctArguments(comList, 1):
        if libraryEmpty() == False:
            b.listPrestec()

def IStats(comList):

    if correctArguments(comList, 1):
        if libraryEmpty() == False:
            b.stats()

def IEndPrestec(comList):

    if correctArguments(comList, 3):
        fechaRetorno = b.fecha2Date(comList[2])
        i = 0
        libroEncontrado = False
        if libraryEmpty() == False:
            if comList[1].upper() not in b.getLibros():
                print(f"El libro con código {comList[1].upper()} no se encuentra en la base de datos")
            else:
                while libroEncontrado == False and i < len(b.getLibros()):

                    if b.getLibros()[comList[1].upper()]["Estado"] == "En Prestec":
                        for a, v in b.getAlumnos().items():
                            if comList[1].upper() in v["En Prestec"]:
                                alumno = a
                                fechaInicio = b.fecha2Date(v["En Prestec"][comList[1].upper()]["Inicio"])
                                fechaFin = b.fecha2Date(v["En Prestec"][comList[1].upper()]["Fin"])

                                libroEncontrado = True
                    i+=1

                if libroEncontrado:
                    if fechaRetorno < fechaInicio:
                        print("ERROR. No se puede develover un libro antes del día del préstamo")

                    else:
                        b.endPrestec(comList[1].upper(), alumno, fechaInicio, fechaFin, fechaRetorno)

                else:
                    print("ERROR. El libro no está en préstamo")

def IQuit(comList):
    return correctArguments(comList, 1)









