import random
numList = []

for i in range(30): #ejecutamos el bucle 30 veces
    numRandom = random.randint(0, 29) #asignamos a numRandom un número random entre 0 y 29
    numList.append(numRandom)#añadimos numRandom a la lista numList
    print(numRandom, end=" ")

print()
contador = 0
for i in range(len(numList)): #ejecutamos el bucle tantas veces como elementos tiene la lista numList
    if i == numList[i]: #si la posición i es igual al valor de la lista en la posición i, imprimimos la siguiente linea
        print(f"El número {numList[i]} está en la posición {i}")
        contador = 1

if contador == 0: #si el contador es 0, significa que no lo anterior no se ha cumplido en ningún momento
    print("No hay ningún número que coincida con su posición")

