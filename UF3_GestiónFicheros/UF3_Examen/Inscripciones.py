import FileManager as f
import DateFile as d


AIF = "AIF"
TIL = "TIL"
MIN = "MIN"
DAM = "DAM"
ASIC = "ASIC"
SUMA_NOTAS = "SUMA_NOTAS"
INSCRITOS = "INSCRITOS"
NOTA_MEDIA = "NOTA_MEDIA"

diccMedias = {}
subDiccMedias = {
    SUMA_NOTAS: 0,
    INSCRITOS: 0,
    NOTA_MEDIA: 0
}


def alta(dni, grado, nota, fecha):

    lineas = f.getDatos()
    if dni in lineas:
        print("El alumno ya está registrado")
    else:
        f.escribir(f"{dni}/{grado}/{nota}/{fecha}")
        print("Alumno registrado correctamente")


def baixa(dni):
    inscripciones = f.getDatos()
    if len(inscripciones) == 0:
        print("No hay ningún alumno inscrito")
    else:
        if dni in inscripciones:
            inscripciones.pop(dni)
            f.actualizar(inscripciones)
            print("Alumno dado de baja correctamente")
        else:
            print(f"ERROR. No hay ningún alumno inscrito con el DNI: {dni}")

def llistat(ciclo):

    inscripciones = f.getDatos()
    PLAZAS_TOTALES = 30
    alumnosInscritos = 0
    alumnosTotales = 0
    if len(inscripciones) == 0:
        print("No hay ningún alumno inscrito")
    else:
        for dni, valores in inscripciones.items():

            if valores[f.GRADO] == ciclo.upper():
                alumnosInscritos += 1
            alumnosTotales += 1

        if alumnosInscritos > PLAZAS_TOTALES:
            plazas = alumnosInscritos - PLAZAS_TOTALES
            print(f"No quedan más plazas disponibles. Hay un total de {plazas} de más")
        elif alumnosInscritos == PLAZAS_TOTALES:
            plazas = PLAZAS_TOTALES
        else:
            plazas = PLAZAS_TOTALES - alumnosInscritos


        for dni, valores in inscripciones.items():
            if ciclo == "*":
                print(f"{valores[f.FECHA]}\t{dni}\t{valores[f.NOTA]}\t{valores[f.GRADO]}")
                inscritos = f"Nº total de inscripciones: {alumnosTotales}"

            elif plazas <= 30:
                if valores[f.GRADO] == ciclo:
                    print(f"{valores[f.FECHA]}\t{dni}\t{valores[f.NOTA]}")
                    inscritos = (f"Nº total de inscripciones: {alumnosInscritos}\n"
                                 f"Todavía quedan {plazas} disponibles")
        print(inscritos)


def mitjana():
    inscripciones = f.getDatos()
    ciclosValidos = ["AIF", "TIL", "MIN", "DAM", "ASIC"]

    hoy = d.hoy()
    fechaString = d.fecha2String(hoy, "%d/%m/%Y")
    fechaHora = fechaString + "\t" + d.horaActual()

    print(f"Medias a: {fechaHora}")

    for ciclo in ciclosValidos:
        if ciclo not in diccMedias:
            diccMedias[ciclo] = subDiccMedias.copy()

    for dni, valores in inscripciones.items():
        grado = valores[f.GRADO]

        diccMedias[grado][SUMA_NOTAS] += float(valores[f.NOTA])
        diccMedias[grado][INSCRITOS] += 1

    for grado, valores in diccMedias.items():
        if diccMedias[grado][INSCRITOS] > 0:
            diccMedias[grado][NOTA_MEDIA] = diccMedias[grado][SUMA_NOTAS] / diccMedias[grado][INSCRITOS]

        if valores[INSCRITOS] == 0:
            print(f"{grado}\t No hay ningún alumno inscrito en este ciclo")
        else:
            print(f"{grado}\t{diccMedias[grado][NOTA_MEDIA]}")

    f.escribirMedias(fechaHora, diccMedias)


def stats():
    print(f"***      ESTADISTICAS INSCRIPCIONES CALAMOT      ***")
    inscripciones = f.getDatos()
    if len(inscripciones) > 0:
        print("Inscripción más antigua: ")
        print(inscripcionStats(inscripciones))
        print("Inscripción con la nota más alta:")
        notaAlta(inscripciones)
        print("Inscripción con la nota más baja:")
        notaBaja(inscripciones)
    else:
        print("No hay ningún alumno inscrito")


def inscripcionStats(inscripcionesDicc):

    fechaMasAntigua = d.hoy()
    for dni, valores in inscripcionesDicc.items():
        fecha = d.fecha2Date(valores[f.FECHA], "%d-%m-%Y")
        if not d.compararFechas(fecha, fechaMasAntigua)[0] or d.compararFechas(fecha, fechaMasAntigua)[1]:
            fechaMasAntigua = fecha
            auxDni = dni
            ciclo = valores[f.GRADO]
            nota = valores[f.NOTA]
            dias = d.diferenciaDias(d.hoy(), fechaMasAntigua)

    return (f"Fecha: {d.fecha2String(fechaMasAntigua, '%d-%m-%Y')}\n"
      f"DNI: {auxDni}\tCiclo: {ciclo}\tNota: {nota}\n"
      f"Han pasado {dias} dias\n"
      f"****************************************************************")

def notaAlta(inscripcionesDicc):
    i = 0
    for dni, valores in inscripcionesDicc.items():
        if i == 0:
            masAlta = valores[f.NOTA]
            auxDni = dni
            ciclo = valores[f.GRADO]
            fecha = valores[f.FECHA]


        if valores[f.NOTA] > masAlta:
            masAlta = valores[f.NOTA]
            auxDni = dni
            ciclo = valores[f.GRADO]
            fecha = valores[f.FECHA]


    print(f"Nota: {masAlta}\n"
          f"DNI: {auxDni}\tCiclo: {ciclo}\tFecha: {fecha}\n"
          f"****************************************************************")

def notaBaja(inscripcionesDicc):

    i = 0
    masBaja = 0
    for dni, valores in inscripcionesDicc.items():
        if i == 0:
            masBaja = valores[f.NOTA]
            auxDni = dni
            ciclo = valores[f.GRADO]
            fecha = valores[f.FECHA]
        else:
            if valores[f.NOTA] < masBaja:
                masBaja = valores[f.NOTA]
                auxDni = dni
                ciclo = valores[f.GRADO]
                fecha = valores[f.FECHA]
        i = 1

    print(f"Nota: {masBaja}\n"
          f"DNI: {auxDni}\tCiclo: {ciclo}\tFecha: {fecha}\n")




