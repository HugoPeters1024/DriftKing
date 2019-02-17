from math import cos, sin, sqrt, acos, atan2


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # Scalar
        if isinstance(other, (float, int)):
            return Vector2(self.x * other, self.y * other)

        # Vector
        elif isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        # Scalar
        if isinstance(other, (float, int)):
            return Vector2(self.x / other, self.y / other)

        # Vector
        elif isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y

    @staticmethod
    def Sangle(a, b):
        return acos(Vector2.dot(a, b) * (a.length * b.length))

    @property
    def angle(self):
        """Gets the angle with the x-unit vector"""
        return atan2(self.y, self.x)

    @property
    def normalized(self):
        l = self.length
        if l > 0:
            return self / self.length
        return Vector2(0, 0)


    def rotate(self, degrees):
        cs = cos(degrees)
        sn = sin(degrees)
        return Vector2(
            self.x * cs - self.y * sn,
            self.x * sn + self.y * cs)

    @property
    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)
