from src.utils import Vector2


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersect(self, other):
        if isinstance(other, Vector2):

