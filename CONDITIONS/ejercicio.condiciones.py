import sys
#variables de numeros
try:
    numero1 = int(input("introduzca un primer numero: "))
    numero2 = int(input("introduzca un segundo numero: "))
except:
    print("alguno de los numeros no se ha convertido")
if numero1 == numero2:
    print(numero1, "==", numero2)
elif numero1 != numero2:
    print(numero1, "!=", numero2)
