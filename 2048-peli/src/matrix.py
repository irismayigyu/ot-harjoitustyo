import random


class Matrix:
    def __init__(self):
        self.empty_cubes = []
        self.merge_done = [[False for _ in range(4)] for _ in range(4)]
        self.gridm = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.two_starter_cubes()
        self.start1 = ""
        self.start2 = ""

    def two_starter_cubes(self):
        self.start1 = (random.choice(range(0, 4)), random.choice(range(0, 4)))
        self.start2 = (random.choice(range(0, 4)), random.choice(range(0, 4)))
        while self.start1 == self.start2:
            self.start2 = (random.choice(range(0, 4)),
                           random.choice(range(0, 4)))
        self.gridm[self.start1[0]][self.start1[1]] = 2
        self.gridm[self.start2[0]][self.start2[1]] = 2
        return self.start1, self.start2

    def new_spawning_cubes(self, moved):
        if moved:
            self.empty_cubes = []
            for i in range(4):
                for j in range(4):
                    if self.gridm[i][j] == 0:
                        self.empty_cubes.append((i, j))
            if self.empty_cubes:
                new_cube = random.choice(self.empty_cubes)
                self.gridm[new_cube[0]][new_cube[1]] = 2
                self.empty_cubes.remove(new_cube)
                self.merge_done = [[False for _ in range(4)] for _ in range(4)]
            if len(self.empty_cubes) <= 0:
                self.game_ends()

    def game_ends(self):
        # self.grid.ending()
        pass

    def movement_up(self):
        moved = False
        for j in range(4):
            for i in range(1, 4):
                if self.gridm[i][j] != 0:
                    k = i
                    while k > 0 and (self.gridm[k-1][j] == 0 or self.gridm[k-1][j] == self.gridm[i][j]):
                        k -= 1
                    if k != i:
                        if self.gridm[k][j] == self.gridm[i][j] and not self.merge_done[k][j] == True \
                                and not self.merge_done[i][j] == True:
                            self.gridm[k][j] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done[k][j] = True
                        else:
                            self.gridm[k][j] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                        moved = True
        if moved:
            self.new_spawning_cubes(moved)

    def movement_down(self):
        moved = False
        for j in range(4):
            for i in range(2, -1, -1):
                if self.gridm[i][j] != 0:
                    k = i
                    while k < 3 and (self.gridm[k+1][j] == 0 or self.gridm[k+1][j] == self.gridm[i][j]):
                        k += 1
                    if k != i:
                        if self.gridm[k][j] == self.gridm[i][j] and not self.merge_done[k][j] == True \
                                and not self.merge_done[i][j] == True:
                            self.gridm[k][j] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done[k][j] = True
                        else:
                            self.gridm[k][j] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                    moved = True
        if moved:
            self.new_spawning_cubes(moved)

    def movement_left(self):
        moved = False
        for i in range(4):
            shift = 0
            for j in range(4):
                if self.gridm[i][j] == 0:
                    shift += 1
                elif shift > 0:
                    self.gridm[i][j-shift] = self.gridm[i][j]
                    self.gridm[i][j] = 0
                    moved = True
            for j in range(1, 4):
                if self.gridm[i][j-1] == self.gridm[i][j] and not self.merge_done[i][j-1] and not self.merge_done[i][j]:
                    self.gridm[i][j-1] *= 2
                    self.gridm[i][j] = 0
                    self.merge_done[i][j-1] = True
                    moved = True
        if moved:
            self.new_spawning_cubes(moved)

    def movement_right(self):
        moved = False
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if self.gridm[i][3-q] == 0:
                        shift += 1
                if shift > 0:
                    self.gridm[i][3-j+shift] = self.gridm[i][3-j]
                    self.gridm[i][3 - j] = 0
                    moved = True
                if 4-j+shift <= 3:
                    if self.gridm[i][4-j+shift] == self.gridm[i][3-j+shift] \
                            and not self.merge_done[i][4-j+shift] \
                            and not self.merge_done[i][3-j+shift]:
                        self.gridm[i][4-j+shift] *= 2
                        self.gridm[i][3-j+shift] = 0
                        self.merge_done[i][4-j+shift] = True
        if moved:
            self.new_spawning_cubes(moved)


matriisi = Matrix()
print(matriisi.gridm)
matriisi.movement_left()
print(matriisi.gridm)
matriisi.movement_right()
print(matriisi.gridm)
print("testi loppu")
