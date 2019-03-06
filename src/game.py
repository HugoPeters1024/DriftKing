# Import the pygame library and initialise the game engine
from multiprocessing import Queue, Process

import pygame

from src.objects.checkpoint import CheckPoint
from src.objects.wall import Wall
from src.utils.Vector2 import Vector2


class Game:
    def __init__(self, cars):
        self.cars = cars
        self.game_objects = []
        # Is calculated on game start
        self.walls = []
        self.checkpoints = []

    def run(self):
        pygame.init()
        pygame.font.init()
        self.walls = [x for x in self.game_objects if isinstance(x, Wall)]
        self.checkpoints = [x for x in self.game_objects if isinstance(x, CheckPoint)]

        BLACK = (0, 0, 0)

        # Open a new window
        size = Vector2(1400, 1000)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Drift King")

        carryOn = True
        camera = Vector2(0, 0)
        clock = pygame.time.Clock()

        processes = []
        input = Queue(500)
        output = Queue(500)
        for i in range(len(self.cars)):
            input.put((i, self.cars[i]))
            p = Process(target=work, args=(input, output, self))
            p.start()
            processes.append(p)

        # -------- Main Program Loop -----------
        while carryOn:
            if all([x.dead for x in self.cars]):
                # Flush the interprocess queue to prevent deadlock
                while not output.empty():
                    (_, _) = output.get()
                [p.join() for p in processes]
                return [x.score for x in self.cars]

            best_score = max([x.score for x in self.cars if not x.dead])
            target_camera = -[x for x in self.cars if x.score == best_score][0].position + size / 2
            camera += (target_camera - camera) / 10
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False
                    break

            for i in range(len([x for x in self.cars if not x.dead])):
                (index, car) = output.get()
                self.cars[index] = car

            # First, clear the screen to black.
            screen.fill(BLACK)
            for entity in self.game_objects:
                entity.draw(pygame.draw, screen, camera)
            for car in self.cars:
                car.draw(pygame.draw, screen, camera)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            #clock.tick(60)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()


def work(input, output, game):
    ticks = 0
    (index, car) = input.get()
    while (not car.dead) and ticks < 1000:
        car.project_sensors(game.walls)
        car.tick(None)
        for wall in game.walls:
            if car.intersects(wall):
                car.score -= 10
                car.dead = True
                output.put((index, car))
                return
        for checkpoint in game.checkpoints:
            if checkpoint not in car.checkpoints:
                if car.intersects(checkpoint):
                    car.score += 10
                    car.checkpoints.append(checkpoint)
                    checkpoint.show = False
        output.put((index, car))
        ticks += 1
    car.dead = True
    output.put((index, car))
    return
