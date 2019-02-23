import random
from math import pi, cos, sin

import neat

from src.game import Game
from src.objects.car import Car
from src.objects.wall import Wall
from src.objects.checkpoint import CheckPoint
from src.utils.Vector2 import Vector2


def eval_genomes(genomes, config):
    cars = []
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        car = Car(net)
        car.position = Vector2(680, 220)
        cars.append(car)
    game = Game(cars)
    center = Vector2(700, 500)

    for i in range(30):
        ratio = (i / 30.0) * (2 * pi)
        ratio2 = ((i + 1) / 30.0) * (2 * pi)
        dis = 200
        pt1 = Vector2(cos(ratio), sin(ratio)) * dis + center
        pt2 = Vector2(cos(ratio2), sin(ratio2)) * dis + center

        wall = Wall(pt1.x, pt1.y, pt2.x, pt2.y)
        game.game_objects.append(wall)

    for i in range(30):
        ratio = (i / 30.0) * (2 * pi)
        ratio2 = ((i + 1) / 30.0) * (2 * pi)
        dis = 300
        pt1 = Vector2(cos(ratio), sin(ratio)) * dis + center
        pt2 = Vector2(cos(ratio2), sin(ratio2)) * dis + center

        wall = Wall(pt1.x, pt1.y, pt2.x, pt2.y)
        game.game_objects.append(wall)
        checkpoint = CheckPoint(pt1.x, pt1.y, pt1.x - 100 * cos(ratio), pt1.y - 100 * sin(ratio))
        game.game_objects.append(checkpoint)

    scores = game.run()
    # scores = [x / sum(scores) for x in scores]
    print(scores)
    for (genome_id, genome), score in zip(genomes, scores):
        print(f"car {genome_id}: {score}")
        genome.fitness = score


config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config-feedforward')

p = neat.Population(config)

p.add_reporter(neat.StdOutReporter(False))

winner = p.run(eval_genomes, 300)

