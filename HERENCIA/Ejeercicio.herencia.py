class Punto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def mostrar(self):
        print("Punto {}, {}, {}".format(self.x, self.y, self.z))
    #FASE2  
    def modulo(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)
    def distancia(self, other=None):
        if other is None:
            other = (0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)
P = Punto(1, 2, 3)
P.mostrar()
print("|P|=", P.modulo())
print("La distancia entre P y el punto (2, 4, 1) es:", P.distancia())
