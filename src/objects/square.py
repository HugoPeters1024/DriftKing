import pygame
from abc import ABC

from src.objects.gameobject import GameObject
from src.utils.Vector2 import Vector2


class Square(GameObject, ABC):
    def _tick(self, keys):
        self.velocity *= Vector2(0.99, 0.99)
        if keys[pygame.K_LEFT]:
            self.velocity = Vector2(0, -1)

    def draw(self, draw, screen):
        draw.rect(screen, (0, 255, 0), [self.x, self.y, 20, 20])
