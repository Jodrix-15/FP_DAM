import User as u
import dates as d
from datetime import date, datetime
import requests


def menu():
    print(f"[1]. Registrar usuario\n"
          f"[2]. Login\n"
          f"[3]. Mostrar dades de un usuario\n"
          f"[4]. Salir\n")

def getInt(mensaje):
    return int(input(mensaje))

def signUp():
    '''Registramos al usuario'''
    user = ""
    password = ""

    while u.testUser(user, password) == False:
        print("\nEl usuario debe contener como mínimo 4 caracteres\n"
              "La contrasenya tiene que tener 6 carácteres y contener al menos una vocal\n")

        user = input("Usuario: ").lower()
        if user in userData:
            print("\nUsuario no disponible")
            user = ""
        else:
            password = input("Contrasenya: ")

    age = u.getAge()
    print("Fecha de nacimiento: ")
    birthDayDate = u.getBirthday()
    userData[user] = {"password": password, "edad": age, "fecha nacimiento": birthDayDate}
    print("\nUsuario registrado\n")
    input("PULSA ENTER")


def login():
    user = input("Usuario: ").lower()
    password = input("Contrasenya: ")
    if u.login(userData, user, password) == True:
        print(f"\nBienvenido {user}\n"
              f"{d.avui()}")
        nextBthDay = d.nextBirthday(userData[user]["fecha nacimiento"])

        if d.aniversari(userData[user]["fecha nacimiento"]) == False:
            print("Este mes no es el de tu cumpleanyos")
            print(f"Faltan {d.daysToGo(nextBthDay)} para tu cumpleanyos\n")

            input("PULSA ENTER")

        else:
            print("Este mes es el de tu cumpleanyos")
            if datetime.strptime(userData[user]["fecha nacimiento"], "%d/%m/%Y").day == date.today().day:
                print("FELCIDADES!!! ES TU CUMPLEANYOS\n")
                input("PULSA ENTER")
            else:
                print(f"Faltan {d.daysToGo(nextBthDay)} para tu cumpleanyos\n")
                input("PULSA ENTER")
    else:
        print("\nUsuario o Contrasenya incorrecto\n")
        input("PULSA ENTER")

def showData():
    user = input("Usuario: ")
    if user in userData:
        print(f"Datos de {user}")
        for k, v in userData[user].items():
            if k == "edad":
                print(f"{k}: {v}")
            if k == "fecha nacimiento":
                print(f"Proximo cumpleanyos: {d.nextBirthday(v)}")
        print()
    else:
        print("Usuario no encontrado\n")

    input("PULSA ENTER")



finalizar = False
userData = {}
userData["jodrix"] = {"password": "a12345", "edad": 30, "fecha nacimiento": "4/12/1993"}
userData["carlos"] = {"password": "a12345", "edad": 30, "fecha nacimiento": "14/12/1993"}
userData["anac"] = {"password": "a12345", "edad": 27, "fecha nacimiento": "9/12/1997"}
userData["sandra"] = {"password": "a12345", "edad": 29, "fecha nacimiento": "10/11/1994"}
userData["sergio"] = {"password": "a12345", "edad": 26, "fecha nacimiento": "28/2/1993"}

while finalizar == False:
    print("\nDel siguiente menu: \n")
    menu()
    opcion = getInt("Escoge una opcion: ")

    if opcion == 1:
        signUp()

    elif opcion == 2:
        login()

    elif opcion == 3:
        showData()

    elif opcion == 4:
        print("\nPrograma finalizado")
        finalizar = True

    else:
        print("\nOpción no válida")
        input("\nPULSA ENTER")












