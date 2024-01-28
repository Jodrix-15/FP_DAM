
numCanastas = int(input())
puntosLocal = 0
puntosVisitante = 0
for i in range(numCanastas):
    equipo= input() #pediomos local visitante
    puntuacion = int(input())
    while puntuacion < 1 or puntuacion >3: #si la puntuacion es menor que cero volvemos a preguntar
        print("Pon un numero 0 o mayor")
        puntuacion = int(input())
    if equipo == "L":
        puntosLocal += puntuacion
    else:
        puntosVisitante += puntuacion

if puntosLocal == puntosVisitante:
    print(f"E {puntosLocal} {puntosVisitante}")
elif puntosLocal > puntosVisitante:
    print(f"L {puntosLocal} {puntosVisitante}")
else:
    print(f"V {puntosLocal} {puntosVisitante}")
