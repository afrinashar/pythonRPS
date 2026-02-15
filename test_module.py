import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class UnitTests(unittest.TestCase):

    def test_quincy(self):
        win_rate = play(player, quincy, 1000)
        self.assertTrue(win_rate >= 60)

    def test_abbey(self):
        win_rate = play(player, abbey, 1000)
        self.assertTrue(win_rate >= 60)

    def test_kris(self):
        win_rate = play(player, kris, 1000)
        self.assertTrue(win_rate >= 60)

    def test_mrugesh(self):
        win_rate = play(player, mrugesh, 1000)
        self.assertTrue(win_rate >= 60)
