# Import the pygame library and initialise the game engine
import pygame

from src.objects.car import Car
from src.objects.checkpoint import CheckPoint
from src.objects.wall import Wall
from src.utils.Line import Line
from src.utils.Polygon import Polygon
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

        tick = 0
        carryOn = True

        # -------- Main Program Loop -----------
        while carryOn:
            tick += 1
            if tick > 1000 or all([x.dead for x in self.cars]):
                return [x.score for x in self.cars]
            # camera = -self.car.position + size / 2
            camera = Vector2(0, 0)
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False
                    break

            for car in [x for x in self.cars if not x.dead]:
                car.project_sensors(self.walls)
                car.tick(None)
                for wall in self.walls:
                    if car.intersects(wall):
                        car.score -= 10
                        car.dead = True
                for checkpoint in self.checkpoints:
                    if checkpoint not in car.checkpoints:
                        if car.intersects(checkpoint):
                            car.score += 10
                            car.checkpoints.append(checkpoint)
                            checkpoint.show = False

            if tick % 3 == 0:
                # First, clear the screen to black.
                screen.fill(BLACK)
                for entity in self.game_objects:
                    entity.draw(pygame.draw, screen, camera)
                for car in self.cars:
                    car.draw(pygame.draw, screen, camera)

            # --- Go ahead and update the screen with what we've drawn.
            if tick % 3 == 0:
                pygame.display.flip()

            # --- Limit to 60 frames per second
            # clock.tick(60)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()
