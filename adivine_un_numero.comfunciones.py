#escribimos la funcion de pedir numero para luego reutilizarla
def pedir_un_numero():
    while True:
        entrada = input("introduzca un numero entre 0 y 99: ")
        try:
            entrada = int(entrada)
        except:
            pass
        if 0 < entrada < 100:
            break
    return entrada
print("introduzca el numero a adivinar")
numero = pedir_un_numero

print("Intente encontrar el numero a adivinar")

while True:
    intento = pedir_un_numero
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Ha ganado")
    break

