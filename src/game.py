# Import the pygame library and initialise the game engine
import pygame


class Game:
    def __init__(self):
        self.game_objects = []

    def run(self):
        pygame.init()

        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        # Open a new window
        size = (700, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("My First Game")

        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()

        carryOn = True

        # -------- Main Program Loop -----------
        while carryOn:
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
                entity.draw(pygame.draw, screen)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()
