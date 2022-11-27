#parte1: hacer que el usuario introduzca un numero, y comrprobar que sea entero y ademas comprendido entre 0 y 99
from ast import While
from operator import truediv

def pedir_un_numero():
      while True:
        entrada = input("introduzca un numero entre 0 y 99: ")
        try:    
            entrada = int(entrada)
        except:
               pass
        else:
               if 0 < entrada < 100:
                  break
      return entrada
#parte 2:proponer al usuario adivinar el numero jugando en un bucle hasta que de con el numero
def adivinar_un_numero():
      print("Intente encontrar el numero a adivinar")
      while True:

            while True:
                intento = input("introduzca un numero entre 0 y 99: ")
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





     

      


