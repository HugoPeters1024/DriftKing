from abc import abstractmethod, ABC

from src.utils.Vector2 import Vector2


class GameObject(ABC):
    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    def tick(self, keys):
        # Basic psychics
        self.position += self.velocity

        self._tick(keys)

    @abstractmethod
    def _tick(self, keys):
        pass

    @abstractmethod
    def draw(self, draw, screen):
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
