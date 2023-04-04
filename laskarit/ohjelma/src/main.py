import pygame 
import random
from grid import Grid
from entities.cube import Cube

pygame.display.set_caption("Ohte 2048")
kello=pygame.time.Clock()
fps=60
kello.tick(fps)
pygame.init()

class Main:
    pygame.init()

    def __init__(self):
        super().__init__()
        ruudukko=Grid() #poistanko tästä tämän?
        self.value=Cube.self.value


def quit_game():
    pygame.quit()
    exit()

if __name__ == "__main__":
    ruudukko = Grid() 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        ruudukko.luo_naytto()
        pygame.display.update()