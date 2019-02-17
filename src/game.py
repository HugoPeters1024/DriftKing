# Import the pygame library and initialise the game engine
import pygame

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
        camera = Vector2(0, 0)

        carryOn = True

        # -------- Main Program Loop -----------
        while carryOn:
            camera = -self.car.position + size/2
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False
                    break

            # First, clear the screen to black.
            screen.fill(BLACK)
            # The you can draw different shapes and lines or add text to your background stage.

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
