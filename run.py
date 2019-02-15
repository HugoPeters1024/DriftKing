from src.game import Game
from src.objects.car import Car
from src.objects.square import Square
from src.utils.Vector2 import Vector2

game = Game()
square = Square()
square.position = Vector2(100, 100)
game.game_objects.append(square)

car = Car()
car.position = Vector2(300, 150)
game.game_objects.append(car)
game.run()
