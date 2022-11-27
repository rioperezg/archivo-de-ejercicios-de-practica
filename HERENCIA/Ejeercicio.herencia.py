class Punto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def mostrar(self):
        print("Punto {}, {}, {}".format(self.x, self.y, self.z))
p = Punto(1, 2, 3)
p.mostrar()    
    