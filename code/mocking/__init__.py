"""
Instructions and code for the mocking exercise.

Trainees should put their code in this directory.

Overview
========

Applying TDD for a new project, with clear requirements, is straightforward.
For this exercise, we will use TDD on a less academic example.
Students will need to take an existing implementation of tic-tac-toe
and make it report completed games to a database.

Requirements
============

    # When a game starts, the gmtime is recorded in the DB
    # After each game, the gmtime and result
      (X win, O win, draw, abort, error, etc.)
      should be reported to the database.
    # Results are persisted.
    # Requirements may change and increase as you work on the exercise!

Suggestions
===========

    # Wrap the original tictactoe library into a version that does
      the necessary calls
      (ie, do not modify the original library to add DB support).
    # Provide a domain-specific interface for the DB calls
      (`record_game_started`, `record_game_result`)
      that has the DB dependency injected.
    # Inject this interface into the game wrapper,
      and test with a mock
      (ensure that things are called in a proper order with proper args).
    # You may also want to inject the tictactoe game itself as a stub.
    # Test db interface separately with in-memory sqlite DB,
      not as part of game.

Resources
=========

See `tictactoegame.py` for an implementation of Tic-Tac-Toe.
It's actually not a real implementation,
but should behave like one.

See `badexample.py` for a bad implementation of this feature.
"""
