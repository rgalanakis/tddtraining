from . import tictactoegame as ttt

# --X
# -O-
# X--

class NoMoveAvailable(Exception):
    pass


class AI(object):

    def __init__(self, player):
        self.player = player
        if player is ttt.X:
            self.opp = ttt.O
        else:
            self.opp = ttt.X

    def _moves_and_values(self, game):
        for a, b, c in ttt.WINNING_MOVES:
            values = game.takenby(a), game.takenby(b), game.takenby(c)
            yield (a, b, c), values

    def _move_to_complete_row(self, game, char):
        for rowmoves, rowvalue in self._moves_and_values(game):
            if rowvalue.count(char) == 2:
                try:
                    emptyind = rowvalue.index(ttt.E)
                except ValueError:
                    pass
                else:
                    return rowmoves[emptyind]

    def choose_move(self, game):
        # Try to win
        winner = self._move_to_complete_row(game, self.player)
        if winner is not None:
            return winner
        # Try to block
        blocker = self._move_to_complete_row(game, self.opp)
        if blocker is not None:
            return blocker

        # Take center
        if game.is_empty(ttt.CENTER):
            return ttt.CENTER

        # Take corner
        for corner in ttt.TOPLEFT, ttt.TOPRIGHT, ttt.BOTTOMLEFT, ttt.BOTTOMRIGHT:
            if game.is_empty(corner):
                return corner

        # Take edge
        for edge in ttt.TOPEDGE, ttt.RIGHTEDGE, ttt.BOTTOMEDGE, ttt.LEFTEDGE:
            if game.is_empty(edge):
                return edge

        raise NoMoveAvailable()
