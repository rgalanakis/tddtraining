import unittest

from .. import tictactoegame as ttt


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.g = ttt.Game()

    def testNewGameIsIncomplete(self):
        self.assertEqual(self.g.result(), ttt.INCOMPLETE)

    def testXMustMoveFirst(self):
        self.assertRaises(ttt.MoveOutOfOrder, self.g.takeo, ttt.CENTER)

    def testMovesMustRotate(self):
        self.g.takex(ttt.TOPLEFT)
        self.g.takeo(ttt.TOPRIGHT)
        self.g.takex(ttt.LEFTEDGE)
        self.g.takeo(ttt.RIGHTEDGE)
        self.assertRaises(ttt.MoveOutOfOrder, self.g.takeo, ttt.CENTER)

    def testOutOfBoundsMoveRaises(self):
        self.assertRaises(ttt.OutOfBoundsMove, self.g.takex, (-1, 0))
        self.assertRaises(ttt.OutOfBoundsMove, self.g.takex, (3, 0))
        self.assertRaises(ttt.OutOfBoundsMove, self.g.takex, (0, -1))
        self.assertRaises(ttt.OutOfBoundsMove, self.g.takex, (0, 3))

    def _winx(self):
        self.g.takex(ttt.TOPLEFT)
        self.g.takeo(ttt.TOPEDGE)
        self.g.takex(ttt.LEFTEDGE)
        self.g.takeo(ttt.TOPRIGHT)
        self.g.takex(ttt.BOTTOMLEFT)

    def testXCanWinGame(self):
        self._winx()
        self.assertEqual(self.g.result(), ttt.WINX)

    def testOCanWinGame(self):
        self.g.takex(ttt.TOPLEFT)
        self.g.takeo(ttt.TOPEDGE)
        self.g.takex(ttt.LEFTEDGE)
        self.g.takeo(ttt.CENTER)
        self.g.takex(ttt.BOTTOMRIGHT)
        self.g.takeo(ttt.BOTTOMEDGE)
        self.assertEqual(self.g.result(), ttt.WINO)

    def _draw(self):
        # XXO
        # OOX
        # XOX
        self.g.takex(ttt.TOPLEFT)
        self.g.takeo(ttt.TOPRIGHT)
        self.g.takex(ttt.TOPEDGE)
        self.g.takeo(ttt.LEFTEDGE)
        self.g.takex(ttt.RIGHTEDGE)
        self.g.takeo(ttt.CENTER)
        self.g.takex(ttt.BOTTOMLEFT)
        self.g.takeo(ttt.BOTTOMEDGE)
        self.g.takex(ttt.BOTTOMRIGHT)

    def testDraw(self):
        self._draw()
        self.assertEqual(self.g.result(), ttt.DRAW)

    def testCannotTakeTakenSquare(self):
        self.g.takex(ttt.CENTER)
        self.assertRaises(ttt.CellTaken, self.g.takeo, ttt.CENTER)

    def testNoMovesAllowedAfterWin(self):
        self._winx()
        self.assertRaises(ttt.GameFinished, self.g.takeo, ttt.CENTER)

    def testNoMovesAllowedAfterDraw(self):
        self._draw()
        self.assertRaises(ttt.GameFinished, self.g.takeo, ttt.CENTER)

    def testTakenByReportsCorrectResult(self):
        self.g.takex(ttt.CENTER)
        self.assertEqual(self.g.takenby(ttt.CENTER), ttt.X)
        self.g.takeo(ttt.TOPEDGE)
        self.assertEqual(self.g.takenby(ttt.TOPEDGE), ttt.O)

    def testIsEmpty(self):
        self.g.takex(ttt.CENTER)
        self.assertFalse(self.g.is_empty(ttt.CENTER))
        self.assertTrue(self.g.is_empty(ttt.TOPLEFT))

    def testOutOfBoundsIsEmptyRaises(self):
        self.assertRaises(ttt.OutOfBoundsMove, self.g.is_empty, (-1, 0))

    def testStringRenderEmpty(self):
        self.assertEqual(str(self.g),
            ("   |   |   \n"
             "-----------\n"
             "   |   |   \n"
             "-----------\n"
             "   |   |   "))

    def testStringRenderDraw(self):
        self._draw()
        self.assertEqual(str(self.g),
            (" X | X | O \n"
             "-----------\n"
             " O | O | X \n"
             "-----------\n"
             " X | O | X "))
