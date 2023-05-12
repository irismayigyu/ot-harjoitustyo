
import pygame
from gamecolours import Colours
from ui.ending import Ending
from . import get_hs, insert_in_table
# from database_connection import get_database_connection


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

    def __init__(self, screen, matrix, connection):
        '''Luokan konstruktori, joka alustaa luokan argumentit.

        Args: 
                matrix: Matrix-luokan matrix
                font : fontti
                cubes_list: sisältää laatat
                colour: Colours-luokan olio
                screen: näyttö
                game_over: tarkistaa onko peli ohi
                count: pitää huolen että score-tekstit piirretään vain kerran kerralla. 
                ending: Ending-luokan olio
                initialize_screen(): piirtää näytön

        '''

        self.matrix = matrix
        self.font = pygame.font.SysFont("Comic Sans", 17)
        self.cubes_list = []
        self.colour = Colours()
        self.screen = screen
        self.ending_matrix = [[0 for _ in range(4)] for _ in range(4)]
        self._connection = connection
        self.ending = Ending(self._connection)
        self.highscore = 0
        self.init_high = get_hs()
        if self.init_high is not None:
            self.highscore = self.init_high

    # def get_hs(self):
    #     cursor = self._connection.cursor()
    #     cursor.execute(
    #         "SELECT h.result FROM Highscores h ORDER BY result DESC LIMIT 1;")
    #     rows = cursor.fetchall()
    #     if rows:
    #         return rows[0][0]
    #     else:
    #         return 0

    def run_loop(self):
        '''Luokan metodi, joka kutsuu draw-cubes- ja movement-metodeja. Sulkee pelin tarvittaessa.

        Args: 
                draw_cubes: metodi, joka piirtää laatat
                movement: metodi, joka kuvaa laattojen liikettä
        '''
        while True:
            self.screen.fill((125, 158, 192))
            self.initialize_screen()
            self.draw_cubes()
            pygame.display.update()

            if self.matrix.score >= self.highscore:
                self.highscore = self.matrix.score

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                else:
                    self.movement(event)

    def movement(self, event):
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
            self.matrix.checker()
            if self.matrix.game_over:
                self.restart_game()

    def restart_game(self):
        # cursor = self._connection.cursor()
        # cursor.execute("INSERT INTO Highscores (result) VALUES (?)", [
        #                self.highscore])
        # self._connection.commit()

        # cursor.execute("SELECT * FROM Highscores")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        # self._connection.commit()
        insert_in_table()
        self.ending_matrix = self.matrix.grid
        self.ending.run = True
        self.matrix.game_over = False
        self.count = 0
        self.matrix.score = 0

        if self.highscore > self.init_high:
            self.init_high = self.highscore
        self.matrix.grid = self.ending.game_ends(self.ending_matrix)

        self.matrix.starting_cubes()
        self.initialize_screen()

    def initialize_screen(self):
        '''Luokan metodi, joka alustaa näytön

        '''
        highscore_text = self.font .render("High score", True, (0, 0, 0))
        self.screen.blit(highscore_text, (390, 130))
        score_text = self.font .render("Score", True, (0, 0, 0))
        self.screen.blit(score_text, (410, 200))
        self.score()

    def score(self):
        highscore_number = self.font .render(
            str(self.highscore), True, (0, 0, 0))
        score_number = self.font .render(
            str(self.matrix.score), True, (0, 0, 0))
        self.screen.blit(highscore_number, (430, 160))
        self.screen.blit(score_number, (430, 235))

    def choose_colour(self, dark, weird):
        if dark:
            self.colour.colours = self.colour.colours_dark
        elif weird:
            self.colour.colours = self.colour.colours_weird
        else:
            self.colour.colours = self.colour.colours_light

    def draw_cubes(self):
        '''Luokan metodi, piirtää laatat ja kirjaa niihin niiden arvot.

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
            if value != 0:
                pygame.draw.rect(
                    self.screen, self.colour.colours[value], cube_rect, 0, 6)
                text = self.font .render(str(value), True, (255, 255, 255))
                text_rect = text.get_rect(center=cube_rect.center)
                self.screen.blit(text, text_rect)
            if value == 0:
                pygame.draw.rect(
                    self.screen, (185, 211, 238), cube_rect, 0, 6)
