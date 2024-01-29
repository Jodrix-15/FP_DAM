import Interprete as itr


def main():

    finalizar = False
    while not finalizar:

        command = input("> ").lower()
        comList = command.split("-")
        opcion = comList[0]

        if opcion == "addllibre":
            itr.IaddLlibre(comList)

        elif opcion == "listllibres":
            itr.IListLlibres(comList)

        elif opcion == "listgenere":
            itr.IListGenere(comList)

        elif opcion == "maxllibre":
            itr.IMaxLlibre(comList)

        elif opcion == "info":
            itr.Iinfo(comList)

        elif opcion == "startprestec":
            itr.IStartPrestec(comList)

        elif opcion == "listprestecs":
            itr.IListPrestec(comList)

        elif opcion == "stats":
            itr.IStats(comList)

        elif opcion == "endprestec":
            itr.IEndPrestec(comList)

        elif opcion == "quit":
            finalizar = itr.IQuit(comList)

        else:
            print("OPCION NO VALIDA")

main()