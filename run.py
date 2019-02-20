import random

from src.game import Game
from src.objects.car import Car
from src.objects.wall import Wall
from src.utils.Vector2 import Vector2

car = Car()
car.position = Vector2(300, 150)

game = Game(car)

x = 0
y = 0
for i in range(30):
    xd = random.randrange(100)
    yd = random.randrange(100)
    wall = Wall(x, y, x + xd, y + yd)
    x += xd
    y += yd
    game.game_objects.append(wall)

game.run()
