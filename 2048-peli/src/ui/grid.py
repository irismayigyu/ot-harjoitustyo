
import pygame
from gamecolours import Colours
from ui.ending import Ending
from handle_highscore import HandleHighscore
from ui.won import Won


class Grid:

    '''Luokka, joka piirtää ruudukon.

        Attributes: 
                matrix: Matrix-luokan olio
                font : fontti
                cubes_list: sisältää laatat
                colour: Colours-luokan olio
                screen: näyttö
                game_over: tarkistaa onko peli ohi
                ending: Ending-luokan olio
                initialize_screen(): piirtää näytön

    '''

    def __init__(self, screen, matrix):
        '''Luokan konstruktori, joka alustaa luokan argumentit.

        Args: 
                matrix: Matrix-luokan matrix
                font : fontti
                cubes_list: sisältää laatat
                colour: Colours-luokan olio
                screen: näyttö
                game_over: tarkistaa onko peli ohi
                ending: Ending-luokan olio
                hscore: HandleHighscore-luokan olio
                initialize_screen(): piirtää näytön
                self.highscore: highscore
                self.init_high: alustettu highscore

        '''

        self.matrix = matrix
        self.font = pygame.font.SysFont("Comic Sans", 17)
        self.cubes_list = []
        self.colour = Colours()
        self.screen = screen
        self.won = Won()
        self.ending_matrix = [[0 for _ in range(4)] for _ in range(4)]
        self.ending = Ending()
        self.hscore = HandleHighscore()
        self.highscore = self.hscore.initialize_highscore()
        self.init_high = self.hscore.initialize_init_high()

    def run_loop(self):
        '''Luokan metodi, joka kutsuu draw-cubes- ja movement-metodeja. Sulkee pelin tarvittaessa.

        Args: 
                draw_cubes: metodi, joka piirtää laatat
                movement: metodi, joka kuvaa laattojen liikettä
        '''
        is_running = True
        while is_running:
            self.screen.fill((125, 158, 192))
            self.initialize_screen()
            self.draw_cubes()

            if self.matrix.score >= self.highscore:
                self.highscore = self.matrix.score
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    pygame.quit()
                    exit()
                else:
                    self._movement(event)

    def _movement(self, event):
        '''Luokan metodi, kuvaa laattojen liikkumista graaffisesti. 
        Nuolinäppäinten käyttö kutsuu Matrix-olion movement-metodeja. Jos peli on ohi
        ja painetaan välilyöntiä niin se alkaa uudestaan

        Args: 
                checker: metodi, joka tarkistaa onko peli päättynyt
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.matrix.movement_left()
            elif event.key == pygame.K_RIGHT:
                self.matrix.movement_right()
            elif event.key == pygame.K_UP:
                self.matrix.movement_up()
            elif event.key == pygame.K_DOWN:
                self.matrix.movement_down()
            self.matrix.win_checker()
            if self.matrix.game_won:
                won = True
                self.restart_game(won)
            self.matrix.checker()
            if self.matrix.game_over:
                won = False
                self.restart_game(won)

    def restart_game(self, won):
        self.ending_matrix = self.matrix.grid
        if not won:
            self.ending.run = True
            self.matrix.game_over = False
            self.matrix.grid = self.ending.game_ends(
                self.ending_matrix)
            if self.highscore > self.init_high:
                self.init_high = self.hscore.update(self.highscore)
        else:
            self.won.run = True
            self.matrix.game_won = False
            self.matrix.grid = self.won.you_won(
                self.ending_matrix)
            self.highscore = 2048
            self.init_high = self.hscore.update(2048)

        self.count = 0
        self.matrix.score = 0
        self.matrix.starting_cubes()
        self.initialize_screen()

    def initialize_screen(self):
        '''Luokan metodi, joka alustaa näytön

        '''
        highscore_text = self.font .render("High score", True, (0, 0, 0))
        self.screen.blit(highscore_text, (390, 130))
        score_text = self.font .render("Score", True, (0, 0, 0))
        self.screen.blit(score_text, (410, 200))
        self._score()

    def _score(self):
        highscore_number = self.font .render(
            str(self.highscore), True, (0, 0, 0))
        score_number = self.font .render(
            str(self.matrix.score), True, (0, 0, 0))
        self.screen.blit(highscore_number, (430, 160))
        self.screen.blit(score_number, (430, 235))

    def choose_colour(self, dark, weird):
        '''Luokan metodi, määrittää laattojen värit

        '''
        if dark:
            self.colour.colours = self.colour.colours_dark
        elif weird:
            self.colour.colours = self.colour.colours_weird
        else:
            self.colour.colours = self.colour.colours_light

    def draw_cubes(self):
        '''Luokan metodi, piirtää laatat ja kirjaa niihin niiden arvot

        Args: 
                gap: laattojen välisen välin pituus
                width: laattojen leveys ja korkeus
                x_cord: laatan x-kordinaatti
                y_cord: laatan y-kordinaatti

        '''
        self.cubes_list = []
        gap = 20
        width = 75
        for i in range(4):
            for j in range(4):
                value = self.matrix.grid[i][j]
                x_cord = j * (width + gap) + 20
                y_cord = i * (width + gap) + 20
                cube_rect = pygame.Rect(x_cord, y_cord, width, width)
                self.cubes_list.append((cube_rect, value))

        for cube_rect, value in self.cubes_list:
            if value != 0 and not value == 2048:
                pygame.draw.rect(
                    self.screen, self.colour.colours[value], cube_rect, 0, 6)
                text = self.font .render(str(value), True, (255, 255, 255))
                text_rect = text.get_rect(center=cube_rect.center)
                self.screen.blit(text, text_rect)
            if value == 0:
                pygame.draw.rect(
                    self.screen, (185, 211, 238), cube_rect, 0, 6)
