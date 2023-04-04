import unittest
from grid import Grid
class TestGrid(unittest.TestCase):
    def setUp(self):
        self.ruudukko=Grid()

    def test_aloituspaikka1_and_aloituspaikka2_are_always_different(self):
        self.assertEqual(self.ruudukko.aloitusruutu1!=self.ruudukko.aloitusruutu2, True)
