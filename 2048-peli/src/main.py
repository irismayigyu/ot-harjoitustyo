import sys
import pygame
from griddrawing import Grid

pygame.init()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)


class Main:
    def __init__(self):
        pass


def quit_game():
    sys.exit()


if __name__ == "__main__":
    grid = Grid(screen)
    grid.run_loop()
