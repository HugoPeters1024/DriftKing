from math import pi, sin, cos, atan2

import pygame

from src.images.images import CAR, TIRE
from src.objects.gameobject import GameObject
from src.utils.Polygon import Polygon
from src.utils.Vector2 import Vector2
from src.utils.mathx import sign


class Car(GameObject):
    def __init__(self):
        super().__init__()
        # Environmental constants
        self.mass = 200
        self.length = 2
        self.wheel_angle = 0.0
        self.max_wheel_angle = 0.4
        self.torque = 0
        self.gears = [
            (4, 60),
            (6.5, 75),
            (7.5, 90)

        ]

        self.engineForce = 0.0
        self.breakingForce = 0
        self.direction = Vector2(1, 0)
        self.drag_constant = 0.4257
        self.rolling_resistance_constant = 6
        self.cornering_stiffness = 0.4

    @property
    def bounding_box(self):
        pt1 = Vector2(self.center.x - 30, self.center.y - 14)
        pt2 = Vector2(self.center.x + 30, self.center.y - 14)
        pt3 = Vector2(self.center.x + 30, self.center.y + 14)
        pt4 = Vector2(self.center.x - 30, self.center.y + 14)
        return Polygon([pt1, pt2, pt3, pt4]).rotated(self.direction.angle)

    def draw(self, draw, screen, camera):
        car = CAR.copy()
        rotated = pygame.transform.rotate(car, -self.direction.angle / pi * 180.0)

        screen.blit(rotated, rotated.get_rect(center=(self.center.x + camera.x, self.center.y + camera.y)))
        screen.blit(TIRE, (0, 0))

    def _tick(self, keys):
        self.velocity += self.acceleration
        self.direction = self.direction.rotate(self.angular_momentum / 30)

        ready_force = 40
        for (threshold, force) in self.gears:
            if self.speed > threshold:
                ready_force = force

        if keys[pygame.K_w]:
            self.engineForce = ready_force
        elif keys[pygame.K_s]:
            self.engineForce = -10
        else:
            self.engineForce = 0

        if keys[pygame.K_a]:
            if self.wheel_angle > -self.max_wheel_angle:
                self.wheel_angle -= 0.01
        elif keys[pygame.K_d]:
            if self.wheel_angle < self.max_wheel_angle:
                self.wheel_angle += 0.01
        else:
            if self.wheel_angle != 0:
                self.wheel_angle += (0 - self.wheel_angle) * self.speed / 109.0

        if keys[pygame.K_SPACE]:
            self.breakingForce = 10
        else:
            self.breakingForce = 0

        self.torque *= 0.98

    @property
    def center(self):
        (cx, cy) = CAR.get_rect().center
        return self.position + Vector2(cx, cy) + self.direction * 20

    @property
    def traction(self):
        return self.direction * self.engineForce

    @property
    def brakes(self):
        forward_speed = abs((self.direction - self.velocity).y)
        if forward_speed > 0.1:
            return -self.direction * min(self.breakingForce, forward_speed)
        return Vector2(0, 0)

    @property
    def drag(self):
        return -self.velocity * self.drag_constant * self.speed

    @property
    def rolling_resistance(self):
        return -self.velocity * self.rolling_resistance_constant

    @property
    def cornering_force(self):
        angle1 = self.direction.angle + self.wheel_angle
        angle2 = self.velocity.angle
        angle = angle1 - angle2

        longitudinal = cos(angle) * self.speed
        lateral = sin(angle) * self.speed

        rear = atan2(lateral + self.angular_momentum, longitudinal)
        front = atan2(lateral + self.angular_momentum, longitudinal) + self.wheel_angle * sign(longitudinal)

        rear_force = rear * 2
        front_force = front

        total = rear_force + cos(self.wheel_angle) * front_force
        # self.torque += (-rear_force + cos(self.wheel_angle) * front_force) / 90.0

        return Vector2(-self.velocity.y, self.velocity.x) * -total * self.cornering_stiffness

    @property
    def acceleration(self):
        return (self.traction + self.brakes + self.drag + self.rolling_resistance + self.cornering_force) / self.mass

    @property
    def angular_momentum(self):
        return self.steer_momentum + self.torque

    @property
    def steer_momentum(self):
        if self.wheel_angle != 0:
            radius = self.length / sin(self.wheel_angle)
        else:
            radius = 99999999999  # ~infinity

        return self.speed / radius
