import pickle
import neat
import sys
from statistics import mean, stdev

from level3 import walls, checkpoints
from src.game import Game
from src.objects.car import Car
from src.utils.Vector2 import Vector2

pivot = 0
alpha = 0

if not len(sys.argv) == 3:
    print(f"Expected exactly 2 arguments: alpha, pivot")
    exit(1)

try:
    alpha = float(sys.argv[1])
except ValueError:
    print(f"{sys.argv[1]} is not a valid float value for alpha")
    exit(1)

try:
    pivot = int(sys.argv[2])
except ValueError:
    print(f"{sys.argv[2]} is not a vlid int value for the pivot")
    exit(1)



filename = f"results/feedfoward-alpha={alpha}-pivot={pivot}-long-species.csv"


def eval_genomes(genomes, config):
    cars = []
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        car = Car(net, alpha)
        car.position = Vector2(150, 100)
        cars.append(car)

    game = Game(cars)
    game.game_objects.extend(walls)
    game.game_objects.extend(checkpoints)

    scores = game.run()
    with open(filename, "a") as file:
        file.write(f"{max(scores)},{min(scores)},{mean(scores)},{stdev(scores)}\n")
    for (genome_id, genome), score in zip(genomes, scores):
        genome.fitness = score
    
    # Stop if all checkpoints are collected
    print(f"best has {max([x.checkpoints for x in cars])}/{len(checkpoints)} checkpoints.")
    if any([x.checkpoints == len(checkpoints) for x in cars]):
        print("All checkpoints collected, aborting")
        exit(0);


config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config-feedforward')

config.__setattr__("fitness_threshold", len(checkpoints) * 10 * 1000)
print(f"Stopping when score exceeds {len(checkpoints) * 10 + 1000}")

with open(filename, "w") as file:
    file.write("Highest,Lowest,Mean,Stdev\n")

p = neat.Population(config)

p.add_reporter(neat.StdOutReporter(False))

winner = p.run(eval_genomes)
print(winner)
with open("winner.bin", "wb") as f:
    pickle.dump(winner, f, 2)

