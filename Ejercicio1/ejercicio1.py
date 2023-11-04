
num = int(input("Numero entre 2 y 20: ")) #Introducimos la variable num que tiene que estar en el rango

if num<2 or num>20: # Realizamos la sentencia alternativa de para que num este en el rango
    print("Error. El número está fuera de rango"
          "Tiene que estar entre 2 y 20") # Si el valor no esta en el rango determinamos el error

else: # Si el valor esta en el rango relizamos bucle
    for i in range (1, num+1):
        print(i)  #Imprimimos sucesion de números
