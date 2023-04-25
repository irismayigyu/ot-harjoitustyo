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
        self.assertEqual(sum(self.matrix.gridm[0]) > 0, True)

    def test_if_movement_down_works(self):
        self.matrix.two_starter_cubes()
        self.matrix.movement_down()
        self.assertEqual(sum(self.matrix.gridm[3]) > 0, True)

    def test_if_movement_left_works(self):
        self.matrix.two_starter_cubes()
        self.matrix.movement_left()
        testi=self.matrix.gridm[0][0]+self.matrix.gridm[1][0]\
            +self.matrix.gridm[2][0]+self.matrix.gridm[3][0]
        self.assertEqual(testi>0, True)

    def test_if_movement_right_works(self):
        self.matrix.two_starter_cubes()
        self.matrix.movement_right()
        testi=self.matrix.gridm[0][3]+self.matrix.gridm[1][3]\
            +self.matrix.gridm[2][3]+self.matrix.gridm[3][3]
        self.assertEqual(sum(self.matrix.gridm[0])>0, True)


    
