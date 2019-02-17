import pygame
from math import pi, sin, cos, acos, atan, atan2

from src.images.images import CAR, TIRE
from src.objects.gameobject import GameObject
from src.utils.Vector2 import Vector2


class Car(GameObject):
    def __init__(self):
        super().__init__()
        # Environmental constants
        self.mass = 200
        self.length = 2
        self.wheel_angle = 0.0
        self.max_wheel_angle = 0.011

        self.engineForce = 0.0
        self.direction = Vector2(1, 0)
        self.drag_constant = 0.4257
        self.rolling_resistance_constant = 12.0
        self.cornering_stiffness = 1

    def draw(self, draw, screen):
        (cx, cy) = CAR.get_rect().center
        # Put the center of gravity slightly to the back.
        cx += self.direction.x * 70
        cy += self.direction.y * 70

        (tcx, tcy) = TIRE.get_rect().center
        rotatedTyre = pygame.transform.rotate(TIRE, - self.wheel_angle / pi * 180 * 30)
        car = CAR.copy()
        car.blit(rotatedTyre, rotatedTyre.get_rect(center=(tcx + 150, tcy + 5)))
        car.blit(rotatedTyre, rotatedTyre.get_rect(center=(tcx + 150, tcy + 105)))
        rotated = pygame.transform.rotate(car, -self.direction.angle / pi * 180.0)

        screen.blit(rotated, rotated.get_rect(center=(self.x + cx, self.y + cy)))
        draw.line(screen, (255, 255, 255), (self.x, self.y),
                  (self.x + self.lateral_resistance.x * 10, self.y + self.lateral_resistance.y * 10))
        pass

    def _tick(self, keys):
        self.velocity += self.acceleration
        self.direction = self.direction.rotate(self.angular_momentum)

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
                self.wheel_angle += (0 - self.wheel_angle) * self.speed / 109.0

        if keys[pygame.K_SPACE]:
            self.cornering_stiffness = 20
        else:
            self.cornering_stiffness = 1

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
    def lateral_resistance(self):
        angle1 = self.direction.angle + self.wheel_angle
        angle2 = self.velocity.normalized.angle
        #angle = angle1 - angle2
        #beta = atan2(self.velocity.y, self.velocity.x)
        #alpha_rear =
        print(angle1 - angle2)
        return Vector2(self.direction.y, -self.direction.x) * sin(angle1 - angle2) * self.speed * self.cornering_stiffness


    @property
    def acceleration(self):
        return (self.traction + self.drag + self.rolling_resistance + self.lateral_resistance) / self.mass

    @property
    def angular_momentum(self):
        if self.wheel_angle != 0:
            radius = self.length / sin(self.wheel_angle)
        else:
            radius = 99999999999  # ~infinity

        return self.speed / radius
