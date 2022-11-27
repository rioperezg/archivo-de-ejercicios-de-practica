#asginacion de variables con try de forma conjunta
try:
    numero1 = int(input("introduzca un numero entre 0 y 10: "))
except:
    numero1 = 0
#introducimos el bucle iterativo
while not 0 < numero1 < 10:
    try:
        numero1 = int(input("introduzca un numero entre 0 y 10: "))
    except:
        numero1 = 0
print("estamos seguros de que el numero", numero1, "esta comprendido entre 0 y 10")