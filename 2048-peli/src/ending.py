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
                    game_ends: luo päättymisnäytön
                
        '''
    
        self.font = pygame.font.SysFont("Comic Sans", 20)
        self.screen = pygame.display.set_mode((400, 400))
        self.game_ends()

    def game_ends(self):

        '''Luokan metodi, joka luo ja piirtää päättysmisnäytön

        Args:
                    you_lost: häviämisteksti
                    restart_instuctions: aloitusohjeet
                
        '''

        self.screen.fill((155, 205, 155))
        you_lost = self.font.render("You Lost!", True, (0, 0, 0))
        restart_instructions = self.font.render(
            "Press space to restart", True, (0, 0, 0))
        self.screen.blit(you_lost, (130, 130))
        self.screen.blit(restart_instructions, (70, 200))

        pygame.display.update()
