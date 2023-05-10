import pygame
from ui.grid import Grid
from services.matrix import Matrix


class Start():

    '''Luokka, joka luo pelin aloitusnäytön

    Kertoo pelaajalle, että hän on hävinnyt sekä miten tämä voi aloittaa uuden pelin

    Argumentit:
                font: fontti
                screen: näyttö
                start_run: muuttuja, joka määrittää looppaamisen kunnes peli alkaa
                matrix: Matrix-luokan olio
                grid: Grid-luokan olio

    '''

    def __init__(self):
        '''Luokan konstruktori, joka alustaa aloituksen

        Args:
                font: fontti
                screen: näyttö
                start_run: muuttuja, joka määrittää looppaamisen kunnes peli alkaa
                matrix: Matrix-luokan olio
                grid: Grid-luokan olio

        '''
        #pygame.init()
        self.font = pygame.font.SysFont("Comic Sans", 16)
        self.screen = pygame.display.set_mode((500, 400))
        self.start_run = True
        self.matrix = Matrix()
        self.grid = Grid(self.screen, self.matrix)

    def start_loop(self):
        '''Luokan konstruktori, joka alustaa aloituksen

        Args:
                welcome: tervetuloa-teksti
                rules: pelin säännöt-teksti
                start_instructions: miten peli aloitetaan-teksti
                choose_colour: miten valitaan väri-teksti
                dark: muuttuja, joka kertoo onko tummat laatat valittu
                weird: muuttuja, joka kertoo onko oudot laatat valittu
                chose_dark: tummat laatat valittu-teksti
                chose_weird: oudot laatat valittu-teksti

        '''

        self.screen.fill((155, 205, 155))
        welcome = self.font.render("Welcome to 2048 :)", True, (0, 0, 0))
        rules = self.font.render(
            "Merge the cubes until you reach 2048!", True, (0, 0, 0))
        start_instructions = self.font.render(
            "Press enter to start", True, (0, 0, 0))
        choose_colour = self.font.render(
            "Press 1 for dark mode tiles or ? for weirder colour tiles", True, (0, 0, 0))
        self.screen.blit(welcome, (170, 150))
        self.screen.blit(rules, (100, 175))
        self.screen.blit(start_instructions, (170, 327))
        self.screen.blit(choose_colour, (52, 360))
        pygame.display.update()

        dark = False
        weird = False

        while self.start_run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        dark = True
                        weird = False
                        pygame.draw.rect(
                            self.screen, (155, 205, 155), (75, 225, 400, 30))
                        chose_dark = self.font.render(
                            "You chose dark, press 2 for normal pastel tiles", True, (0, 0, 0))
                        self.screen.blit(chose_dark, (80, 230))

                    elif event.key == pygame.K_7:
                        weird = True
                        dark = False
                        pygame.draw.rect(
                            self.screen, (155, 205, 155), (75, 225, 400, 30))
                        chose_weird = self.font.render(
                            "You chose weird, press 2 for normal pastel tiles", True, (0, 0, 0))
                        self.screen.blit(chose_weird, (80, 230))

                    elif event.key == pygame.K_RETURN:
                        self.start_run = False
                        self.screen.fill((125, 158, 192))
                        self.grid.initialize_screen()
                        self.grid.choose_colour(dark, weird)
                        self.grid.run_loop()

                    elif event.key == pygame.K_2 and (dark or weird):
                        dark = False
                        weird = False
                        pygame.draw.rect(
                            self.screen, (155, 205, 155), (75, 225, 400, 30))
                elif event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
