import sys
#ejecutar codigo con try
try:
    numero1 = int(input("introduzca un primer numero: "))
    numero2 = int(input("introduzca un segundo numero: "))
#declarar excepcion
except:
   print("alguno de los numeros no se ha convertido correctamente")
#realizar la comparacion
if numero1 <= numero2:
    print(numero1, "<=", numero2)
elif numero1 >= numero2:
    print(numero1, ">=", numero2)
else:
    print(numero1,"==", numero2)