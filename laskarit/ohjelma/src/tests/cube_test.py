
import unittest
from entities.cube import Cube
class TestCube(unittest.TestCase):
    def setUp(self):
        self.cuube=Cube()

    def test_is_aloitusruutu_given_the_right_value(self):
        self.assertEqual(self.cuube.value, 2)


    def test_does_the_number_double_as_intended(self):
        self.cuube.cube_number_doubles()
        self.cuube.cube_number_doubles()
        self.assertEqual(self.cuube.value,8)

