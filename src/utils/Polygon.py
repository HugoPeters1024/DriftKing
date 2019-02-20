import pygame

from src.utils.Vector2 import Vector2
from src.utils.Line import Line


class Polygon:
    def __init__(self, points):
        self.points = points

    def draw(self, draw, screen, camera):
        draw.polygon(screen, (255, 255, 255), [p + camera for p in self.points])

    def intersects(self, other):
        for myedge in self.edges:
            for otheredge in other.edges:
                if myedge.intersects(otheredge):
                    return True
        return False

    @property
    def edges(self):
        result = []
        l = len(self.points)
        for i in range(l):
            a = self.points[i]
            b = self.points[(i+1) % l]
            result.append(Line(a.x, a.y, b.x, b.y))
        return result

    def rotated(self, angle):
        newpoints = []
        center = self.centroid
        for p in self.points:
            newpoints.append((p - center).rotate(angle) + center)
        return Polygon(newpoints)


    @property
    def centroid(self):
        off = self.points[0]
        j = len(self.points) - 1
        twicearea = 0
        x = 0
        y = 0
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[j]
            f = (p1.x - off.x) * (p2.y - off.y) - (p2.x - off.x) * (p1.y - off.y)
            twicearea += f
            x += (p1.x + p2.x - 2 * off.x) * f
            y += (p1.y + p2.y - 2 * off.y) * f
            j = i

        f = twicearea * 3
        return Vector2(x / f + off.x, y / f + off.y)



