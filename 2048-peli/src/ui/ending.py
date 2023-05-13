import pygame


class Ending():

    '''Luokka, joka luo pelin päättymisnäytön

    Kertoo pelaajalle, että hän on hävinnyt sekä miten tämä voi aloittaa uuden pelin

    Argumentit:
                font: fontti
                screen: näyttö
                game_ends: luo ja piirtää päättymisnäytön

    '''

    def __init__(self):
        '''Luokan konstruktori, joka alustaa lopetuksen

        Args:
                    font: fontti
                    screen: näyttö
                    run: pitää lopetusnäyttöä yllä kunnes peslaaja painaa välilyöntiä

        '''
        self.font = pygame.font.SysFont("Comic Sans", 20)
        self.screen = pygame.display.set_mode((500, 400))
        self.run = True

    def game_ends(self, ending_matrix):
        '''Luokan metodi, joka luo ja piirtää päättysmisnäytön. Nollaa ruudukon

        Args:
                    you_lost: häviämisteksti
                    restart_instuctions: aloitusohjeet

        '''

        while self.run:
            self.screen.fill((155, 205, 155))
            you_lost = self.font.render("You Lost!", True, (0, 0, 0))
            restart_instructions = self.font.render(
                "Press space to restart", True, (0, 0, 0))
            self.screen.blit(you_lost, (200, 160))
            self.screen.blit(restart_instructions, (140, 210))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.run = False
                    ending_matrix = [[0 for x in range(4)] for y in range(4)]
                    self.screen.fill((125, 158, 192))
                    return ending_matrix
                if event.type == pygame.QUIT:
                    pygame.quit()
