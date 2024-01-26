
letra = input()
a = -1
b = -1
while letra != "D": #mientras sea diferente de D se ejecuta
    if letra == "A":
        a = int(input("Introduce un número entre 0 y 10: "))
    elif letra == "B":
        b = int(input("Introduce un número entre 0 y 10: "))
    elif letra == "C":
        if a != -1 and b != -1:
            if a > b:
                print("ERROR")
            for i in range(a, b + 1):
                print(i)
        else:
            print("ERROR")
    letra = input()
print("BYE")