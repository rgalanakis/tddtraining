import unittest

from ...tddai_source import tictactoegame as tttg
from ...tddai_source.tictactoegame import X, O, E
from .. import tictactoeai as tttai


class TestAI(unittest.TestCase):
    """
    1. Win: If AI has two in a row, place a third to win.
    2. Block. If opponent has two in a row, play the block.
    3. Fork: Create two non-blocked lines of 2.
    4. Block a fork:
        1. Create two in a row to force opponent into defending as long as defense does not create a fork.
        2. If the opponent can fork, block the fork.
    1. Play the center.
    2. If the opponent is in a corner, play the opposite corner.
    3. Play an empty corner.
    4. Play an empty side.
    """

    def assertMove(self, player, ideal, board, func='assertEqual'):
        g = tttg.Game(board)
        ai = tttai.AI(player)
        move = ai.choose_move(g)
        getattr(self, func)(move, ideal)

    def testPlacesToWinX(self):
        self.assertMove(tttg.X, tttg.BOTTOMLEFT, [
            [X, E, O],
            [X, E, O],
            [E, E, E]
        ])

    def testPlacesToWinO(self):
        self.assertMove(tttg.O, tttg.BOTTOMRIGHT, [
            [X, E, O],
            [E, X, O],
            [X, E, E]
        ])

    def testPlacesToBlock(self):
        self.assertMove(O, tttg.LEFTEDGE, [
            [X, O, O],
            [E, E, X],
            [X, E, E]
        ])

    def testFork(self):
        self.assertMove(X, tttg.BOTTOMRIGHT, [
            [X, O, E],
            [O, E, E],
            [X, E, E]
        ])

    def testBlockAFork(self):
        edges = [tttg.TOPEDGE, tttg.RIGHTEDGE, tttg.BOTTOMEDGE, tttg.LEFTEDGE]
        self.assertMove(O, edges, [
            [E, E, X],
            [E, O, E],
            [X, E, E]
        ], 'assertIn')

    def testCenterIsPlayedAsFirstMove(self):
        self.assertMove(X, tttg.CENTER, None)
        self.assertMove(O, tttg.CENTER, [
            [X, E, E],
            [E, E, E],
            [E, E, E]
        ])

    def testPlaysEmptyCorner(self):
        self.assertMove(O, tttg.TOPLEFT, [
            [E, E, E],
            [E, X, E],
            [E, E, E]
        ])
        self.assertMove(X, tttg.TOPLEFT, [
            [E, E, E],
            [E, O, E],
            [E, E, X]
        ])

    def testPlaysEmptyEdge(self):
        self.assertMove(O, tttg.LEFTEDGE, [
            [X, O, X],
            [E, O, X],
            [O, X, O]
        ])

    def testRaisesForFullBoard(self):
        with self.assertRaises(tttai.NoMoveAvailable):
            self.assertMove(X, None, [
                [X, O, X],
                [X, O, X],
                [O, X, O]
            ])


class TestAIImpl(unittest.TestCase):

    def testFindsFork(self):
        self.assertEqual(tttg.BOTTOMRIGHT, tttai.find_fork(X, tttg.Game([
            [X, O, E],
            [O, E, E],
            [X, E, E]
        ]))[0])

    def testFindsNoFork(self):
        self.assertEqual(None, tttai.find_fork(X, tttg.Game([
            [X, O, E],
            [E, E, E],
            [E, E, E]
        ]))[0])
        self.assertEqual(None, tttai.find_fork(X, tttg.Game([
            [X, E, E],
            [O, O, E],
            [X, E, E]
        ]))[0])
