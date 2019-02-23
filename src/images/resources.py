from pathlib import Path

import pygame

root = Path("src/images")


def load_image(name):
    return pygame.image.load(str(root / Path(name)))


CAR = load_image("car.png")
TIRE = load_image("tire.png")

pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS', 30)
