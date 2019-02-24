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
        car.position = Vector2(200, 200)
        cars.append(car)
    game = Game(cars)
    center = Vector2(700, 500)

    scalar = Vector2(140, 75)

    points = [
        Vector2(1, 1),
        Vector2(5, 0),
        Vector2(9, 1),
        Vector2(9, 10),
        Vector2(5, 10),
        Vector2(6, 6),
        Vector2(3, 9),
        Vector2(1, 10),
    ]

    for i in range(len(points)):
        pt1 = points[i] * scalar
        pt2 = points[(i+1)%len(points)] * scalar
        wall = Wall(pt1.x, pt1.y, pt2.x, pt2.y)
        game.game_objects.append(wall)

    points2 = [
        Vector2(1.4, 4.5),
        Vector2(5, 2),
        Vector2(8, 3),
        Vector2(7, 8)
    ]

    thepoint = points[5] * scalar
    extra = CheckPoint(thepoint.x, thepoint.y, thepoint.x + 80, thepoint.y - 265)
    game.game_objects.append(extra)
    thepoint = points2[0] * scalar
    extra = CheckPoint(thepoint.x, thepoint.y, thepoint.x - 80, thepoint.y)
    game.game_objects.append(extra)


    for i in range(len(points2)-1):
        pt1 = points2[i] * scalar
        pt2 = points2[(i+1)] * scalar
        wall = Wall(pt1.x, pt1.y, pt2.x, pt2.y)
        game.game_objects.append(wall)

        for pt_check in points:
            pt_check = pt_check * scalar
            check = CheckPoint(pt1.x, pt1.y, pt_check.x, pt_check.y)
            game.game_objects.append(check)

    scores = game.run()
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

