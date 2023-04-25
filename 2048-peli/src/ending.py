import pygame
class Ending():

    def __init__(self, screen):
        self.backround_colour_blue = (125, 158, 192)
        self.font = pygame.font.SysFont("Comic Sans", 19)
        self.screen = screen

    def game_ends(self):
        self.screen.fill(self.backround_colour_blue)
        text = self.font.render("You Lost!", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.screen.center)
        self.screen.blit(text, text_rect)
        pygame.display.update()
        