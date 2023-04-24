
import pygame
from matrix import Matrix


class Grid:
    def __init__(self, screen):
        self.matrix = Matrix()
        self.gridm = self.matrix.gridm
        self.backround_colour_blue = (125,158,192)
        self.cube_colour_rose = (238,169,184)
        self.empty_cube_colour = (185,211,238)
        self.font = pygame.font.SysFont("Comic Sans", 19)
        self.width = 75
        self.cubes_list=[]
        self.screen = screen
        self.grid_rectangles=[]
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

    # def ending(self):
    #     self.screen.fill(self.backround_colour_blue)
    #     text = self.font.render("You Lost!", True, (255, 255, 255))
    #     text_rect = text.get_rect(center=self.screen.center)
    #     self.screen.blit(text, text_rect)
    #     pygame.display.update()


    def initialize_grid(self):
        # for i in range(4):
        #     for j in range(4):
        #         cordinates = (j*95+20, i*95+20)
        #         self.cuberectangle = pygame.Rect(cordinates, (75, 75))
        #         self.grid_rectangles.append(self.cuberectangle)
        self.screen.fill(self.backround_colour_blue)
        #for i in self.grid_rectangles:
        #    pygame.draw.rect(self.screen, self.colourr, i, 0, 10)
        pygame.display.update()

    def draw_cubes(self):
        self.cubes_list=[]
        gap_size = 20
        for i in range(4):
            for j in range(4):
                value = self.gridm[i][j]
                x_cord = j * (self.width + gap_size) + 20
                y_cord = i * (self.width + gap_size) + 20
                cube_rect = pygame.Rect(x_cord, y_cord, self.width, self.width)
                self.cubes_list.append((cube_rect, value))

        for cube_rect, value in self.cubes_list:
            if value!=0:
                pygame.draw.rect(self.screen, self.cube_colour_rose, cube_rect, 0, 6)
                text = self.font.render(str(value), True, (255, 255, 255))
                text_rect = text.get_rect(center=cube_rect.center)
                self.screen.blit(text, text_rect)
            if value==0:
                pygame.draw.rect(self.screen, self.empty_cube_colour, cube_rect, 0, 6)

        pygame.display.update()
