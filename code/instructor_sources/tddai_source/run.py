"""Console UI for `tictactoegame.py`.

Run this file to play an actual game with two players.
Feel free to edit it if you want to play against an AI.
"""

import os

import tictactoegame as ttt

g = ttt.Game()

RESULT = {
    ttt.WINX: "X WON!",
    ttt.WINO: "O WON!",
    ttt.DRAW: "You tied!",
}


class InputError(Exception):
    pass


def show(string):
    print string


class Runner(object):

    def __init__(self, game):
        self.game = game

    def validate_input(self, input):
        try:
            chosen = [int(i) for i in input.split(' ')]
            if len(chosen) != 2:
                raise InputError()
        except:
            raise InputError()

        if not self.game.is_empty(chosen):
            raise ttt.CellTaken()

        return chosen

    def render_game(self, error=""):
        os.system('cls' if os.name == 'nt' else 'clear')
        show(self.game)
        if error:
            show(error)

    def take_a_turn(self):
        chosen = raw_input("{0} - Pick a position "
                           "(x y):".format(self.game.turnis))
        try:
            position = self.validate_input(chosen)
        except ttt.CellTaken:
            return "That position is taken, try again."
        except ttt.OutOfBoundsMove:
            return ("The position you chose ({0}) "
                     "is off the grid.".format(chosen))
        except InputError:
            return ("You need to input in the zero-based "
                    "coordinate form: <x> <y>")

        if self.game.turnis == ttt.X:
            self.game.takex(position)
        else:
            self.game.takeo(position)

    def run(self):
        error = False
        while self.game.result() == ttt.INCOMPLETE:
            self.render_game(error)
            error = self.take_a_turn()

        show(RESULT[self.game.result()])


def main():
    r = Runner(g)
    r.run()


if __name__ == '__main__':
    main()
