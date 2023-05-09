import unittest
from grid import Grid
from matrix import Matrix
from ui.start import Start
from handle_highscore import HandleHighscore


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()
        self.start = Start()
        self.grid = Grid(self.start.screen, self.matrix)
        self.handlehs = HandleHighscore()

    def test_if_checker_senses_if_game_over(self):
        self.matrix.grid == [[0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0]]
        self.assertEqual(self.grid.checker() == False, True)

    def test_if_checker_senses_if_game_isnt_over(self):
        self.matrix.grid = [[32, 16, 32, 64],
                            [256, 8, 2, 4],
                            [128, 2048, 8, 16],
                            [8, 128, 2, 8]]
        self.assertEqual(self.grid.checker() == True, True)

    # def test_if_update_works(self):
    #     self.handlehscore.init_high=1300
    #     self.handlehscore.highscore=1304
    #     self.handlehscore.update()
    #     self.assertEqual(self.handlehscore.init_high== self.handlehscore.highscore, True)

    # def test_if_restaring_works(self): #miten testaan jos metodissä on graafisia piirteitä?
    #     self.matrix.score=69
    #     self.grid.restart_game()
    #     self.assertEqual(self.matrix.score==0, True)
