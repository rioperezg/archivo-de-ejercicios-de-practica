from ast import Try
import sys
#numero1
numero1 = int(input("introduzca un primer numero: "))
try:
    numero1 = int(numero1)

except:
    print("uno de los numeros no se ha convertido")

#numero2
numero2 = int(input("introduzca un segundo numero: "))
try:
    numero2 = int(numero2)
except ValueError as e:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()
    

comparacion = numero1 < numero2

print(numero1, "<", numero2, ":", comparacion)
