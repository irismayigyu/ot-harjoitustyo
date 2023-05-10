
import unittest
from services.matrix import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_start1_and_start2_are_always_different(self):
        tuple = self.matrix.starting_cubes()
        self.assertEqual(tuple[0] !=
                         tuple[1], True)

    def test_if_movement_up_works_and_merging(self):
        self.matrix.grid = [[2, 0, 0, 0],
                            [0, 2, 8, 0],
                            [0, 2, 0, 0],
                            [0, 0, 0, 16]]
        self.matrix.movement_up()
        testup = [2, 4, 8, 16]
        self.assertEqual(self.matrix.grid[0] == testup, True)

    def test_if_movement_down_works_and_merging(self):
        self.matrix.grid = [[2, 0, 0, 0],
                            [0, 2, 16, 0],
                            [0, 2, 0, 0],
                            [0, 0, 0, 16]]
        self.matrix.movement_down()
        testup = [2, 4, 16, 16]
        self.assertEqual(self.matrix.grid[3] == testup, True)

    def test_if_movement_left_works(self):
        self.matrix.grid = [[2, 0, 0, 0],
                            [0, 2, 8, 0],
                            [0, 2, 0, 0],
                            [0, 0, 0, 0]]
        self.matrix.movement_left()
        testi = self.matrix.grid[0][0]+self.matrix.grid[1][0]\
            + self.matrix.grid[2][0]+self.matrix.grid[3][0]
        self.assertEqual(testi > 0, True)

    def test_if_movement_right_works(self):
        self.matrix.grid = [[0, 0, 0, 0],
                            [0, 2, 8, 0],
                            [0, 2, 0, 0],
                            [0, 0, 0, 0]]
        self.matrix.movement_right()
        testi = self.matrix.grid[0][3]+self.matrix.grid[1][3]\
            + self.matrix.grid[2][3]+self.matrix.grid[3][3]
        self.assertEqual(testi > 0, True)

    def test_if_merging_left_works(self):
        self.matrix.grid = [[0, 0, 2, 2],
                            [0, 2, 8, 0],
                            [0, 2, 0, 0],
                            [0, 0, 0, 0]]
        self.matrix.movement_left()
        self.assertEqual(self.matrix.grid[0][0] == 4, True)

    def test_if_merging_right_works(self):
        self.matrix.grid = [[0, 0, 2, 2],
                            [0, 2, 8, 0],
                            [0, 2, 0, 0],
                            [0, 0, 0, 0]]
        self.matrix.movement_right()
        self.assertEqual(self.matrix.grid[0][3] == 4, True)

    def test_if_starting_cubes_works(self):
        total = 0
        self.matrix.grid = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]]
        self.matrix.starting_cubes()
        for i in range(4):
            for j in range(4):
                total += self.matrix.grid[i][j]
        self.assertEqual(total < 8, True)

    def test_if_checker_senses_if_game_over(self):
        self.matrix.grid == [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
        self.assertEqual(self.matrix.checker() == False, True)

    def test_if_checker_senses_if_game_isnt_over(self):
        self.matrix.grid = [[32, 16, 32, 64],
                    [256, 8, 2, 4],
                    [128, 2048, 8, 16],
                    [8, 128, 2, 8]]
        self.assertEqual(self.matrix.checker() == True, True)
