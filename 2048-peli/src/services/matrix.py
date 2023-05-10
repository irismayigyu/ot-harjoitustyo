import random


class Matrix:

    '''Luokka, joka kuvaa ruudukon toimintaa

        Attributes: 
                    empty_cubes: lista kuvaa tyhjiä paikkoja ruudukossa
                    merge_done: lista kertoo onko jo jossain kohdassa tehty yhdistäminen
                    grid: ruudukko
    '''

    def __init__(self):
        '''Luokan konstruktori, joka alustaa ruudukon 

        Args: 

                    initialize_game(): funktio alustaa tyhjän ruudukon

        '''
        self.score = 0
        self.spawn = False
        self.empty_cubes = []
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.merge_done = [[False for _ in range(4)] for _ in range(4)]
        self.game_over = False
        self.initialize_game()

    def initialize_game(self):
        self.empty_cubes = []
        self.merge_done = [[False for _ in range(4)] for _ in range(4)]
        self.grid  = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        # self.grid = [[32, 16, 32, 64],  # pelin päättymisen testausta varten
        #              [256, 8, 2, 4],
        #              [128, 2048, 2, 2],
        #              [2, 2, 2, 2]]
        self.starting_cubes()

    def starting_cubes(self):
        '''Luokan metodi, joka asettaa kaksi aloituslaattaa satunnaisille paikoille

        Args: 
                start1: ensimmäinen laatta
                start2: toinen laatta

        '''

        start1 = (random.choice(range(0, 4)), random.choice(range(0, 4)))
        start2 = (random.choice(range(0, 4)), random.choice(range(0, 4)))
        while start1 == start2:
            start2 = (random.choice(range(0, 4)),
                      random.choice(range(0, 4)))
        self.grid[start1[0]][start1[1]] = 2
        self.grid[start2[0]][start2[1]] = 2
        return (start1, start2)  # testejä varten

    def new_cubes(self):
        '''Luokan metodi, joka luo uuden laatan satunnaiselle paikalla

        Args: 
                value: laatan arvo, joka on 90% ajasta 2 ja loput 4

        '''

        self.empty_cubes = []
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    self.empty_cubes.append((i, j))
        if self.empty_cubes:
            new_cube = random.choice(self.empty_cubes)
            if random.randint(1, 10) == 10:
                value = 4
            else:
                value = 2
            self.grid[new_cube[0]][new_cube[1]] = value
            self.empty_cubes.remove(new_cube)
            self.merge_done = [[False for _ in range(4)] for _ in range(4)]

    def checker(self):  # matrix
        '''Luokan metodi, joka tarkistaa onko peli päättynyt.

        Jos peli on päättynyt, game_over muuttuja muuttuu.

        Args: 
                game_over: boolean-kertoo kun peli on ohi
        '''

        for i in self.grid:
            if 0 in i:
                return False
        for i in self.grid:
            for j in range(3):
                if i[j] == i[j+1]:
                    return False
        for i in range(4):
            for j in range(3):
                if self.grid[j][i] == self.grid[j+1][i]:
                    return False

        self.game_over = True
        return True

    def movement_up(self):
        '''Luokan metodi, joka määrittää liikkeen ylöspäin.

        Etsii ruudukon epätyhjät laatat ja kutsuu metodia, joka tarkistaa onko ylempänä
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.
        Kutsuu uuden laatan luomista jos siihen on aihetta.


        Args: 
                spawn: kun on aihetta luoda uusi laatta
                get_next_tile_up: arkistaa onko ylempänä tyhjä tai samanarvoinen laatta 
                ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        '''
        self.spawn = False
        for j in range(4):
            for i in range(4):
                if self.grid[i][j] != 0:
                    self.grid = self.get_next_tile_up(i, j)
        if 0 in self.grid[3]:
            pass
        else:
            self.spawn = False
        if self.spawn:
            self.new_cubes()

    def get_next_tile_up(self, i, j):
        '''Luokan metodi, joka tarkistaa onko ylempänä
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        Args:
            changes_up_and_down: tekee liikkeen ja/tai yhdistämisen'''

        k = i
        while k > 0 and (self.grid[k-1][j] == 0 or self.grid[k-1][j] == self.grid[i][j]):
            k -= 1
        if k != i:
            self.grid = self.changes_up_and_down(k, i, j)
            self.spawn = True
        return self.grid

    def movement_down(self):
        '''Luokan metodi, joka määrittää liikkeen alaspäin.

        Etsii ruudukon epätyhjät laatat ja kutsuu metodia, joka tarkistaa onko alempana
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.
        Kutsuu uuden laatan luomista jos siihen on aihetta.


        Args: 
                spawn: kun on aihetta luoda uusi laatta
                get_next_tile_down: arkistaa onko alempana tyhjä tai samanarvoinen laatta 
                ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        '''
        self.spawn = False
        for j in range(4):
            for i in range(2, -1, -1):
                if self.grid[i][j] != 0:
                    self.grid = self.get_next_tile_down(i, j)

        if 0 in self.grid[0]:
            pass
        else:
            self.spawn = False
        if self.spawn:
            self.new_cubes()

    def get_next_tile_down(self, i, j):
        '''Luokan metodi, joka tarkistaa onko alempana
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        Args:
            changes_up_and_down: tekee liikkeen ja/tai yhdistämisen'''

        k = i
        while k < 3 and (self.grid[k+1][j] == 0
                         or self.grid[k+1][j] == self.grid[i][j]):
            k += 1
        if k != i:
            self.grid = self.changes_up_and_down(k, i, j)
            self.spawn = True
        return self.grid

    def changes_up_and_down(self, k, i, j):
        '''Luokan metodi, joka määrittelee ja tekee liikkeen ja/tai yhdistämisen ylös ja alas'''

        if self.grid[k][j] == self.grid[i][j] \
            and not self.merge_done[k][j] \
                and not self.merge_done[i][j]:
            self.grid[k][j] *= 2
            self.grid[i][j] = 0
            self.merge_done[k][j] = True
            self.score += self.grid[k][j]
        else:
            self.grid[k][j] = self.grid[i][j]
            self.grid[i][j] = 0
        return self.grid

    def movement_left(self):
        '''Luokan metodi, joka määrittää liikkeen vasemmalle.

        Etsii ruudukon epätyhjät laatat ja kutsuu metodia, joka tarkistaa onko vasemmalla
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.
        Kutsuu uuden laatan luomista jos siihen on aihetta.


        Args: 
                spawn: kun on aihetta luoda uusi laatta
                get_next_tile_left: arkistaa onko vasemmalla tyhjä tai samanarvoinen laatta 
                ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        '''

        self.spawn = False
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] != 0:
                    self.grid = self.get_next_tile_left(i, j)
        if 0 in [row[3] for row in self.grid]:
            pass
        else:
            self.spawn = False
        result = self.new_cubes() if self.spawn else None
        return result

    def get_next_tile_left(self, i, j):
        '''Luokan metodi, joka tarkistaa onko vasemmalla
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        Args:
            changes_left_and_right: tekee liikkeen ja/tai yhdistämisen'''

        k = j
        while k > 0 and (self.grid[i][k-1] == 0
                         or self.grid[i][k-1] == self.grid[i][j]):
            k -= 1
        if k != j:
            self.grid = self.changes_left_and_right(k, i, j)
            self.spawn = True
        return self.grid

    def movement_right(self):
        '''Luokan metodi, joka määrittää liikkeen oikealle.

        Etsii ruudukon epätyhjät laatat ja kutsuu metodia, joka tarkistaa onko oikealla
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.
        Kutsuu uuden laatan luomista jos siihen on aihetta.


        Args: 
                spawn: kun on aihetta luoda uusi laatta
                get_next_tile_right: arkistaa onko oikealla tyhjä tai samanarvoinen laatta 
                ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        '''

        self.spawn = False
        for i in range(4):
            for j in range(3, -1, -1):
                if self.grid[i][j] != 0:
                    self.grid = self.get_next_tile_right(i, j)
        if 0 in [row[0] for row in self.grid]:
            pass
        else:
            self.spawn = False
        result = self.new_cubes() if self.spawn else None
        return result

    def get_next_tile_right(self, i, j):
        '''Luokan metodi, joka tarkistaa onko oikealla
        tyhjä tai samanarvoinen laatta ja suorittaa tarvittaessa liikkeen ja/tai yhdistämisen.

        Args:
            changes_up_and_down: tekee liikkeen ja/tai yhdistämisen'''
        k = j
        while k < 3 and (self.grid[i][k+1] == 0
                         or self.grid[i][k+1] == self.grid[i][j]):
            k += 1
        if k != j:
            self.grid = self.changes_left_and_right(k, i, j)
            self.spawn = True
        return self.grid

    def changes_left_and_right(self, k, i, j):
        '''Luokan metodi, joka määrittelee ja tekee liikkeen ja/tai yhdistämisen sivuille'''

        if self.grid[i][k] == self.grid[i][j] \
                and not self.merge_done[i][k] and not self.merge_done[i][j]:
            self.grid[i][k] *= 2
            self.grid[i][j] = 0
            self.merge_done[i][k] = True
            self.score += self.grid[i][k]
        else:
            self.grid[i][k] = self.grid[i][j]
            self.grid[i][j] = 0
        return self.grid
