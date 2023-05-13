import unittest
from gamecolours import Colours


class TestColours(unittest.TestCase):
    def setUp(self):
        self.colour = Colours()

    def test_if_light_colours_work_correctly(self):
        self.assertEqual(self.colour.colours_light[4] == (255, 160, 122), True)
