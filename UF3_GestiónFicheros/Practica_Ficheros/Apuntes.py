import os
import sys

alumnos = {}
nombre_carpeta = "pesados"
ruta_archivo = "./" + nombre_carpeta + "/notas.txt"

if os.path.exists(nombre_carpeta):
    if os.path.exists(ruta_archivo):
        with open (ruta_archivo, "r") as file:
            lineas = file.readline()
            file.close()
            for linea in lineas:
                nombre = linea[0]
                nota = linea[1]
                nota = int(nota)
                alumnos[nombre] = nota
    else:
        os.mkdir(nombre_carpeta)

    comando = sys.argv
    if len(comando) >1:
        if len(comando)==2:
            if comando[1].lower() == "list":
                if len(alumnos)==0:
                    print("No hay alumnos registrados")
                else:
                    for nombre in alumnos:
                        print(nombre, "-", alumnos[nombre])
            else:
                print("Comando incorrecto")
        elif len(comando) == 3:
            nombre = comando[1]
            nota = int(comando[2])
            if nombre not in alumnos:
                alumnos[nombre] = nota
                with open(ruta_archivo, "a") as file:
                    file.write(nombre + "-" + str(nota) + "\n")
                    file.close()
    else:
        print("uso fitxers.py nombre_alumno nota (para añadir alumno")
        print("uso fitxers.py list")