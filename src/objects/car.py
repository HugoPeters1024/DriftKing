import pygame
from abc import ABC
from math import pi

from src.images.images import CAR
from src.objects.gameobject import GameObject
from src.utils.Vector2 import Vector2


class Car(GameObject, ABC):
    def __init__(self):
        super().__init__()
        self.direction = 0

    def draw(self, draw, screen):
        (cx, cy) = CAR.get_rect().center
        rotated = pygame.transform.rotate(CAR, -self.direction)
        screen.blit(rotated, rotated.get_rect(center=(self.x + cx, self.y + cy)))
        pass

    def _tick(self, keys):
        if keys[pygame.K_w]:
            self.velocity += Vector2(0.1, 0).rotate(self.direction * pi / 180.0)
        if keys[pygame.K_s]:
            self.velocity += -Vector2(0.1, 0).rotate(self.direction * pi / 180.0)

        if keys[pygame.K_a]:
            self.direction -= 0.5 * self.speed
        if keys[pygame.K_d]:
            self.direction += 0.5 * self.speed
        self.velocity *= Vector2(0.98, 0.98)
