#En este módulo se implementa el main, el cual usaremos para ejecutar el programa

import validaciones as v
import sys

'''Esta función recibe una lista de argumentos desde la terminal y representa un menú'''
def main():

    comandos = sys.argv
    if len(comandos)>1:
        if comandos[1].lower() == "afegir":
            if len(comandos) > 2:
                if comandos[2].lower() == "habitacio":
                    v.valAnyadirHab(comandos[1:len(comandos)])
                elif comandos[2].lower() == "reserva":
                    v.valAnyadirReserva(comandos[1:len(comandos)])
            else:
                print("ERROR. Si el primer argumento es 'añadir', debe haber obligatoriamente un segundo argumento")

        elif comandos[1].lower() == "finalitzar":
            v.valFinalizar(comandos[1:len(comandos)])
        elif comandos[1].lower() == "netejar":
            v.valLimpiar(comandos[1:len(comandos)])
        elif comandos[1].lower() == "list":
            v.valHabList(comandos[1:len(comandos)])
        elif comandos[1].lower() == "info":
            v.valInfo(comandos[1:len(comandos)])
        elif comandos[1].lower() == "reserves":
            v.valReservasList(comandos[1:len(comandos)])

        else:
            print("OPCION NO VALIDA")
    else:
        print("ERROR. DEBES DAR AL MENOS UN ARGUMENTO")

main()



