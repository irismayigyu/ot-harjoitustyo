import pygame
from griddrawing import Grid
from matrix import Matrix


class Start():

    '''Luokka, joka luo pelin aloitusnäytön

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
        pygame.init()
        self.font = pygame.font.SysFont("Comic Sans", 16)
        self.screen = pygame.display.set_mode((400, 400))
        self.start_run=True
        self.matrix=Matrix()
        self.grid=Grid(self.screen)

    def start(self):

        '''Luokan metodi, joka luo ja piirtää päättysmisnäytön

        Args:
                    you_lost: häviämisteksti
                    restart_instuctions: aloitusohjeet
                
        '''

        self.screen.fill((155, 205, 155))
        welcome = self.font.render("Welcome to 2048 :)", True, (0, 0, 0))
        rules = self.font.render(
            "Merge the cubes until you reach 2048!", True, (0, 0, 0))
        start_instructions = self.font.render(
            "Press enter to start", True, (0, 0, 0))
        self.screen.blit(welcome, (120, 130))
        self.screen.blit(rules, (50, 155))
        self.screen.blit(start_instructions, (120, 210))

        pygame.display.update()

        while self.start_run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.start_run = False
                    self.screen.fill((125, 158, 192))
                    self.matrix.initialize_game()
                    self.grid.run_loop()
                if event.type == pygame.QUIT:
                    pygame.quit()

alotus=Start()
alotus.start()