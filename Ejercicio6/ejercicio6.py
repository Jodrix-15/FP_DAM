
print("Hola Alba! introdueix el temps dels trams en minuts. Indica -1 per finalitzar.\n")
minutos = 0
numTramos = 0
suma = 0
while minutos != -1: #mientras el dato sea diferente -1 se ejecuta el bucle
    minutos = int(input(f"Tram {numTramos +1}: "))
    if minutos > 0: #si es mayor que 0 sumamos los minutos si no, no
        if minutos != -1:
            suma += minutos
            numTramos += 1
    else: #errores
        if minutos != -1:
            print("El número no puede ser negativo o cero")


horas = suma//60 #horas enteras
minutos = suma%60 #el resto nos da los minutos sobrantes

print(f"Temps total caminat: {horas} hores {minutos} minuts\n"
      f"Total trams {numTramos}")



