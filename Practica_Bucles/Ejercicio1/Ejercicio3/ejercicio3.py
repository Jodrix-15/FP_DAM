
cantidadNumeros = int(input("introduce un número: ")) # Introducimos el la primera variable de cantidad de veces a ejecutar
if cantidadNumeros <= 0: # Si el valor no esta en el rango imprimimos error
    print("Error, debe ser un número entero positivo")

numMayor= -100
numMenor = 0 # Establecemos variables para numeros y suma de estos
suma = 0
i = 0;
while i < cantidadNumeros: #se ejecutar el bucle el numeo de cantidad de numeros
    print(i+1, ". Introduce número: ", end= " ")
    num = int(input())
    suma += num #suma total de numeros
    if num < -100 or num>100: #si el número esta fuera de rango marcamos un error y le restamos 1 a i
        print("El número está fuera de rango. "
              "Debe estar entre -100 y 100)")
        i -= 1
    else: #si el rango esta bien
        if i == 0:
            numMenor = num
        if num > numMayor:
            numMayor = num
        elif num < numMenor:
            numMenor = num
        i += 1

if cantidadNumeros > 0:
    media = suma / cantidadNumeros #calulamos la media
    print(f"numero mayor: {numMayor}, numero menor: {numMenor}, media: {media}")

