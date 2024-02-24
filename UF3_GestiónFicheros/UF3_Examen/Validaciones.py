#En este archivo he puesto todas las funciones que verifican si un dato se ha introducido correctamente o no.

import DateFile as d
import Inscripciones as i

def valAlta(comandos):
    dniVal, grauValido, notaValida, fechaValida = False, False, False, False
    if correctArgumentos(comandos, 4):
        if dniValido(comandos[0]):
            dniVal = True
            if cicloValido(comandos[1].upper()):
                grauValido = True
                if notaAprobada(float(comandos[2])):
                    notaValida = True
                    if d.compararFechas(d.hoy(), d.fecha2Date(comandos[3], "%d-%m-%Y"))[0]:
                        fechaValida = True
                    else:
                        print("ERROR. La fecha tiene que ser anterior o igual a hoy")

        if dniVal and grauValido and notaValida and fechaValida:
            i.alta(comandos[0].upper(), comandos[1].upper(), comandos[2], comandos[3])


def valBaixa(comandos):
    if correctArgumentos(comandos, 1):
        if dniValido(comandos[0]):
            i.baixa(comandos[0].upper())

def valLlistat(comandos):
    if correctArgumentos(comandos, 1):
        if cicloValido(comandos[0].upper()) or comandos[0].upper() == "*":
            i.llistat(comandos[0].upper())

def valMitjana(comandos):
    if correctArgumentos(comandos, 0):
        i.mitjana()

def valStats(comandos):
    if correctArgumentos(comandos, 0):
        i.stats()
def cicloValido(nombreCiclo):
    ciclosValidos = ["AIF", "TIL", "MIN", "DAM", "ASIC"]
    esValido = False
    if nombreCiclo in ciclosValidos:
        esValido = True
    else:
        if nombreCiclo != "*":
            print(f"El ciclo '{nombreCiclo}' no es válido")

    return esValido

def notaAprobada(nota):
    esAprobado = False
    if 10 >= nota >= 5:
        esAprobado = True
    else:
        print("La nota debe estar entre 5 y 10 (ambas incluidas)")

    return esAprobado


'''Recibe una lista de comandos y, si tiene el número correcto de elementos, devuelve True.
De lo contrario devuelva False.'''
def valExit(comandos):
    return correctArgumentos(comandos, 1)


'''Recibe como argumentos una lista de elementos y el número de elementos que
debería tener dicha lista. Retorna True si la longitud de la lista es igual al
número de elementos. De lo contrario, retorna False'''
def correctArgumentos(comList, numArguments):
    isCorrect = True
    if len(comList) != numArguments:
        print("ERROR. Nº de argumentos incorrecto")
        isCorrect = False
    return isCorrect


'''Recibe como argumento un string y comprueba si el valor es numérico (0 o positivo)
Retorna True si se cumple la condición anterior, y False si no la cumple'''
def isNum(string):
    esNumero = True
    if not string.isnumeric():
        print("ERROR. Debe ser un número que no sea negativo")
        esNumero = False
    return esNumero


'''Recibe un número como parámetro y devuelve True si el número es >= 1.
Devuelve False si el número es menor que 1'''
def numPositivo(num):
    esPositivo = True
    if num < 1:
        print("ERROR. Debe ser un número mayor o igual a uno")
        esPositivo = False
    return esPositivo


'''Esta función recibe un STRING como argumento y comprueba si es un DNI válido. Devuelve True si es así, y False
si no lo es'''
def dniValido(dniString):
    esValido = False
    validLetters = "TRWAGMYFPDXBNJZSQVHLCKE"

    if len(dniString) == 9:
        if isNum(dniString[0:7]) and (dniString[-1].upper() in validLetters):
            num = int(dniString[0:8])

            letter = dniString[-1].upper()
            resto = num%23
            if letter == validLetters[resto]:
                esValido = True
            else:
                print("La letra del DNI no es válida")
        else:
            print("El formato del DNI debe ser '12345678X'")
    else:
        print("ERROR. El DNI debe contener 8 números y una letra al final")

    return esValido

