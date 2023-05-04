import random
from ending import Ending

class Matrix:

    '''Luokka, joka kuvaa ruudukon toimintaa

        Attributes: 
                    empty_cubes: lista kuvaa tyhjiä paikkoja ruudukossa
                    merge_done: lista kertoo onko jo jossain kohdassa tehty yhdistäminen
                    gridm: ruudukko
    '''

    def __init__(self):
        '''Luokan konstruktori, joka alustaa ruudukon 

        Args: 
                    empty_cubes: lista kuvaa tyhjiä paikkoja ruudukossa
                    merge_done: lista kertoo onko jo jossain kohdassa tehty yhdistäminen
                    gridm: ruudukko
        '''

        self.empty_cubes = []
        self.merge_done = [[False for _ in range(4)] for _ in range(4)]
        self.ending=Ending()
        self.gridm=self.ending.gridm
        # self.gridm = [[0 for _ in range(4)] for _ in range(4)]
        self.initialize_game()

    def initialize_game(self):
        self.empty_cubes = []
        self.merge_done = [[False for _ in range(4)] for _ in range(4)]
        # self.gridm = [[0, 0, 0, 0],
        #               [0, 0, 0, 0],
        #               [0, 0, 0, 0],
        #               [0, 0, 0, 0]]
        self.gridm = [[32, 16, 32, 64], #pelin päättymisen testausta varten
                [256, 8, 2, 4],
                [128, 2048, 8, 16],
                [8, 128, 16, 2]]
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
        self.gridm[start1[0]][start1[1]] = 2
        self.gridm[start2[0]][start2[1]] = 2
        return (start1, start2)  # testejä varten

    def new_cubes(self):
        '''Luokan metodi, joka luo uuden laatan satunnaiselle paikalla

        Args: 
                value: laatan arvo, joka on 90% ajasta 2 ja loput 4

        '''

        self.empty_cubes = []
        for i in range(4):
            for j in range(4):
                if self.gridm[i][j] == 0:
                    self.empty_cubes.append((i, j))
        if self.empty_cubes:
            new_cube = random.choice(self.empty_cubes)
            if random.randint(1, 10) == 10:
                value = 4
            else:
                value = 2
            self.gridm[new_cube[0]][new_cube[1]] = value
            self.empty_cubes.remove(new_cube)
            self.merge_done = [[False for _ in range(4)] for _ in range(4)]

    def movement_up(self):  # ylöspäin mergeäminen ei aina toimi
        '''Luokan metodi, joka määrittää liikkeen ylöspäin.

        Tarkistaa onko laatan yläpuolella tilaa tai onko yläpuolella olevalla laatalla sama arvo.
        Sitten siirtää ja/tai tekee yhdistyksen. Kutsuu uuden laatan luontia.

        Args: 
                spawn: kun on aihetta luoda uusi laatta

        '''

        spawn = False
        for j in range(4):
            for i in range(4):
                if self.gridm[i][j] != 0:
                    k = i
                    while k > 0 and (self.gridm[k-1][j] == 0
                                     or self.gridm[k-1][j] == self.gridm[i][j]):
                        k -= 1
                    if k != i:
                        if self.gridm[k][j] == self.gridm[i][j] \
                            and not self.merge_done[k][j] \
                                and not self.merge_done[i][j]:
                            self.gridm[k][j] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done[k][j] = True
                        else:
                            self.gridm[k][j] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                        spawn = True
        if 0 in self.gridm[3]:
            pass
        else:
            spawn = False
        if spawn:
            self.new_cubes()

    def movement_down(self):
        '''Luokan metodi, joka määrittää liikkeen alaspäin.

        Tarkistaa onko laatan yläpuolella tilaa tai onko yläpuolella olevalla laatalla sama arvo.
        Sitten siirtää ja/tai tekee yhdistyksen. Kutsuu uuden laatan luontia.

        Args: 
                spawn: kun on aihetta luoda uusi laatta

        '''
        spawn = False
        for j in range(4):
            for i in range(2, -1, -1):
                if self.gridm[i][j] != 0:
                    k = i
                    while k < 3 and (self.gridm[k+1][j] == 0
                                     or self.gridm[k+1][j] == self.gridm[i][j]):
                        k += 1
                    if k != i:
                        if self.gridm[k][j] == self.gridm[i][j] \
                            and not self.merge_done[k][j] \
                                and not self.merge_done[i][j]:
                            self.gridm[k][j] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done[k][j] = True
                        else:
                            self.gridm[k][j] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                        spawn = True

        if 0 in self.gridm[0]:
            pass
        else:
            spawn = False
        if spawn:
            self.new_cubes()

    def movement_left(self):
        '''Luokan metodi, joka määrittää liikkeen vasemmalle.

        Tarkistaa onko laatan vasemmalla puolella tilaa 
        tai onko vasemmalla puolella olevalla laatalla sama arvo.
        Sitten siirtää ja/tai tekee yhdistyksen. Kutsuu uuden laatan luontia.

        Args: 
                spawn: kun on aihetta luoda uusi laatta
        '''

        spawn = False
        for i in range(4):
            for j in range(4):
                if self.gridm[i][j] != 0:
                    k = j
                    while k > 0 and (self.gridm[i][k-1] == 0
                                     or self.gridm[i][k-1] == self.gridm[i][j]):
                        k -= 1
                    if k != j:
                        if self.gridm[i][k] == self.gridm[i][j] \
                                and not self.merge_done[i][k] and not self.merge_done[i][j]:
                            self.gridm[i][k] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done[i][k] = True
                        else:
                            self.gridm[i][k] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                        spawn = True
        if 0 in [row[3] for row in self.gridm]:
            pass
        else:
            spawn = False
        self.new_cubes() if spawn else None

    def movement_right(self):
        '''Luokan metodi, joka määrittää liikkeen oikealle.

        Tarkistaa onko laatan oikealla puolella tilaa 
        tai onko oikealla puolella olevalla laatalla sama arvo.
        Sitten siirtää ja/tai tekee yhdistyksen. Kutsuu uuden laatan luontia.

        Args: 
                spawn: kun on aihetta luoda uusi laatta

        '''

        spawn = False
        for i in range(4):
            for j in range(3, -1, -1):
                if self.gridm[i][j] != 0:
                    k = j
                    while k < 3 and (self.gridm[i][k+1] == 0 or self.gridm[i][k+1] == self.gridm[i][j]):
                        k += 1
                    if k != j:
                        if self.gridm[i][k] == self.gridm[i][j] \
                            and not self.merge_done[i][k] and not self.merge_done[i][j]:
                            self.gridm[i][k] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done[i][k] = True
                        else:
                            self.gridm[i][k] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                        spawn = True
        if 0 in [row[0] for row in self.gridm]:
            pass
        else:
            spawn = False
        self.new_cubes() if spawn else None


# me=Matrix()
# print(me.initialize_game())
