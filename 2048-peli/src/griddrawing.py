
import pygame
from matrix import Matrix


class Grid:
    def __init__(self, screen):
        self.matrix = Matrix()
        self.gridm = self.matrix.gridm
        self.colour = (255, 250, 205)
        self.other_colour = (205, 140, 149)
        self.vaari=(180,180,100)
        self.fontti = pygame.font.SysFont("Comic Sans", 19)
        self.leveys = 75
        self.cubes_list=[]
        self.screen = screen
        self.ruudukon_ruudut=[]
        self.initialize_grid()

    def run_loop(self):
        while True:
            self.draw_cubes()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.matrix.movement_left()
                    elif event.key == pygame.K_RIGHT:
                        self.matrix.movement_right()
                    elif event.key == pygame.K_UP:
                        self.matrix.movement_up()
                    elif event.key == pygame.K_DOWN:
                        self.matrix.movement_down()

    def initialize_grid(self):
        for i in range(4):
            for j in range(4):
                cordinates = (j*95+20, i*95+20)
                self.cuberectangle = pygame.Rect(cordinates, (75, 75))
                self.ruudukon_ruudut.append(self.cuberectangle)
        self.screen.fill((164, 211, 238))
        for i in self.ruudukon_ruudut:
            pygame.draw.rect(self.screen, self.vaari, i, 0, 10)

        pygame.display.update()

    def draw_cubes(self):
        self.cubes_list=[]
        gap_size = 20
        for i in range(4):
            for j in range(4):
                value = self.gridm[i][j]
                if value != 0:
                    x_cordinate = j * (self.leveys + gap_size) + 20
                    y_cordinate = i * (self.leveys + gap_size) + 20
                    cube_rect = pygame.Rect(x_cordinate, y_cordinate, self.leveys, self.leveys)
                    self.cubes_list.append((cube_rect, value))

        for cube_rect, value in self.cubes_list:
            pygame.draw.rect(self.screen, self.other_colour, cube_rect)
            #self.cubes_list.remove(cube_rect)
            text = self.fontti.render(str(value), True, (255, 255, 255))
            text_rect = text.get_rect(center=cube_rect.center)
            self.screen.blit(text, text_rect)

        pygame.display.update()
