class Punto:
    """Representa un punto en el espacio"""

    def __init__(self, x, y, z):
        """Método de inicialización de un punto en el espacio"""
        self.x, self.y, self.z = x, y, z

    def distancia(self, other=None):
        """Devuelve la distancia respecto a otro punto o por defecto al origen"""
        if other is None:
            other = Punto(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)
    def __add__(self, other=None):
        if other is None:
            return (self.x, self.y, self.z)
        else:
            return ((self.x+other.x), (self.y+other.y), (self.z+other.z))
    def __sub__(self, other=None):
        if other is None:
            return (self.x, self.y, self.z)
        else:
            return ((self.x-other.x), (self.y-other.y), (self.z-other.z))
    def __mul__(self, scalaire):
        return(self.x*scalaire, self.y*scalaire, self.z*scalaire)
    def __str__(self):
        return ("punto: {}, {}, {}".format(self.x, self.y, self.z))

P = Punto(1, 2, 3)
r = Punto(2, 0, 1)
print(P.distancia(r))
print(P.__add__(r))
print(P.__sub__(r))
print(P.__mul__(3))
print(P.__str__())
