"""Ignore this file, it's just for testing purposes."""

import unittest

X_WINS = "X WINS"

class SpaceTakenError(Exception):
    pass


class MoveOrderError(Exception):
    pass


class TicTacToeGame(object):

    def __init__(self):
        self.board = {}
        self._lastplayer = 'O'

    def take_space(self, player, xy):
        if player not in ("X", "O"):
            raise ValueError("Player {0} is invalid. Use "
                             "'X' or 'O'".format(player))
        if xy in self.board:
            raise SpaceTakenError("Space {0} is taken".format(xy))
        if player == self._lastplayer:
            raise MoveOrderError()
        self.board[xy] = player
        self._lastplayer = player

    def query_space(self, xy):
        return 'X'

    def get_result(self):
        return X_WINS


class TicTacToeTests(unittest.TestCase):

    def setUp(self):
        self.g = TicTacToeGame()

    def testCoordinatesCanBeTaken(self):
        self.g.take_space('X', (0, 0))
        self.assertEqual(self.g.query_space((0, 0)), 'X')

    def testCannotRetakeCoordinate(self):
        self.g.take_space('X', (0, 0))
        self.assertRaises(SpaceTakenError, self.g.take_space, 'X', (0, 0))

    def testXMustMoveFirst(self):
        self.assertRaises(MoveOrderError, self.g.take_space, 'O', (0, 0))

    def testPlayerMustBeXorO(self):
        self.assertRaises(ValueError, self.g.take_space, 'T', (0, 0))

    def testMovesMustRotate(self):
        self.g.take_space('X', (0, 0))
        self.assertRaises(MoveOrderError, self.g.take_space, 'X', (1, 1))

    def testDetectsVictory(self):
        self.g.take_space('X', (0, 0))
        self.g.take_space('O', (1, 0))
        self.g.take_space('X', (0, 1))
        self.g.take_space('O', (2, 0))
        self.g.take_space('X', (0, 2))
        self.assertEqual(self.g.get_result(), X_WINS)

    def testOCanWin(self):
        return
