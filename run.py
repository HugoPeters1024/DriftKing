import neat

from level2 import walls, checkpoints
from src.game import Game
from src.objects.car import Car
from src.utils.Vector2 import Vector2


def eval_genomes(genomes, config):
    cars = []
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        car = Car(net)
        car.position = Vector2(200, 200)
        cars.append(car)

    game = Game(cars)
    game.game_objects.extend(walls)
    game.game_objects.extend(checkpoints)

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

