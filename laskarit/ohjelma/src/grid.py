import pygame 
import random
#from entities.cube import Cube

pygame.display.set_caption("Ohte 2048")
kello=pygame.time.Clock()
fps=60
kello.tick(fps)
#siirrä main.py-iin 

class Grid:
    def __init__(self):
        pygame.init()
        self.naytto=pygame.display.set_mode((400,400))
        self.ruutujen_koordinaatit=[]
        self.ruudukon_ruudut = []
        self.aloitusruudut=[]
        self.fontti = pygame.font.SysFont("Comic Sans", 19)
        self.vari=(200,200,200)
        self.spawnaavien_ruutujen_vari=(255, 0, 127)
        self.value=Cube.self.value
        self.luo_ruudukon_ruudut()
        self.random_aloitus_ruutu()
    
    def luo_ruudukko(self):
        self.naytto.fill("black")
        for ruutu in self.ruudukon_ruudut:
            pygame.draw.rect(self.naytto, self.vari, ruutu, 0,10)
        for ruutu in self.aloitusruudut:
            pygame.draw.rect(self.naytto,self.spawnaavien_ruutujen_vari, ruutu, 0, 10)
            teksti = self.fontti.render(str(self.value), True, (255, 255, 255))
            numeron_nelio = teksti.get_rect(center=(ruutu.centerx, ruutu.centery))
            self.naytto.blit(teksti, numeron_nelio)
            
        pygame.display.update()

    def luo_ruudukon_ruudut(self):
        for i in range(4):
            for j in range(4):
                koordinaatit=(j*95+20,i*95+20)
                self.ruutujen_koordinaatit.append(koordinaatit)
                self.ruututings=pygame.Rect(koordinaatit,(75,75))
                self.ruudukon_ruudut.append(self.ruututings)
        print(self.ruutujen_koordinaatit)

    def random_aloitus_ruutu(self):
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
        ruudukko.luo_naytto()
        pygame.display.update()

