#En este archivo solo hay una función y es la que ejecuta el programa

import validaciones as v

def main():

    finalizar = False
    while not finalizar:
        comando = input().lower().split(",")

        if comando[0] == "registrar":
            v.valRegistar(comando)

        elif comando[0] == "esborrar":
            v.valEliminar(comando)

        elif comando[0] == "list":
            v.valList(comando)

        elif comando[0] == "setmana":
            v.valSetmana(comando)

        elif comando[0] == "primera":
            v.valPrimera(comando)

        elif comando[0] == "exit":
            if v.exit(comando):
                finalizar = True

        else:
            print("Opción no válida")

main()