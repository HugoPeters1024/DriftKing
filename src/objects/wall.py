from src.objects.gameobject import GameObject
from src.utils.Polygon import Polygon
from src.utils.Vector2 import Vector2


class Wall(GameObject):
    @property
    def bounding_box(self):
        pt1 = Vector2(self.x1, self.y1 - 1)
        pt2 = Vector2(self.x2, self.y2 - 1)
        pt3 = Vector2(self.x2, self.y2 + 1)
        pt4 = Vector2(self.x1, self.y1 + 1)
        return Polygon([pt1, pt2, pt3, pt4])

    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, draw, screen, camera):
        draw.aaline(screen, (0, 255, 0), (self.x1 + camera.x, self.y1 + camera.y), (self.x2 + camera.x, self.y2 + camera.y), 10)
        pass

    def _tick(self, keys):
        pass
