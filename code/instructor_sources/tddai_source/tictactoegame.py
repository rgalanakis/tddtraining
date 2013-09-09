"""Working implementation of tictactoe to build an AI against."""

import itertools

INCOMPLETE = 'unfin'
WINX = 'winx'
WINO = 'wino'
DRAW = 'draw'

X = 'X'
O = 'O'
E = ' '

TOPLEFT = 0, 0
LEFTEDGE = 1, 0
BOTTOMLEFT = 2, 0
TOPEDGE = 0, 1
CENTER = 1, 1
BOTTOMEDGE = 2, 1
TOPRIGHT = 0, 2
RIGHTEDGE = 1, 2
BOTTOMRIGHT = 2, 2

THREE_IN_A_ROWS = [
    # row
    [TOPLEFT, TOPEDGE, TOPRIGHT],
    [LEFTEDGE, CENTER, RIGHTEDGE],
    [BOTTOMLEFT, BOTTOMEDGE, BOTTOMRIGHT],
    # columns
    [TOPLEFT, LEFTEDGE, BOTTOMLEFT],
    [TOPEDGE, CENTER, BOTTOMEDGE],
    [TOPRIGHT, RIGHTEDGE, BOTTOMRIGHT],
    # diags
    [TOPLEFT, CENTER, BOTTOMRIGHT],
    [TOPRIGHT, CENTER, BOTTOMLEFT]
]

class MoveOutOfOrder(Exception):
    pass


class OutOfBoundsMove(Exception):
    pass


class CellTaken(Exception):
    pass


class GameFinished(Exception):
    pass


class Game(object):

    def __init__(self, board=None):
        self._turnis = X
        if board is None:
            board = [
                [E, E, E],
                [E, E, E],
                [E, E, E]
            ]
        self._board = board

    @property
    def turnis(self):
        return self._turnis

    def _possiblewins(self):
        for a, b, c in THREE_IN_A_ROWS:
            yield [self.takenby(a), self.takenby(b), self.takenby(c)]

    def result(self):
        xwin = [X, X, X]
        owin = [O, O, O]
        for w in self._possiblewins():
            if w == xwin:
                return WINX
            if w == owin:
                return WINO
        if E not in list(itertools.chain(*self._board)):
            return DRAW
        return INCOMPLETE

    def _checkrange(self, val):
        if val < 0 or val > 2:
            raise OutOfBoundsMove()

    def _take(self, char, row, col):
        if self.result() != INCOMPLETE:
            raise GameFinished()

        if not self.is_empty((row, col)):
            raise CellTaken()
        if char != self._turnis:
            raise MoveOutOfOrder()
        self._board[row][col] = char
        self._turnis = O if char is X else X

    def takex(self, spot):
        self._take(X, spot[0], spot[1])

    def takeo(self, spot):
        self._take(O, spot[0], spot[1])

    def takenby(self, spot):
        return self._board[spot[0]][spot[1]]

    def is_empty(self, spot):
        self._checkrange(spot[0])
        self._checkrange(spot[1])
        return self.takenby(spot) == E

    def __str__(self):
        string = ""
        for index, row in enumerate(self._board):
            string += " {0} | {1} | {2} ".format(*row)
            if index in (0, 1):
                string += "\n-----------\n"
        return string
