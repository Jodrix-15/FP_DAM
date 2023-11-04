import  random

numRandom = random.randint(-10,10) #generamos un número random de -10 a 10

numPositivos = 0
numNegativos = 0
numTotales = 0

while numRandom != 0: #el bucle se ejecuta mientras no sea 0
    #en los siguientes casos señalamos los números positvos y negativos
    if numRandom > 0:
        numPositivos += 1
        print(numRandom, "es un número positivo")

    elif numRandom < 0:
        numNegativos += 1
        print(numRandom, "es un número negativo")

    numTotales += 1
    numRandom = random.randint(-10, 10)

print(f"\nNumeros positivos: {numPositivos}\n"
      f"Numeros negativos: {numNegativos}\n"
      f"Numeros generados: {numTotales+1}")
