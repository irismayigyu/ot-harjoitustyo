
import pygame
from matrix import Matrix
from gamecolours import Colours


class Grid:
    def __init__(self, screen):
        self.matrix = Matrix()
        self.backround_colour_blue = (125, 158, 192)
        self.cube_colour_rose = (238, 169, 184)
        self.empty_cube_colour = (185, 211, 238)
        self.font = pygame.font.SysFont("Comic Sans", 19)
        self.cubes_list = []
        self.colour = Colours()
        self.screen = screen
        self.initialize_grid()

    def run_loop(self):
        while True:
            self.draw_cubes()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                else:
                    self.movement(event)

    def movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.matrix.movement_left()
            elif event.key == pygame.K_RIGHT:
                self.matrix.movement_right()
            elif event.key == pygame.K_UP:
                self.matrix.movement_up()
            elif event.key == pygame.K_DOWN:
                self.matrix.movement_down()

    def initialize_grid(self):
        self.screen.fill(self.backround_colour_blue)
        pygame.display.update()

    def draw_cubes(self):
        self.cubes_list = []
        gap_size = 20
        width = 75
        for i in range(4):
            for j in range(4):
                value = self.matrix.gridm[i][j]
                x_cord = j * (width + gap_size) + 20
                y_cord = i * (width + gap_size) + 20
                cube_rect = pygame.Rect(x_cord, y_cord, width, width)
                self.cubes_list.append((cube_rect, value))

        for cube_rect, value in self.cubes_list:
            if value != 0:
                pygame.draw.rect(
                    self.screen, self.colour.colours[value], cube_rect, 0, 6)
                text = self.font.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=cube_rect.center)
                self.screen.blit(text, text_rect)
            if value == 0:
                pygame.draw.rect(
                    self.screen, self.empty_cube_colour, cube_rect, 0, 6)

        pygame.display.update()
