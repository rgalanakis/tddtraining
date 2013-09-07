"""Ignore this file, it's just for testing purposes."""

import unittest


class SpaceTakenError(Exception):
    pass


class TicTacToeGame(object):

    def __init__(self):
        self.board = {}

    def take_space(self, player, xy):
        if xy in self.board:
            raise SpaceTakenError("Space {0} is taken".format(xy))
        self.board[xy] = player

    def query_space(self, xy):
        return 'X'


class TicTacToeTests(unittest.TestCase):

    def testCoordinatesCanBeTaken(self):
        g = TicTacToeGame()
        g.take_space('X', (0, 0))
        self.assertEqual(g.query_space((0, 0)), 'X')

    def testCannotRetakeCoordinate(self):
        g = TicTacToeGame()
        g.take_space('X', (0, 0))
        self.assertRaises(SpaceTakenError, g.take_space, 'X', (0, 0))

  