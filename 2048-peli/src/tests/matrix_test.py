import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_start1_and_start2_are_always_different(self):
        tuple = self.matrix.two_starter_cubes()
        self.assertEqual(tuple[0] !=
                         tuple[1], True)

    def test_if_movement_up_works(self):
        self.matrix.two_starter_cubes()
        self.matrix.movement_up()
        self.assertEqual(sum(self.matrix.gridm[0])>0, True)

    def test_if_movement_down_works(self):
        self.matrix.two_starter_cubes()
        self.matrix.movement_up()
        self.assertEqual(sum(self.matrix.gridm[3])>0, True)

    # def test_if_movement_left_works(self):
    #     self.matrix.two_starter_cubes()
    #     self.matrix.movement_up()
    #     self.assertEqual(sum(self.matrix.gridm[0])>0, True)

    # def test_if_movement_right_works(self):
    #     self.matrix.two_starter_cubes()
    #     self.matrix.movement_up()
    #     self.assertEqual(sum(self.matrix.gridm[0])>0, True)
