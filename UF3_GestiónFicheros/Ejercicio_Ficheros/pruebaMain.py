import validaciones as v
import sys

com = [
    "main añadir habitacion -1 4 50",
    "main añadir habitacion 0 1 50",
    "main añadir habitacion 1 0 40",
    "main añadir habitacion aa 1 40",
    "main añadir habitacion 100 aa 50",
    "main añadir habitacion 100 1 -1",
    "main añadir",
    "main añadir habitacion",
    "main añadir reserva",
    "main añadir reserva -1 hornos jordi 123 123",
    "main añadir reserva 0 hornos jordi 123 123",
    "main añadir reserva 100 hornos jordi 123456789 123123123",
    "main añadir reserva 100 hornos jordi 12345678z 123",
    "main finalizar",
    "main finalizar 100 -1",
    "main limpiar",
    "main limpiar 100",
    "main finalizar 100 5",
    "main list",
    "main info 12345678Z",
    "main info asdf asdf",
    "main reservas",
    "main reservas 234",
    "main añadir habitacion 104 4 50",
    "main reservas",
    "main list",
    "main añadir reserva 104 hornos jordi 12345678z 123456789",
    "main añadir habitacion 105 2 60",
    "main list",
    "main finalizar 100 0",
    "main finalizar 105 4",
    "main añadir habitacion 106 2 40",
    "main añadir reserva 105 segura albert 45790286t 123456789",
    "main info 12345678z",
    "main info 23415678E",
    "main reservas",
    "main finalizar 104 0",
    "main list",
    "main finalizar 105 4",
    "main list",
    "main limpiar 106",
    "main limpiar 104",
    "main limpiar 105",
    "main list",
]

def main():

    for comand in com:
        comandos = comand.split(" ")
        if len(comandos)>1:
            if comandos[1].lower() == "añadir":
                if len(comandos) > 2:
                    if comandos[2].lower() == "habitacion":
                        v.valAnyadirHab(comandos[1:len(comandos)])
                    elif comandos[2].lower() == "reserva":
                        v.valAnyadirReserva(comandos[1:len(comandos)])
                else:
                    print("ERROR. Si el primer argumento es 'añadir', debe haber obligatoriamente un segundo argumento")

            elif comandos[1].lower() == "finalizar":
                v.valFinalizar(comandos[1:len(comandos)])
            elif comandos[1].lower() == "limpiar":
                v.valLimpiar(comandos[1:len(comandos)])
            elif comandos[1].lower() == "list":
                v.valHabList(comandos[1:len(comandos)])
            elif comandos[1].lower() == "info":
                v.valInfo(comandos[1:len(comandos)])
            elif comandos[1].lower() == "reservas":
                v.valReservasList(comandos[1:len(comandos)])

            else:
                print("OPCION NO VALIDA")
        else:
            print("ERROR. DEBES DAR AL MENOS UN ARGUMENTO")

main()