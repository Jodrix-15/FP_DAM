#En este módulo implemento todas las funciones que manejan ficheros para extraer o escribir datos

import os

nombreCarpeta = "Data"
reservasFile = f"Reservas.txt"
habitacionesFile = "Habitaciones.txt"
CAPACIDAD = "capacidad"
PRECIO = "precio"
ESTADO = "estado"
NOMBRE = "Nombre"
APELLIDO = "Apellido"
DNI = "DNI"
TELEF = "Teléfono"

habitacionesPath = nombreCarpeta + "/" + habitacionesFile
reservasPath = nombreCarpeta + "/" + reservasFile

'''Esta función recibe como argumento el nombre de una carpeta y la crea'''
def dirExist(dir):

    print(f"Creando carpeta {nombreCarpeta}...")
    os.mkdir(dir)

'''Esta función recibe un path y el nombre del fichero, Y crea el fichero'''
def fileExist(pathFile, nameFile):

    print(f"Creando fichero {nameFile}...")
    f = open(pathFile, "w")
    f.close()

'''Esta función recibe como argumentos el path de un fichero y el nombre del mismo.
Si el path es válido devolverá una lista con todas las líneas del fichero. En caso contrario
devuelve una lista vacía'''
def readFile(pathFile, nameFile):
    lineas = []
    if valPath(nombreCarpeta, pathFile, nameFile):
        f = open(pathFile, "r")
        lineas = f.readlines()
        f.close()

    return lineas


'''Esta función devuelve un diccionario con las habitaciones que se encuentran en el archivo con el mismo nombre'''
def getDataHabitaciones():
    habitaciones = {}
    lineas = readFile(habitacionesPath, habitacionesFile)

    if len(lineas) != 0:
        for hab in lineas:
            dataHab = hab.split(",")
            habitaciones[dataHab[0]] = {
                CAPACIDAD: dataHab[1],
                PRECIO: dataHab[2],
                ESTADO: dataHab[3][:-1]
            }

    return habitaciones

'''Esta función devuelve un diccionario con las reservas que se han hecho en el hotel'''
def getDataReservas():

    reservas = {}
    lineas = readFile(reservasPath, reservasFile)
    if len(lineas) != 0:
        for re in lineas:
            re = re.replace("\n", "")
            dataReservas = re.split(",")
            reservas[dataReservas[0]] = {
                NOMBRE: dataReservas[1],
                APELLIDO: dataReservas[2],
                DNI: dataReservas[3],
                TELEF: dataReservas[4]
            }
    return reservas

'''Esta función recibe como argumentos un path, un mensaje y el nombre de un fichero y comprueba
si el fichero esta vacía. Si lo está devuelve True, y False si no lo está'''
def ficheroVacio(pathFile, msj, nameFile):

    estaVacio = False
    if len(readFile(pathFile, nameFile)) == 0:
        print(msj)
        estaVacio = True

    return estaVacio

'''Esta función recibe el nombre de una carpeta, un path, y el nombre de un fichero. Comprueba
que el path existe. Si existe devuelve True, si no, devuelve False'''
def valPath(nombreCarpeta, pathfile, nameFile):
    pathValid = False
    if os.path.exists(nombreCarpeta):
        if os.path.exists(pathfile):
            pathValid = True
        else:
            print(f"El fichero no existe")
            fileExist(pathfile, nameFile)
    else:
        print("La carpeta no existe")
        dirExist(nombreCarpeta)

    return pathValid

'''Esta función registra una nueva habitación en la base de datos del hotel, con los datos que 
se le envían como argumentos'''
def escribirHabitaciones(numHab, capacidad, precio, estado):
    f = open(habitacionesPath, "a")
    f.write(f"{numHab},{capacidad},{precio},{estado}\n")
    f.close()

'''Esta función realiza una nueva reserva en el fichero de reservas del hotel con los datos que 
se le envían como argumentos'''
def escribirReservas(numHab, nombre, apellido, dni, tlf):
    f = open(reservasPath, "a")
    f.write(f"{numHab},{nombre},{apellido},{dni},{tlf}\n")
    f.close()

'''Esta función recibe como argumento una lista de lineas actualizadas, y hace lo propio con el archivo
de habitaciones'''
def actualizarHabitacionesFile(lineas):
    f = open(habitacionesPath, "w")
    f.writelines(lineas)
    f.close()

'''Esta función recibe como argumentos el número de habitación y el estado al que se la quiere cambiar
Devuelve una lista con los estados actualizados'''
def cambiarEstadoFile(numHab, nuevoEstado):

    f = open(habitacionesPath, "r")
    lineas = f.readlines()
    f.close()

    for i in range(len(lineas)):
        if lineas[i] != None:
            datosHab = lineas[i].split(",")
            if datosHab[0] == numHab:
                datosHab[3] = datosHab[3].replace(datosHab[3][:-1], nuevoEstado)
                lineaActualizada = f"{datosHab[0]},{datosHab[1]},{datosHab[2]},{datosHab[3]}"
                lineas.pop(i)
                lineas.insert(i, lineaActualizada)

    return lineas

'''Esta función recibe como argumento un diccionario con las reservas actualizadas, y actualiza los cambios en 
el fichero de reservas'''
def actualizarReservasFile(diccReservas):
    f = open(reservasPath, "w")
    for numHab, data in diccReservas.items():
        f.write(f"{numHab},{data[NOMBRE]},{data[APELLIDO]},{data[DNI]},{data[TELEF]}\n")
    f.close()




