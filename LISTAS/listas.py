lista = list("python is awesome")
print(lista)
#para seleccionar un elemento unico de la lista:
lista[4]
lista[-3]
print("lista[4]=", lista[4])
print("lista[-3]=", lista[3])
#extraccion de sublista
print("lista[:6]=", lista[:6])
print("lista[6:]=", lista[6:])
print("lista[-6:]=", lista[-6:])
print("lista[3:6]=", lista[3:6])
print("lista[2::7]=", lista[2::7])
#escritura de un miembro de la lista
lista[5] = "r"
print(lista)
lista[13:15] = "fg"
print("lista = ", lista)
lista[5] = "n"
lista[10] = "s"
lista[11] = "h"
lista[12] = "i"
lista[13] = "t"
#eliminar un elemento de la lista
print(lista)
lista.pop()
print(lista)
lista.remove("m")
lista.remove("g")
print(lista)
while " " in lista:
    lista.remove(" ")
print(lista)
while "o" and "n" in lista:
    lista.remove("o")
    lista.remove("n")
print(lista)
#agregar un elemento al final de la lista
lista.append("!")
print(lista)
#agregar un elemento a la lista donde queramos
lista.insert(4, "o")
lista.insert(5, "n")
lista.insert(6, " ")
lista.insert(9, " ")
print(lista)



