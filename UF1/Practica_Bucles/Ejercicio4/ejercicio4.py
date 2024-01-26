num = int(input("Introduce un número entre 2 y 30: "))
while num < 2 or num >  30: #si esta fuera rango que vuelva a pedir el dato
    num = int(input("Error, debes introducir un número entre 2 y 30: "))
suma = 0
for i in range(num, -1, -1): #sumatoria en revertida para que se muestren así los numeros
    suma += i #sumatoria
    if i > 1:
        print(i, end=" + ")
    elif i == 1:
        print(i, end=" =") #establecemos condiciones para los signos
print(f" {suma}")


