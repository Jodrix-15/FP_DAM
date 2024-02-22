#En este módulo se implementa el main, el cual usaremos para ejecutar el programa

import Validaciones as v
import sys

'''Esta función recibe una lista de argumentos desde la terminal y representa un menú'''
def main():

    comandos = sys.argv
    if len(comandos)>1:
        if comandos[1].lower() == "":
            if len(comandos) > 2:
                if comandos[2].lower() == "":

                elif comandos[2].lower() == "":

                else:
                    print("ERROR. El segundo argumento debe ser 'o' o ''")
            else:
                print("ERROR. Si el primer argumento es '', debe haber obligatoriamente un segundo argumento")

        elif comandos[1].lower() == "":

        elif comandos[1].lower() == "":

        elif comandos[1].lower() == "":

        elif comandos[1].lower() == "":

        elif comandos[1].lower() == "":


        else:
            print("OPCION NO VALIDA")
    else:
        print("ERROR. DEBES DAR AL MENOS UN ARGUMENTO")

main()