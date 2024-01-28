import datetime as d

datosLibros = {
    "Titulo": "",
    "Autor": "",
    "Genero": "",
    "Num. Paginas": 0
}

libros = {}

alumnos = {}


def getLibros():
    return libros


def getAlumnos():
    return alumnos

def fecha2String(fecha):
    da = d.date(fecha.year, fecha.month, fecha.day)
    return d.date.strftime(da, "%d/%m/%Y")

def fecha2Date(fecha):
    da = d.datetime.strptime(fecha, "%d/%m/%Y")
    return d.date(da.year, da.month, da.day)


def addLlibre(codigo, titulo, autor, genero, numPag):
    '''codigo-titulo-genero-numPaginas'''

    datosLibros["Titulo"] = titulo
    datosLibros["Autor"] = autor
    datosLibros["Genero"] = genero
    datosLibros["Num. Paginas"] = int(numPag)
    datosLibros["Estado"] = "disponible"

    libros[codigo] = datosLibros.copy()
    print("Libro Registrado")


def startPrestec(codigoLibro, nombreAlumno, fechaInicio):
    final = fechaInicio + d.timedelta(days=+15)
    fechaFinal = fecha2String(final)

    if nombreAlumno not in alumnos:
        alumnos[nombreAlumno] = {
            "En Prestec": {
            },
            "Incidencias": []
        }

    nuevoLibro = {
        codigoLibro: {
            "Titulo": getLibros()[codigoLibro]["Titulo"],
            "Inicio": d.date.strftime(fechaInicio, "%d/%m/%Y"),
            "Fin": fechaFinal
        }
    }
    alumnos[nombreAlumno]["En Prestec"].update(nuevoLibro)
    libros[codigoLibro]["Estado"] = "En Prestec"
    print(f"Préstamo registrado. El libro se tiene que devolver: {fechaFinal}")

def listLibros():
    for id in libros:
        print(f"{id} : {libros[id]['Titulo']} , {libros[id]['Autor']}   - ESTAT: {libros[id]['Estado']}")

def maxLibros():
    aux = ""
    maxPag = 0
    for id in libros:
        for datos in libros[id]:
            if datos == "Num. Paginas":
                if libros[id]["Num. Paginas"] > maxPag:
                    maxPag = libros[id]["Num. Paginas"]
                    aux = id

    print(f"El libro con más páginas es {libros[aux]['Titulo']}, con {maxPag} páginas")

def listGenere(genero):
    cont = 0
    for id in libros:
        if libros[id]["Genero"].lower() == genero:
            print(f"{id} : {libros[id]['Titulo']} , {libros[id]['Autor']}   - ESTAT: {libros[id]['Estado']}")
            cont += 1
    if cont == 0:
        print(f"No hay ningún libro registrado del género {genero}")

def info(alumno):
    print("Libros en préstamo: ")
    librosAlumno = getAlumnos()[alumno]["En Prestec"]
    for a in getAlumnos():
        if a.lower() == alumno:
            for prestamo in librosAlumno:
                print(f"Libro: {prestamo} - {librosAlumno[prestamo]['Titulo']}\t Fecha_Inicio: {librosAlumno[prestamo]['Inicio']}\t Fecha_Fin: {librosAlumno[prestamo]['Fin']}")

def stats():
    numLibros = len(getLibros())
    numIncidencias = 0
    for a, v in getAlumnos().items():
        numIncidencias += len(v["Incidencias"])

    paginasTotales = 0
    for l, v in getLibros().items():
        paginasTotales += v["Num. Paginas"]

    mediaPaginas = paginasTotales / len(getLibros())
    print(f"Número de libros registrados: {numLibros}\n"
          f"Número de incidencias registradas: {numIncidencias}\n"
          f"Media de páginas por libro: {mediaPaginas}")

def endPrestec(codigoLibro, alumno, fechaInicio, fechaFin, fechaDevuelto):

    if fechaDevuelto > fechaFin:
        print("Has devuelto el libro fuera de plazo")
        getAlumnos()[alumno]["Incidencias"].append(f"Libro: {codigoLibro}\t Fecha_Inicio: {fecha2String(fechaInicio)}\t Fecha_Fin: {fecha2String(fechaFin)}\t Fecha_Retorno: {fecha2String(fechaDevuelto)}")

    getLibros()[codigoLibro]["Estado"] = "disponible"
    getAlumnos()[alumno]["En Prestec"].pop(codigoLibro)
    print("El libro ha quedado disponible")

def listPrestec():

    for codigo, valores in getLibros().items():
        if valores["Estado"] == "En Prestec":
            for alumno, datos in getAlumnos().items():

                if codigo in datos["En Prestec"]:

                    if d.date.today() > fecha2Date(datos['En Prestec'][codigo]["Fin"]):
                        print(f"Libro: {codigo} - {valores['Titulo']} - Alumno: {alumno} - Fecha_Inicio: {datos['En Prestec'][codigo]['Inicio']} - Fecha_Fin: {datos['En Prestec'][codigo]['Fin']} - * FUERA DE PLAZO *")
                    else:
                        print(f"Libro: {codigo} - {valores['Titulo']} - Alumno: {alumno} - Fecha_Inicio: {datos['En Prestec'][codigo]['Inicio']} - Fecha_Fin: {datos['En Prestec'][codigo]['Fin']}")









# addLlibre()
# listLibros()
# maxLibros()
