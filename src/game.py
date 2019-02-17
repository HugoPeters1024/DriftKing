# Import the pygame library and initialise the game engine
import pygame

from src.utils.Line import Line
from src.utils.Polygon import Polygon
from src.utils.Vector2 import Vector2


class Game:
    def __init__(self, car):
        self.car = car
        self.game_objects = [car]

    def run(self):
        pygame.init()

        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        # Open a new window
        size = Vector2(1400, 1000)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Drift King")

        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()
        tick = 0

        carryOn = True

        # -------- Main Program Loop -----------
        while carryOn:
            tick += 1
            camera = -self.car.position + size / 2
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False
                    break

            # First, clear the screen to black.
            screen.fill(BLACK)

            square = Polygon(points=[Vector2(0, 0), Vector2(100, 0), Vector2(100, 100), Vector2(0, 100)])
            square.draw(pygame.draw, screen)

            (mx, my) = pygame.mouse.get_pos()
            square2 = Polygon([Vector2(mx, my), Vector2(mx + 50, my), Vector2(mx + 50, my + 50), Vector2(mx, my + 50)]).rotated(tick/100.0)
            square2.draw(pygame.draw, screen)
            print(square.intersects(square2))

            """
            line = Line(40, 40, 150, 150)
            line.draw(pygame.draw, screen)

            (mx, my) = pygame.mouse.get_pos()
            line2 = Line(mx-20, my+10, mx+40, my+30)
            line2.draw(pygame.draw, screen)

            print(line.intersects(line2))
            """

            keys = pygame.key.get_pressed()
            for entity in self.game_objects:
                entity.tick(keys)

            for entity in self.game_objects:
                entity.draw(pygame.draw, screen, camera)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()
