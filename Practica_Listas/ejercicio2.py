import random

num = int(input("Introduce un número entre 10 y 50: "))

while num<10 or num>50: #se ejecuta el bucle mientras el usuario no ponga un número dentro del rango
    num = int(input("ERROR. Número fuera de rango. Debe estar entre 10 y 50: "))

listaNums = []
for i in range(num):# se ejecuta num veces
    numRandom = random.randint(1, 4)#genera un numero random entre 1 y 4 y se asigna a numRandom
    listaNums.append(numRandom)#añadimos numRandom a la listaNums
    print(numRandom, end=" ")

#contamos los numeros, 1, 2, 3 y 4 que tiene la insta
listaNums.sort()

numMasRepetido = 0
numRepeticiones = 0
numRepeticionesAux = 0

for v in listaNums: #recorremos la listaNums
    if v != numMasRepetido: #comprueba si el valor actual v de la listaNums es diferente al número más repetido
        numRepeticions = listaNums.count(v) #contamos cuántas veces aparece v en la listaNums
        if numRepeticions > numRepeticionesAux: #comprueba si el num actual se repite más veces que el anterior número con más repeticiones
            numMasRepetido = v #si la condición se cumple, el num más repetido, será el valor actual v
            numRepeticionesAux = listaNums.count(numMasRepetido) #el número de repeticiones será el del número más repetido

print(f"\nEl número que ha salido más veces es el {numMasRepetido} con {numRepeticionesAux} repeticiones")
suma = 0
for n in listaNums: #recorremos la lista y sumamos sus valores
    suma += n

media = suma / len(listaNums)
print("La media de los números es: ", media)
