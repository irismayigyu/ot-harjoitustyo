import pygame 
import random
from entities.cube import Cube

pygame.display.set_caption("2048")
clock=pygame.time.Clock()
fps=60
clock.tick(fps)
#siirrä main.py-iin 

class Grid:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((400,400))
        self.ruutujen_koordinaatit=[]
        self.ruudukon_ruudut = []
        self.aloitusruudut=[]
        self.fontti = pygame.font.SysFont("Comic Sans",19)
        self.vari=(255,250,205)
        self.colour_of_spawning_cubes=(205,140,149)
        self.cube=Cube()
        self.value=self.cube.value
        self.make_grid_rectangles()
        self.two_random_starting_cubes()
    
    def make_grid(self):
        self.screen.fill((164,211,238))
        for cube in self.ruudukon_ruudut:
            pygame.draw.rect(self.screen, self.vari, cube, 0,10)
        for cube in self.aloitusruudut:
            pygame.draw.rect(self.screen,self.colour_of_spawning_cubes, cube, 0, 10)
            teksti = self.fontti.render(str(self.value), True, (255, 255, 255))
            numeron_nelio = teksti.get_rect(center=(cube.centerx, cube.centery))
            self.screen.blit(teksti, numeron_nelio)
            
        pygame.display.update()

    def make_grid_rectangles(self):
        for i in range(4):
            for j in range(4):
                cordinates=(j*95+20,i*95+20)
                self.ruutujen_koordinaatit.append(cordinates)
                self.ruututings=pygame.Rect(cordinates,(75,75))
                self.ruudukon_ruudut.append(self.ruututings)
        print(self.ruutujen_koordinaatit)

    def two_random_starting_cubes(self):
        aloituspaikka1=random.choice(self.ruutujen_koordinaatit)
        aloituspaikka2=random.choice(self.ruutujen_koordinaatit)
        while aloituspaikka1==aloituspaikka2:
            aloituspaikka2=random.choice(self.ruutujen_koordinaatit)
        self.aloitusruutu1=pygame.Rect(aloituspaikka1,(75,75))
        self.aloitusruutu2=pygame.Rect(aloituspaikka2,(75,75))
        self.aloitusruudut.append(self.aloitusruutu1)
        self.aloitusruudut.append(self.aloitusruutu2)

def quit_game():
    pygame.quit()
    exit()

if __name__ == "__main__":
    ruudukko = Grid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        ruudukko.make_grid()
        pygame.display.update()

