from ..tddai_source import tictactoegame as ttt

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
        for a, b, c in ttt.THREE_IN_A_ROWS:
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

        # Make a fork
        fork = find_fork(self.player, game)
        if fork[0] is not None:
            return fork[0]

        # Block a fork
        fork = find_fork(self.opp, game)
        if fork[0] is not None:
            for adj, opp in fork[1]:
                if game.is_empty(adj):
                    return adj

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


_corners = {
    ttt.TOPLEFT: [
        (ttt.TOPEDGE, ttt.TOPRIGHT),
        (ttt.CENTER, ttt.BOTTOMRIGHT),
        (ttt.LEFTEDGE, ttt.BOTTOMLEFT)
    ],
    ttt.TOPRIGHT: [
        (ttt.TOPEDGE, ttt.TOPLEFT),
        (ttt.CENTER, ttt.BOTTOMLEFT),
        (ttt.RIGHTEDGE, ttt.BOTTOMRIGHT)
    ],
    ttt.BOTTOMRIGHT: [
        (ttt.RIGHTEDGE, ttt.TOPRIGHT),
        (ttt.CENTER, ttt.TOPLEFT),
        (ttt.BOTTOMEDGE, ttt.BOTTOMLEFT)
    ],
    ttt.BOTTOMLEFT: [
        (ttt.BOTTOMEDGE, ttt.BOTTOMRIGHT),
        (ttt.CENTER, ttt.TOPRIGHT),
        (ttt.LEFTEDGE, ttt.TOPLEFT)
    ],

}

def find_fork(player, game):
    for xy, connections in _corners.items():
        if game.takenby(xy) != ttt.E:
            continue
        forks = []
        for adjacent, opposite in connections:
            adjplayer = game.takenby(adjacent)
            oppplayer = game.takenby(opposite)
            if adjplayer != ttt.E:
                continue
            if oppplayer != player:
                continue
            forks.append([adjacent, opposite])
        if len(forks) > 1:
            return xy, forks
    return None, []
