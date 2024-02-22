#En este archivo he puesto todas las funciones que verifican si un dato se ha introducido correctamente o no.


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
        print("ERROR. Debe contener 8 números y una letra al final")

    return esValido