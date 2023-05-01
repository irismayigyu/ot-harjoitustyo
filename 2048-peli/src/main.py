import sys
import pygame
from start import Start
from ending import Ending


pygame.init()
pygame.display.set_caption("2048")
#screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

FPS = 60
clock.tick(FPS)


class Main:
    def __init__(self):
        self.start=Start()
        self.ending=Ending()

    def start(self):
        while True and not self.ended:
            self.start.start()

def quit_game():
    sys.exit()


# if __name__ == "__main__":
#     start = Start()
#     start.start()
