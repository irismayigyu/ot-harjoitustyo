import random


class Matrix:
    def __init__(self):
        self.empty_cubes = []
        self.merge_done = False
        self.gridm = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.two_starter_cubes()
        self.start1=""
        self.start2=""

    def two_starter_cubes(self):
        self.start1 = (random.choice(range(0, 4)), random.choice(range(0, 4)))
        self.start2 = (random.choice(range(0, 4)), random.choice(range(0, 4)))
        while self.start1 == self.start2:
            self.start2 = (random.choice(range(0, 4)), random.choice(range(0, 4)))
        self.gridm[self.start1[0]][self.start1[1]] = 2
        self.gridm[self.start2[0]][self.start2[1]] = 2
        return self.start1,self.start2

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
                self.merge_done = False
            if len(self.empty_cubes) <= 0:
                self.game_ends()

    def game_ends(self):
        pass

    def movement_up(self):
        moved = False
        for j in range(4):
            for i in range(1, 4):
                if self.gridm[i][j] != 0:  # for cube in matrix
                    k = i
                    while k>0 and (self.gridm[k-1][j]==0 or self.gridm[k-1][j]==self.gridm[i][j]):
                        k -= 1  # one row higher
                    if k != i:
                        if self.gridm[k][j] == self.gridm[i][j] and not self.merge_done:
                            self.gridm[k][j] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done = True
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
                    while k<3 and (self.gridm[k+1][j]==0 or self.gridm[k+1][j]==self.gridm[i][j]):
                        k += 1
                    if k != i:
                        if self.gridm[k][j] == self.gridm[i][j] and not self.merge_done:
                            self.gridm[k][j] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done = True
                        else:
                            self.gridm[k][j] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                    moved = True
        if moved:
            self.new_spawning_cubes(moved)

    def movement_left(self):
        moved = False
        for i in range(4):
            for j in range(1, 4):
                if self.gridm[i][j] != 0 and (j == 0 or self.gridm[i][j-1] == 0):
                    k = j
                    while k>0 and (self.gridm[i][k-1]==0 or self.gridm[i][k-1]==self.gridm[i][j]):
                        k -= 1
                    if k != j:
                        if self.gridm[i][k] == self.gridm[i][j] and not self.merge_done:
                            self.gridm[i][k] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done = True
                        else:
                            self.gridm[i][k] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                        moved = True
        if moved:
            self.new_spawning_cubes(moved)

    def movement_right(self):
        moved = False
        for i in range(4):
            for j in range(2, -1, -1):
                if self.gridm[i][j] != 0 and (j == 3 or self.gridm[i][j+1] == 0):
                    k = j
                    while k<3 and (self.gridm[i][k+1]==0 or self.gridm[i][k+1]==self.gridm[i][j]):
                        k += 1
                    if k != j:
                        if self.gridm[i][k] == self.gridm[i][j] and not self.merge_done:
                            self.gridm[i][k] *= 2
                            self.gridm[i][j] = 0
                            self.merge_done = True
                        else:
                            self.gridm[i][k] = self.gridm[i][j]
                            self.gridm[i][j] = 0
                        moved = True
        if moved:
            self.new_spawning_cubes(moved)


# matriisi = Matrix()
# matriisi.two_starter_cubes()
# print(matriisi.gridm)
# matriisi.movement_up()
# print(matriisi.gridm)
# # matriisi.movement_down()
# # print(matriisi.gridm)
# # matriisi.movement_left()
# # print(matriisi.gridm)
# # matriisi.movement_right()
# # print(matriisi.gridm)
# # matriisi.movement_right()
# # print(matriisi.gridm)
# # matriisi.movement_left()
# # print(matriisi.gridm)
# # matriisi.movement_left()
# # print(matriisi.gridm)
# # matriisi.movement_up()
# # print(matriisi.gridm)
# # matriisi.movement_down()
# # print(matriisi.gridm)
# print("testi loppu")
