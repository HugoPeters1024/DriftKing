from src.objects.gameobject import GameObject
from src.utils.Polygon import Polygon
from src.utils.Vector2 import Vector2


class CheckPoint(GameObject):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.show = True

    def draw(self, draw, screen, camera):
        if self.show:
            draw.line(screen, (40, 40, 255), Vector2(self.x1, self.y1) + camera, Vector2(self.x2, self.y2) + camera)

    def _tick(self, keys):
        pass

    @property
    def bounding_box(self):
        pt1 = Vector2(self.x1, self.y1)
        pt2 = Vector2(self.x2, self.y2)
        return Polygon([pt1, pt2])

    def __mul__(self, other):
        self.x1 *= other
        self.y1 *= other
        self.x2 *= other
        self.y2 *= other

