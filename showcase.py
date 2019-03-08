import pickle

import neat

from src.game import Game
from src.objects.car import Car
from src.utils.Vector2 import Vector2

from level1 import walls, checkpoints

if __name__ == "__main__":
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'config-feedforward')

    with open("winner.bin", "rb") as f:
        genome = pickle.load(f)
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    car = Car(net)
    car.position = Vector2(200, 200)
    game = Game([car])
    game.game_objects.extend(walls)
    game.game_objects.extend(checkpoints)
    game.run()
