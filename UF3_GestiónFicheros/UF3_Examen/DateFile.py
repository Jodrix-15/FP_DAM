#En este archivo he puesto todas las funciones que manipulan fechas

import datetime as d


'''Retorna la fecha actual'''
def hoy():
    return d.date.today()

'''Recibe como argumentos una fecha tipo Date y el formato de la misma.
Retorna la fecha en tipo String con el formato pasado por argumento'''
def fecha2String(fechaDate, formato):
    return d.date.strftime(fechaDate, formato)

'''Recibe como argumentos una fecha tipo String y el formato de la misma.
Retorna la fecha en tipo Date'''
def fecha2Date(fechaString, formato):
    fecha = d.datetime.strptime(fechaString, formato)
    return d.date(fecha.year, fecha.month, fecha.day)


'''Recibe como argumentos una fecha tipo Date y una cantidad de días.
Retorna la suma de ambos como una nueva fecha'''
def sumarDias(fechaDate, numDias):
    return fechaDate + d.timedelta(days=numDias)


'''si la fechaDate es más actual que fechaDate2 devuelve un número positivo.
Devuelve un número negativo si, por contra, fechaDate2 es más actual que fechaDate'''
def diferenciaDias(fechaDate, fechaDate2):
    return (fechaDate - fechaDate2).days


'''Recibe como argumento dos fechas (tipo Date) y las compara.
Si fechaDate es más actual que fechaDate2 devuelve (True, False)
Si fechaDate es más antigua que fechaDate2 devuelve (False, False)
Si son iguales devuelve (False, True)'''
def compararFechas(fechaDate, fechaDate2):
    esPosterior = False
    esIgual = False
    if fechaDate > fechaDate2:
        esPosterior = True
    elif fechaDate == fechaDate2:
        esIgual = True

    return esPosterior, esIgual
