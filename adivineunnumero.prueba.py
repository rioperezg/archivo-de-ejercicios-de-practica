#parte1: hacer que el usuario introduzca un numero, y comrprobar que sea entero y ademas comprendido entre 0 y 99
from ast import While
from operator import truediv


while True:
      numero = input("introduzca un numero entre 0 y 99: ")
      try:    
        numero = int(numero)
      except:
            pass
      else:
            if 0 < numero < 100:
               break
#parte 2:proponer al usuario adivinar el numero jugando en un bucle hasta que de con el numero
print("Intente encontrar el numero a adivinar")
while True:
      intento = input("Introduzca un numero entre 0 y 99: ")

      while True:
            try:
                intento = int(intento)
            except:
                pass
            else:
                if 0 < intento < 100:
                    break    
 
      if intento < numero:
            print("demasiado pequeño")
      elif intento > numero:
            print("demasiado grande")
      else:
            print("Ha ganado")
            break





     

      


