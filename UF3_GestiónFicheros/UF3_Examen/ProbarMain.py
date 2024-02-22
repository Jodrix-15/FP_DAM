#Fichero para probar que todos los comandos de nuestro programa funcionan correctamente

pruebas = ["comando1 ejemplo1",
           "comando2 ejemplo2",
           "comando3 ejemplo3"
           ]

def main():

    for com in pruebas:
        comandos = com.split()
        #Escribir aqui el Main del examen sin el sys.argv


main()