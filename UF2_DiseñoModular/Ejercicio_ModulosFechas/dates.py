import locale
from datetime import date as d, datetime as dt
import User as u
locale.setlocale(locale.LC_ALL, 'ca_ES.UTF-8')
def avui():
    avui = d.today()
    return avui.strftime("Avui es: %d de %B del %Y")

def aniversari(date):
    '''Retorna True si el mes de la fecha (fecha de nacimiento) que se le pasa por parámetro es
    igual al mes de la fecha actual'''

    sameMonth = False

    date = dt.strptime(date, "%d/%m/%Y")
    todayDate = d.today()

    if date.month == todayDate.month:
        sameMonth = True

    return sameMonth

def nextBirthday(date):
    '''Recibe como argumento la fecha de nacimiento y calcula la fecha del próximo cumpleaños'''

    birthDate = dt.strptime(date, "%d/%m/%Y")
    year = d.today().year

    if aniversari(date):
        if d.today().day >= birthDate.day:
            year += 1
    else:
        if d.today().month > birthDate.month:
            year += 1

    next = d(year, birthDate.month, birthDate.day)
    return next.strftime("%d/%m/%Y")

def daysToGo(date):
    '''Recibe como argumento la fecha del próximo aniversario y la compara con la fecha actual.
    Retorna los dias que faltan para tu próximo cumpleaños'''

    todayDate = d.today()
    date = dt.strptime(date, "%d/%m/%Y")
    date = d(date.year, date.month, date.day)

    dias = (date - todayDate).days

    return f"{dias} dias"









