
import pygame
from matrix import Matrix
from gamecolours import Colours
from ending import Ending


class Grid:

    '''Luokka, joka piirtää ruudukon.
        
        Attributes: 
                matrix: Matrix-luokan olio
                font: fontti
                cubes_list: sisältää laatat
                colour: Colours-luokan olio
                screen: näyttö
                game_over: tarkistaa onko peli ohi
                ending: Ending-luokan olio
                initialize_screen(): piirtää näytön
                
    '''

    def __init__(self, screen):

        '''Luokan konstruktori, joka alustaa luokan argumentit.
        
        Args: 
                matrix: Matrix-luokan olio
                font: fontti
                cubes_list: sisältää laatat
                colour: Colours-luokan olio
                screen: näyttö
                game_over: tarkistaa onko peli ohi
                ending: Ending-luokan olio
                initialize_screen(): piirtää näytön
                
        '''
        pygame.init()
        self.matrix = Matrix()
        self.font = pygame.font.SysFont("Comic Sans", 19)
        self.cubes_list = []
        self.colour = Colours()
        self.screen = screen
        self.game_over = False
        self.ending = Ending()
        self.initialize_screen()


    def run_loop(self):

        '''Luokan metodi, joka kutsuu draw-cubes- ja movement-metodeja. Sulkee pelin tarvittaessa.

        Args: 
                draw_cubes: metodi, joka piirtää laatat
                movement: metodi, joka kuvaa laattojen liikettä
        '''
        #self.start.start()
        while True:
            self.draw_cubes()
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
                self.checker()
            elif event.key == pygame.K_RIGHT:
                self.matrix.movement_right()
                self.checker()
            elif event.key == pygame.K_UP:
                self.matrix.movement_up()
                self.checker()
            elif event.key == pygame.K_DOWN:
                self.matrix.movement_down()
                self.checker()
            if self.game_over:
                self.ending.run=True
                self.ending.game_ends()
                if event.key == pygame.K_SPACE:
                    self.screen.fill((125, 158, 192))
                    self.matrix.initialize_game()
                    self.merge_done = [
                        [False for _ in range(4)] for _ in range(4)]
                    self.initialize_screen()

    def initialize_screen(self):

        '''Luokan metodi, joka alustaa näytön

        '''
        
        self.screen.fill((125, 158, 192))
        pygame.display.update()

    def draw_cubes(self):  # piirtääks tää koko ajan (piirtää endingnäytön päälle..)

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
                value = self.matrix.gridm[i][j]
                x_cord = j * (width + gap) + 20
                y_cord = i * (width + gap) + 20
                cube_rect = pygame.Rect(x_cord, y_cord, width, width)
                self.cubes_list.append((cube_rect, value))

        for cube_rect, value in self.cubes_list:
            if value != 0:
                pygame.draw.rect(
                    self.screen, self.colour.colours[value], cube_rect, 0, 6)
                text = self.font.render(str(value), True, (255, 255, 255))
                text_rect = text.get_rect(center=cube_rect.center)
                self.screen.blit(text, text_rect)
            if value == 0:
                pygame.draw.rect(
                    self.screen, (185, 211, 238), cube_rect, 0, 6)

        pygame.display.update()

    def checker(self):

        '''Luokan metodi, joka tarkistaa onko peli päättynyt.

        Jos peli on päättynyt, kutsuu Ending-luokan metodia.

        Args: 
                ending.game_ends: piirtää uuden näytön, jossa ohjeet aloittaa peli uudestaan
        '''
        
        for i in self.matrix.gridm:
            if 0 in i:
                return False
        for i in self.matrix.gridm:
            for j in range(3):
                if i[j] == i[j+1]:
                    return False
        for i in range(4):
            for j in range(3):
                if self.matrix.gridm[j][i] == self.matrix.gridm[j+1][i]:
                    return False
        else:
            self.game_over = True
            print("bepeep")
