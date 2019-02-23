from math import sqrt

from src.utils.Vector2 import Vector2


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def intersects(self, other):
        x1 = self.x1
        x2 = self.x2
        x3 = other.x1
        x4 = other.x2

        y1 = self.y1
        y2 = self.y2
        y3 = other.y1
        y4 = other.y2

        p_num_x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        p_den_x = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        p_num_y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        p_den_y = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if p_den_x == 0 or p_den_y == 0:
            return False

        px = p_num_x / p_den_x
        py = p_num_y / p_den_y

        return self.has_point(px, py) and other.has_point(px, py)

    def intersection_length(self, other):
        if not self.intersects(other):
            return float("inf")
        x1 = self.x1
        x2 = self.x2
        x3 = other.x1
        x4 = other.x2

        y1 = self.y1
        y2 = self.y2
        y3 = other.y1
        y4 = other.y2

        t_num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        t_den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if t_den == 0:
            return float("inf")

        length = (t_num / t_den) * self.length
        return length if length >= 0 else float("inf")

    def cutoff(self, other):
        dir = Vector2(self.x2 - self.x1, self.y2 - self.y1) / self.length
        if isinstance(other, Line):
            length = self.intersection_length(other)
            if length < self.length:
                return Line(self.x1, self.y1, self.x1 + dir.x * length, self.y1 + dir.y * length)
            return self

    def has_point(self, x, y):
        dxc = x - self.x1
        dyc = y - self.y1

        dxl = self.x2 - self.x1
        dyl = self.y2 - self.y1

        cross = dxc * dyl - dyc * dxl

        if not abs(cross) < 0.01:
            return False

        if abs(dxl) >= abs(dyl):
            return self.x1 <= x <= self.x2 if dxl > 0 else self.x2 <= x <= self.x1
        else:
            return self.y1 <= y <= self.y2 if dyl > 0 else self.y2 <= y <= self.y1

    def rotate(self, angle):
        dir = (Vector2(self.x2, self.y2) - Vector2(self.x1, self.y1)).rotate(angle)
        return Line(self.x1, self.y1, dir.x + self.x1, dir.y + self.y1)

    def draw(self, draw, screen):
        draw.line(screen, (255, 255, 255), (self.x1, self.y1), (self.x2, self.y2))

    @property
    def length(self):
        dx = self.x1 - self.x2
        dy = self.y1 - self.y2
        return sqrt(dx * dx + dy * dy)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Line(self.x1 + other.x, self.y1 + other.y, self.x2 + other.x, self.y2 + other.y)
