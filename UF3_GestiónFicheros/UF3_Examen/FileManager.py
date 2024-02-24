#En este módulo implemento todas las funciones que manejan ficheros para extraer o escribir datos

import os

nombreCarpeta = "documents"
nameFile = f"inscripcions.txt"
mediasFile = "mitjana.txt"
path = nombreCarpeta + "/" + nameFile
mediasPath = nombreCarpeta + "/" + mediasFile

GRADO = "GRADO"
NOTA = "NOTA ACCESO"
FECHA = "FECHA"


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
que el path existe. Si no existe lo crea. Siempre devuelve True'''
def valPath(nombreCarpeta, pathfile):
    pathValid = True
    if not os.path.exists(nombreCarpeta):
        os.mkdir(nombreCarpeta)
        if not os.path.exists(pathfile):
            crearFichero(pathfile)

    return pathValid


'''Esta función se debe modificar según lo que pida el examen'''
def getDatos():
    lineas = readFile(path)
    inscripciones = {}
    for li in lineas:
        alumno = li.split("/")
        if len(alumno)>1:
            inscripciones[alumno[0]] = {
                    GRADO: alumno[1],
                    NOTA: float(alumno[2]),
                    FECHA: alumno[3][:-1]
                }

    return inscripciones


'''Esta función registra [Rellenar según lo que pida el examen], con los datos que 
se le envían como argumentos'''
def escribir(linea):
    f = open(path, "a")
    f.write(f"{linea}\n")
    f.close()


'''Esta función recibe como argumento una lista de lineas actualizadas, y hace lo propio con el archivo'''
def actualizar(diccInscripciones):
    f = open(path, "w")
    lineas = []
    for dni, valores in diccInscripciones.items():
        lineas.append(f"{dni}/{valores[GRADO]}/{valores[NOTA]}/{valores[FECHA]}\n")
    f.writelines(lineas)
    f.close()

def escribirMedias(fecha, mediasDicc):
    f = open(mediasPath, "w")
    f.write(f"{fecha}\n")
    for grado, valores in mediasDicc.items():
        if valores["INSCRITOS"] == 0:
            f.write(f"{grado}-No hay alumnos inscritos en este ciclo\n")
        else:
            f.write(f"{grado}-{valores['NOTA_MEDIA']}\n")
    f.close()


