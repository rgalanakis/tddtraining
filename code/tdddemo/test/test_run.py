import unittest
from mock import patch

from .. import run
from .. import tictactoegame as ttt


class TestRunner(unittest.TestCase):

    def setUp(self):
        self.game = ttt.Game()
        self.runner = run.Runner(self.game)

    def test_validate_input(self):
        self.assertEqual(self.runner.validate_input("0 0"), [0, 0])
        self.assertEqual(self.runner.validate_input("2 2"), [2, 2])

    def test_validate_input_raises_on_invalid_input(self):
        self.assertRaises(run.InputError, self.runner.validate_input, "01")
        self.assertRaises(run.InputError, self.runner.validate_input, 12)
        self.assertRaises(run.InputError, self.runner.validate_input, "a b")

    def test_validate_input_raises_on_cell_taken(self):
        self.runner.game.takex(ttt.TOPLEFT)
        self.assertRaises(ttt.CellTaken, self.runner.validate_input, "0 0")

    @patch(run.__name__ + ".os.system")
    @patch(run.__name__ + ".show")
    def test_render_game(self, show, _):
        self.runner.render_game()
        show.assert_any_call(self.game)

    @patch(run.__name__ + ".os.system")
    @patch(run.__name__ + ".show")
    def test_render_game_with_errors(self, show, _):
        self.runner.render_game('some error!')
        show.assert_any_call(self.game)
        show.assert_any_call('some error!')

    @patch(run.__name__ + ".raw_input", create=True)
    def test_take_a_turn(self, raw_input_builtin):
        raw_input_builtin.return_value = "0 0"
        self.runner.take_a_turn()
        self.assertEqual(str(self.game),
                         (" X |   |   \n"
                          "-----------\n"
                          "   |   |   \n"
                          "-----------\n"
                          "   |   |   "
                          ))
        raw_input_builtin.return_value = "2 2"
        self.runner.take_a_turn()
        self.assertEqual(str(self.game),
                         (" X |   |   \n"
                          "-----------\n"
                          "   |   |   \n"
                          "-----------\n"
                          "   |   | O "
                          ))

    @patch(run.__name__ + ".raw_input", create=True)
    def test_take_a_turn_pos_taken(self, raw_input_builtin):
        raw_input_builtin.return_value = "0 0"
        self.assertEqual(self.runner.take_a_turn(), None)
        self.assertEqual(self.runner.take_a_turn(),
                         "That position is taken, try again.")

    @patch(run.__name__ + ".raw_input", create=True)
    def test_take_a_turn_invalid(self, raw_input_builtin):
        raw_input_builtin.return_value = "fred"
        self.assertEqual(self.runner.take_a_turn(),
                         ("You need to input in the zero-based "
                          "coordinate form: <x> <y>"))

    @patch(run.__name__ + ".raw_input", create=True)
    def test_take_a_turn_off_the_grid(self, raw_input_builtin):
        raw_input_builtin.return_value = "4 4"
        self.assertEqual(self.runner.take_a_turn(),
                         ("The position you chose (4 4) "
                          "is off the grid."))
