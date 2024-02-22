#En este módulo implemento todas las funciones que manejan ficheros para extraer o escribir datos

import os

nombreCarpeta = "Datos"
nameFile = f"prueba.txt"
path = nombreCarpeta + "/" + nameFile


'''Esta función recibe un path y crea el fichero'''
def crearFichero(pathFile):
    f = open(pathFile, "w")
    f.close()


'''Esta función recibe como argumentos el path de un fichero.
Si el path es válido devolverá una lista con todas las líneas del fichero. En caso contrario
devuelve una lista vacía'''
def readFile(pathFile):
    lineas = []
    if valPath(nombreCarpeta, pathFile):
        f = open(pathFile, "r")
        lineas = f.readlines()
        f.close()

    return lineas


'''Esta función recibe el nombre de una carpeta y un path. Comprueba
que el path existe. Si existe devuelve True, si no, devuelve False'''
def valPath(nombreCarpeta, pathfile):
    pathValid = True
    if not os.path.exists(nombreCarpeta):
        os.mkdir(nombreCarpeta)
        if not os.path.exists(pathfile):
            crearFichero(pathfile)

    return pathValid


'''Esta función se debe modificar según lo que pida el examen'''
def getDatos():

    return readFile(path)


'''Esta función registra [Rellenar según lo que pida el examen], con los datos que 
se le envían como argumentos'''
def escribir(linea):
    f = open(path, "a")
    f.write(f"{linea}\n")
    f.close()


'''Esta función recibe como argumento una lista de lineas actualizadas, y hace lo propio con el archivo'''
def actualizar(lineas):
    f = open(path, "w")
    f.writelines(lineas)
    f.close()

