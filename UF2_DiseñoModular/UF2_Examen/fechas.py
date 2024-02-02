#En este archivo he puesto todas las funciones que manipulan fechas

import datetime as d

#formato = "%d-%m-%Y"

def hoy():
    return d.date.today()
def fecha2String(fechaDate, formato):
    return d.date.strftime(fechaDate, formato)

def fecha2Date(fechaString, formato):
    fecha = d.datetime.strptime(fechaString, formato)
    return d.date(fecha.year, fecha.month, fecha.day)


def diferenciaDias(fechaDate, fechaDate2):
    '''si la fechaDate es mayor que fechaDate2 devuelve un número positivo.
    Devuelve un número negativo si, por contra, fechaDate2 es más actual que fechaDate'''
    return (fechaDate - fechaDate2).days

def compararFechas(fechaDate, fechaDate2):
    esPosterior = False
    esIgual = False
    if fechaDate > fechaDate2:
        esPosterior = True
    elif fechaDate == fechaDate2:
        esIgual = True

    return esPosterior, esIgual




