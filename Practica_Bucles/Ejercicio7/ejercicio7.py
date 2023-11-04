
pisoPequeño = int(input("Introduce el piso más pequeño: "))

pisoAlto = int(input("Introduce el piso más alto: "))

pisoActual = int(input("Introduce el piso actual: "))#miramos que el piso este comprendido en el rango

numCambioPiso = 0
desplazamiento = 0
piso = input()
error = False
while piso != "X": #bucle se ejecuta mientras el usuario no marque X


    if int(piso) >= pisoPequeño and int(piso) <= pisoAlto: #si el piso esta en el rango correcto calcula el desplazamiento, numero de cambios y piso actual
        if int(piso) != pisoActual:
            numCambioPiso += 1


        desplazamiento += abs(int(piso) - pisoActual)
        pisoActual = int(piso)

    else:
        error=True

    piso = input() #lo ponemos para que el bucle no sea infinito

if error == True:
    print(f"{numCambioPiso} {desplazamiento} {pisoActual} E")

else:

    print(f"{numCambioPiso} {desplazamiento} {pisoActual}")





