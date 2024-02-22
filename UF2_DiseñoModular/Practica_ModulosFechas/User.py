import datetime
from datetime import *

def getAge():
    age = int(input("Edad: "))

    while age<0 or age >130:
        print("ERROR. La edad debe estar entre 0 y 130")
        age = int(input("Edad: "))

    return age

def testUser(user, password):
    #valida si el usuario y contraseña son válidos
    validUser = False
    validPassword = False
    allValid = False

    vocales = "aeiou"
    numVocales = 0

    if len(user) >= 4:
        validUser = True
        if len(password) == 6:

            for chr in password:
                if chr.lower() in vocales:
                    numVocales += 1

            if numVocales >= 1:
                validPassword = True

    if validUser == True and validPassword == True:
        allValid = True

    return allValid

def getBirthday():

    yearValid = False
    monthValid = False
    dayValid = False
    monthDays =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while yearValid == False:
        year = int(input("Año (1900-2021): "))
        if 1900 <= year <= 2021:
            yearValid = True

    while monthValid == False:
        month = int(input("Mes (1-12): "))
        if 1 <= month <= 12:
            monthValid = True

    while dayValid == False:

        day = int(input(f"Dia (1-{monthDays[month-1]}): "))
        if 1 <= day <= monthDays[month-1]:
            dayValid = True

    d = date(year, month, day) #después de pedir todos los datos, lo convertimos en tipo date
    return d.strftime("%d/%m/%Y")

def login(userData, user, password):
    inUserData = False

    if user in userData:
        if userData[user]["password"] == password:
            inUserData = True

    return inUserData




