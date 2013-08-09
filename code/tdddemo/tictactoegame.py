import itertools

INCOMPLETE = 'unfin'
WINX = 'winx'
WINO = 'wino'
DRAW = 'draw'

X = 'x'
O = 'o'
E = ''

TOPLEFT = 0, 0
LEFTEDGE = 1, 0
BOTTOMLEFT = 2, 0
TOPEDGE = 0, 1
CENTER = 1, 1
BOTTOMEDGE = 2, 1
TOPRIGHT = 0, 2
RIGHTEDGE = 1, 2
BOTTOMRIGHT = 2, 2

WINNING_MOVES = [
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

    def _possiblewins(self):
        for a, b, c in WINNING_MOVES:
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

        self._checkrange(row)
        self._checkrange(col)
        if char != self._turnis:
            raise MoveOutOfOrder()
        if self._board[row][col] != E:
            raise CellTaken()
        self._board[row][col] = char
        self._turnis = O if char is X else X

    def takex(self, spot):
        self._take(X, spot[0], spot[1])

    def takeo(self, spot):
        self._take(O, spot[0], spot[1])

    def takenby(self, spot):
        return self._board[spot[0]][spot[1]]

    def is_empty(self, spot):
        return self.takenby(spot) == E
