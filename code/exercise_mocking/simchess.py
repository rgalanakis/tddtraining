"""A Chess implementation to use during the mocking exercise.

Students should not modify this file.
"""

import exceptions
import inspect
import random
import time

__all__ = ['WINWHITE', 'WINBLACK', 'DRAW', 'ABORTED', 'simulate_game']

WINWHITE = 'winw'
WINBLACK = 'winb'
DRAW = 'draw'
ABORTED = 'aborted'


_ALL_EXC = [e for e in inspect.getmembers(exceptions)
            if inspect.isclass(e) and issubclass(e, Exception)]


def simulate_game():
    """Simulates a game and returns a result
    (one of the consts on this module)."""
    # occassionally, we want to raise some sort of exception,
    # because that's how code is :)
    time.sleep(0.01)
    if random.randint(0, 50) == 30:
        raise random.choice(_ALL_EXC)()
    return random.choice([WINWHITE, WINBLACK, DRAW, ABORTED])
