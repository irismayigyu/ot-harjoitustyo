
import sys
import pygame
from start import Start


pygame.init()
pygame.display.set_caption("2048")
# screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

FPS = 60
clock.tick(FPS)


class Main:
    def __init__(self):
        self.start = Start()
        self.start.start()


def quit_game():
    sys.exit()
