#Fase1
class Punto:
    def __init__(self, x, y ,z):
        #Metodo de inicializacion
        self.x = x
        self.y = y
        self.z = z
    def mostrar(self):
        print("punto {}, {}, {}".format(self.x, self.y, self.z))
p = Punto(1, 2, 3)
p.mostrar()