import pygame
from math import pi, sin, cos, acos, atan

from src.images.images import CAR
from src.objects.gameobject import GameObject
from src.utils.Vector2 import Vector2


class Car(GameObject):
    def __init__(self):
        super().__init__()
        # Environmental constants
        self.mass = 200
        self.length = 2
        self.wheel_angle = 0
        self.max_wheel_angle = 0.005

        self.engineForce = 0
        self.direction = Vector2(1, 0)
        self.drag_constant = 0.4257
        self.rolling_resistance_constant = 12

    def draw(self, draw, screen):
        (cx, cy) = CAR.get_rect().center
        rotated = pygame.transform.rotate(CAR, -self.direction.angle / pi * 180.0)
        screen.blit(rotated, rotated.get_rect(center=(self.x + cx, self.y + cy)))
        # draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.velocity.x * 10, self.y + self.velocity.y * 10))
        pass

    def _tick(self, keys):
        if self.wheel_angle != 0:
            radius = self.length / sin(self.wheel_angle)
        else:
            radius = 99999999999  # ~infinity

        omega = self.speed / radius
        self.direction = self.direction.rotate(omega)
        self.velocity += self.acceleration

        self.wheel_angle *= 0.98
        if keys[pygame.K_w]:
            self.engineForce = 100
        elif keys[pygame.K_s]:
            self.engineForce = -25
        else:
            self.engineForce = 0

        if keys[pygame.K_a]:
            if self.wheel_angle > -self.max_wheel_angle:
                self.wheel_angle -= 0.001
        elif keys[pygame.K_d]:
            if self.wheel_angle < self.max_wheel_angle:
                self.wheel_angle += 0.001
        else:
            if self.wheel_angle != 0:
                self.wheel_angle += (0 - self.wheel_angle) * 0.1

        print(self.engineForce)

    @property
    def traction(self):
        return self.direction * self.engineForce

    @property
    def drag(self):
        return -self.velocity * self.drag_constant * self.speed

    @property
    def rolling_resistance(self):
        return -self.velocity * self.rolling_resistance_constant

    @property
    def acceleration(self):
        return (self.traction + self.drag + self.rolling_resistance) / self.mass


