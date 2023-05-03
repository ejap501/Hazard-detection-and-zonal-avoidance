from math import sqrt

class Vector:
    def __init__(self, x=0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        assert other != 0
        return Vector(self.x / other, self.y / other, self.z / other)

    def __div__(self, other):
        assert not isinstance(other, Vector)
        assert other != 0
        return Vector(self.x // other, self.y // other, self.z // other)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self):
        return sqrt(self.dot_product(self))

    def normalise(self):
        return self / self.magnitude()
