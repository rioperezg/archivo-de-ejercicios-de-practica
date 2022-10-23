import random
numero = random.randint(0,100)
print(numero)
intento = input("introduzca un numero: ")
intento = int(intento)
while not 0 < intento < 100:
    intento = input("introduzca un numero: ")
    intento = int(intento)

if  intento < numero:
      print("demsiado pequeño")
elif intento > numero:
      print("demasiado grande")
else:
      print("ha ganado")

     

      


