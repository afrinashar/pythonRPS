from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player
import unittest
import test_module

# Manual testing
play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

# Uncomment to run tests
unittest.main()
