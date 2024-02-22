#En esté módulo creo las funciones necesarias para validar que los argumentos que le enviamos
#sean correctos y lógicos

import Hotel as h

'''Esta función recibe una lista con los mismos argumentos que recibe el main (excepto el de índice = 0)
 y comprueba que todos ellos sean correctos y lógicos. Si todos están bien llamará a la función "añadir habitacion"'''
def valAnyadirHab(comandos):
   habCorrecta = False
   capCorrecta = False
   precioCorrecto = False

   if correctArgumentos(comandos, 5):
        if isNum(comandos[2]):
            if numPositivo(int(comandos[2]), "Número habitación incorrecto. Tiene que ser mayor que 0"):
                habCorrecta = True

        if isNum(comandos[3]):
            if numPositivo(int(comandos[3]), "Capacidad incorrecta. Tiene que ser mayor que 0"):
                capCorrecta = True

        if numPositivo(float(comandos[4]), "Precio Incorrecto. Tiene que ser mayor que 0"):
            precioCorrecto = True

        if habCorrecta and capCorrecta and precioCorrecto:
            h.anyadirHabitacion(comandos[2], comandos[3], comandos[4])

'''Esta función recibe una lista con los mismos argumentos que recibe el main (excepto el de índice = 0)
 y comprueba que todos ellos sean correctos y lógicos. Si todos están bien llamará a la función "añadir reserva"'''
def valAnyadirReserva(comandos):
    habValida, dniValid, telefenoValido = False, False, False

    if correctArgumentos(comandos, 7):
        if isNum(comandos[2]):
            if numPositivo(int(comandos[2]), "Número habitación incorrecto. Tiene que ser mayor que 0"):
                habValida = True

        if isNum(comandos[-1]):
            if len(comandos[-1]) == 9:
                telefenoValido = True
            else:
                print("El número debe contener 9 números")

        if dniValido(comandos[-2]):
            dniValid = True

        if dniValid and telefenoValido and habValida:
            h.anyadirReserva(comandos[2], comandos[3].capitalize(), comandos[4].capitalize(), comandos[5].upper(), comandos[6])

'''Esta función recibe una lista con los mismos argumentos que recibe el main (excepto el de índice = 0)
 y comprueba que todos ellos sean correctos y lógicos. Si todos están bien llamará a la función "reservasList"'''
def valReservasList(comandos):

    if correctArgumentos(comandos, 1):
        h.reservasList()

'''Esta función recibe una lista con los mismos argumentos que recibe el main (excepto el de índice = 0)
 y comprueba que todos ellos sean correctos y lógicos. Si todos están bien llamará a la función "habList"'''
def valHabList(comandos):

    if correctArgumentos(comandos, 1):
        h.habList()

'''Esta función recibe una lista con los mismos argumentos que recibe el main (excepto el de índice = 0)
 y comprueba que todos ellos sean correctos y lógicos. Si todos están bien llamará a la función "añadir habitacion"'''
def valInfo(comandos):
    if correctArgumentos(comandos, 2):
        if dniValido(comandos[1]):
            h.infoCliente(comandos[1].upper())

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

'''Esta función recibe una lista con los mismos argumentos que recibe el main (excepto el de índice = 0)
 y comprueba que todos ellos sean correctos y lógicos. Si todos están bien llamará a la función "finalizar"'''
def valFinalizar(comandos):
    habValida, numDiasValid = False, False

    if correctArgumentos(comandos, 3):
        if isNum(comandos[1]):
            if numPositivo(int(comandos[1]), "Número habitación incorrecto. Tiene que ser mayor que 0"):
                habValida = True

        if isNum(comandos[2]):
            numDiasValid = True

        if habValida and numDiasValid:
            h.finalizar(comandos[1], comandos[2])

'''Esta función recibe una lista con los mismos argumentos que recibe el main (excepto el de índice = 0)
 y comprueba que todos ellos sean correctos y lógicos. Si todos están bien llamará a la función "limpiar"'''
def valLimpiar(comandos):

    if correctArgumentos(comandos, 2):
        if isNum(comandos[1]):
            if numPositivo(int(comandos[1]), "Número habitación incorrecto. Tiene que ser mayor que 0"):
                h.limpiar(comandos[1])


'''Esta función recibe una lista de comandos y la longitud que debería tener la misma. Devuelve TRUE si 
coinciden, y False si no lo hacen'''
def correctArgumentos(comList, numArguments):
    isCorrect = True
    if len(comList) != numArguments:
        print("ERROR. Nº de argumentos incorrecto")
        isCorrect = False

    return isCorrect


'''Esta función recibe un string y comprueba si es un numero >= 0. Devuelve True si se cumple esa condición
y False si no la cumple'''
def isNum(string):
    esNumero = True
    if not string.isnumeric():
        print("ERROR. Debe ser un número que no sea negativo")
        esNumero = False

    return esNumero

'''Esta función recibe un número entero y comprueba si es un numero >= 1. Devuelve True si se cumple esa condición
y False si no la cumple'''
def numPositivo(num, msj):
    esPositivo = True
    if num < 1:
        print(msj)
        esPositivo = False

    return esPositivo



