from itertools import chain, product, repeat, cycle

lista = list("abc")
#recorrido clasico de una lista
for lista in lista:
    print(lista)
#si queremos ver indices tambien
for indice, letra in enumerate(lista):
    print("indice {}, letra {}".format(indice, letra))