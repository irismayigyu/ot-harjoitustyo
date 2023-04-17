
import pygame
from matrix import Matrix


class Grid:
    def __init__(self, screen):
        self.matrix = Matrix()
        self.gridm = self.matrix.gridm
        self.colour = (255, 250, 205)
        self.other_colour = (205, 140, 149)
        self.fontti = pygame.font.SysFont("Comic Sans", 19)
        self.leveys = 90
        # self.cubes_list=[]
        self.screen = screen

    def run_loop(self):
        self.screen.fill((200, 200, 200))
        while True:
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
            self.draw_grid()

    def draw_cube(self, x_cordinate, y_cordinate):
        pygame.draw.rect(self.screen, self.colour, [
                         x_cordinate, y_cordinate, self.leveys, self.leveys], 3, 10)

    def draw_grid(self):
        y_cordinate = 0
        for i in range(4):
            x_cordinate = 0
            for j in range(4):
                if self.gridm[i][j] != 0:
                    # self.cubes_list.append(self.gridm[i][j])
                    self.draw_cube(x_cordinate, y_cordinate)
                x_cordinate += self.leveys
            y_cordinate += self.leveys
        pygame.display.update()
