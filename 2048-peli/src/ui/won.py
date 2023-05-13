
import pygame


class Won:
    def __init__(self):
        self.font = pygame.font.SysFont("Comic Sans", 17)
        self.screen = pygame.display.set_mode((500, 400))
        self.run = False

    def you_won(self, ending_matrix):
        while self.run:
            self.screen.fill((205, 170, 125))
            winner_message = self.font.render(
                "you won!! secret: for the next time you start playing,", True, (0, 0, 0))
            winner_message2 = self.font.render(
                "you can unlock weird tiles by pressing 7", True, (0, 0, 0))
            restart_instructions = self.font.render(
                "Start again by pressing space!", True, (0, 0, 0))
            self.screen.blit(winner_message, (34, 160))
            self.screen.blit(winner_message2, (50, 200))
            self.screen.blit(restart_instructions, (100, 260))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.run = False
                    ending_matrix = [[0 for x in range(4)] for y in range(4)]
                    self.screen.fill((125, 158, 192))
                    return ending_matrix
                if event.type == pygame.QUIT:
                    pygame.quit()
