#En este archivo he puesto todas las funciones que verifican si un dato se ha introducido correctamente o no.

import expediciones as e

def exit(comandos):
    return correctArgumentos(comandos, 1)

def valRegistar(comandos):
    if correctArgumentos(comandos, 4):
        e.registrar(comandos[1], comandos[2], comandos[3])

def valEliminar(comandos):
    if correctArgumentos(comandos, 2):
        if not diccionarioVacio(e.misiones):
            e.eliminar(comandos[1])

def valList(comandos):
    if correctArgumentos(comandos, 2):
        if not diccionarioVacio(e.misiones):
            if isNum(comandos[1]):
                if numPositivo(int(comandos[1])):
                    e.list(comandos[1])

def valSetmana(comandos):
    if correctArgumentos(comandos, 1):
        if not diccionarioVacio(e.misiones):
            e.setmana()

def valPrimera(comandos):
    if correctArgumentos(comandos, 1):
        if not diccionarioVacio(e.misiones):
            e.primera()

def diccionarioVacio(dicc):
    isEmpty = False
    if len(dicc) == 0:
        print("No hay ninguna misión registrada")
        isEmpty = True

    return isEmpty

def correctArgumentos(comList, numArguments):
    isCorrect = True
    if len(comList) != numArguments:
        print("ERROR. Nº de argumentos incorrecto")
        isCorrect = False

    return isCorrect

def isNum(string):
    esNumero = True
    if not string.isnumeric():
        print("ERROR. Debe ser un número que no sea negativo")
        esNumero = False

    return esNumero

def numPositivo(num):
    esPositivo = True
    if num < 1:
        print("ERROR. Debe ser un número mayor o igual a uno")
        esPositivo = False

    return esPositivo



