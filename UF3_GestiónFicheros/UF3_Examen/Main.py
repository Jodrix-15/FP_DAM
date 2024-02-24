#En este módulo se implementa el main, el cual usaremos para ejecutar el programa

import Validaciones as v
import sys

'''Esta función recibe una lista de argumentos desde la terminal y representa un menú'''
def main():

    comandos = sys.argv
    if len(comandos)>1:
        if comandos[1].lower() == "alta":
            v.valAlta(comandos[2:len(comandos)])
        elif comandos[1].lower() == "baixa":
            v.valBaixa(comandos[2:len(comandos)])
        elif comandos[1].lower() == "llistat":
            v.valLlistat(comandos[2:len(comandos)])
        elif comandos[1].lower() == "mitjana":
            v.valMitjana(comandos[2:len(comandos)])
        elif comandos[1].lower() == "stats":
            v.valStats(comandos[2:len(comandos)])
        else:
            print("OPCION NO VALIDA")
    else:
        print("ERROR. DEBES DAR AL MENOS UN ARGUMENTO")

main()