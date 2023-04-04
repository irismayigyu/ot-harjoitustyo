import pygame 
import random
from grid import Grid
from entities.cube import Cube

pygame.display.set_caption("2048")
clock=pygame.time.Clock()
fps=60
clock.tick(fps)
pygame.init()

class Main:
    pygame.init()

    def __init__(self):
        super().__init__()
        grid=Grid() 
        cube=Cube()
        self.value=Cube.self.value


def quit_game():
    pygame.quit()
    exit()

if __name__ == "__main__":
    grid= Grid() 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        grid.make_grid()
        pygame.display.update()