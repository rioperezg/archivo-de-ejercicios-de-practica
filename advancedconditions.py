import sys
#declaracion de variables, en este caso separamos el try de la variable
try:
   numero1 = int(input("introduzca un primer numero entre 0 y 10: "))
   numero2 = int(input("introduzca un sefgundo numero entre 0 y 10: "))
   
except:
   print("alguno de los numeros no se ha convertido correctamente")
#y por ultimo declaramos las condiciones
if 0 < numero1 < 11:
    print("el primer numero esta comprendido entre 0 y 10")
if 1 <= numero2 <= 10:
    print("el segundo numero esta comprendido entre 0 y 10")