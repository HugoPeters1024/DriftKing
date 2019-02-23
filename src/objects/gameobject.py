from abc import abstractmethod, ABC

from src.utils.Vector2 import Vector2


class GameObject(ABC):
    def tick(self, keys):
        self._tick(keys)

    def intersects(self, other):
        return self.bounding_box.intersects(other.bounding_box)

    @property
    @abstractmethod
    def bounding_box(self):
        return None

    @abstractmethod
    def _tick(self, keys):
        pass

    @abstractmethod
    def draw(self, draw, screen, camera):
        pass

    @property
    def x(self):
        return self.position.x

    @x.setter
    def x(self, x):
        self.position = Vector2(x, self.y)

    @property
    def y(self):
        return self.position.y

    @y.setter
    def y(self, y):
        self.position = Vector2(self.x, y)

    @property
    def speed(self):
        return self.velocity.length
