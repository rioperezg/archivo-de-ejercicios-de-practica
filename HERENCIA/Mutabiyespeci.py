class Punto:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def Distancia(self, other=None):
        if other is None:
            other=Punto(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)
    def __add__(self, other):
        if other is None:
            return(self.x, self.y, self.z)
        else:
            return ((self.x + other.x), (self.y + other.y), (self.z + other.z))
    def __sub__(self, other):
        if other is None:
            return(self.x, self.y, self.z)
        else:
            return((self.x - other.x), (self.y - other.y), (self.z - other.z))
    def __mul__(self, sclaire):
        return ((sclaire*self.x), (sclaire*self.y), (sclaire*self.z))
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return (self)
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return (self)
    def __imul__(self, scalaire):
        self.x *= scalaire
        self.y *= scalaire
        self.z *= scalaire
        return self
    def __str__(self):
        return("Punto ({self.x}, {self.y}, {self.z})".format(self=self))
class Punto2D(Punto):
    def __init__(self, x, y):
        super().__init__(x, y, 0)
    def __str__(self):
        return ("Punto ({self.x}, {self.y})".format(self=self))
        

P = Punto(1, 2, 3)
r = Punto(0, 1, 3)
print(P.__imul__(2))
T = Punto2D(1, 0)
Q = Punto2D(2, 0)
print(T.__iadd__(Q))
