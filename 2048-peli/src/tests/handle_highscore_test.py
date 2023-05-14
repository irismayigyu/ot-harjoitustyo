import unittest
from handle_highscore import HandleHighscore


class TestColours(unittest.TestCase):
    def setUp(self):
        self.hscore = HandleHighscore()

    def test_if_updating_works(self):
        self.hscore.init_high = 0
        self.hscore.update(64)
        self.assertEqual(self.hscore.update(64) == 64, True)
        self.hscore.init_high = 0
