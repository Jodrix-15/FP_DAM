#En este archivo he usado funciones que manejan las misiones de las expediciones

import fechas as fe

misiones = {} #He usado un diccionario para acceder fácilmente a los datos. Abajo hay un ejemplo de la estructura que tiene el diccionario

'''misiones = {
    "aprobarexamen": {
        "lugar": "calamot",
        "fecha": "3-2-2024"
    },
    "adios": {
        "lugar": "mi casa",
        "fecha": "4-2-2024"
    },
    "hola": {
        "lugar": "mi salón",
        "fecha": "3-2-2024"
    },
    "excursion": {
        "lugar": "prince of persia",
        "fecha": "9-2-2024"
    }
}'''

def registrar(mision, lugar, fecha):
    if mision not in misiones:
        misiones[mision] = {}
        misiones[mision]["lugar"] = lugar
        misiones[mision]["fecha"] = fecha
        print("Misión añadida con éxito")
    else:
        print(f"La misión '{mision}' ya está registrada en la base de datos")

def eliminar(mision):
    if mision not in misiones:
        print(f"La mision '{mision}' no existe")
    else:
        misiones.pop(mision)
        print("Mision eliminada con éxito")

def list(anyo):
    print(f"AÑO {anyo}")
    contador = 0
    for mision, f in misiones.items():
        fecha = fe.fecha2Date(f['fecha'], '%d-%m-%Y')
        if fecha.year == int(anyo):
            print(f"{fe.fecha2String(fecha, '%d-%m-%Y')}\t{mision}")
            contador += 1

    if contador == 0:
        print("No hay ninguna misión en el año indicado")

def setmana():
    print("SEMANA")
    contador = 0
    fechaHoy = fe.hoy()
    for mision, f in misiones.items():
        fechaMision = fe.fecha2Date(f["fecha"], "%d-%m-%Y")
        if 0 <= fe.diferenciaDias(fechaMision, fechaHoy) <= 7:
            if fe.diferenciaDias(fechaMision, fechaHoy) == 0:
                print(f"=> * AVUI *\t\tMisión: {mision}\tLugar: {f['lugar']}")
            elif fe.diferenciaDias(fechaMision, fechaHoy) == 1:
                print(f"=> * DEMÀ *\t\tMisión: {mision}\tLugar: {f['lugar']}")
            else:
                print(f"{fe.fecha2String(fechaMision, '%d-%m-%Y')}:\t\tMisión: {mision}\tLugar: {f['lugar']}")
            contador += 1

    if contador == 0:
        print("No hay ninguna misión para la próxima semana")

def primera():
    print("PRIMERA")
    i = 0
    fechaHoy = fe.hoy()
    misionAntigua = ""
    for mision, f in misiones.items():
        if i == 0:
            fechaMasAntigua = fe.fecha2Date(f["fecha"], "%d-%m-%Y")
        fecha = fe.fecha2Date(f["fecha"], "%d-%m-%Y")
        if not fe.compararFechas(fecha, fechaMasAntigua)[0]:
            fechaMasAntigua = fecha
            misionAntigua = mision
        i = 1

    print(f"La misión más antigua es: {misionAntigua}\n"
          f"Lugar: {misiones[misionAntigua]['lugar']}\n"
          f"Fecha: {fe.fecha2String(fechaMasAntigua, '%d-%m-%Y')}")

    if fe.diferenciaDias(fechaHoy, fechaMasAntigua) == 0:
        print("La misión es hoy")
    elif fe.diferenciaDias(fechaHoy, fechaMasAntigua) > 0:
        print(f"Han pasado {fe.diferenciaDias(fechaHoy, fechaMasAntigua)} días")
    else:
        print(f"Quedan {abs(fe.diferenciaDias(fechaHoy, fechaMasAntigua))} días para llevar a cabo la misión")








