Overview
========

Applying TDD for a new project, with clear requirements, is straightforward.
For this exercise, we will use TDD on a less academic example.
Take an existing implementation of tic-tac-toe
and make it report completed games to a database.

Requirements
============

    # When a game starts, the gmtime is recorded in the DB
    # After each game, the gmtime and result
      (X win, O win, draw, abort, error, etc.)
      should be stored in the database.
    # Results are persisted.
    # Requirements may change and increase as you work on the exercise!
      Just like the real world!

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

See `simtictactoe.py` for an implementation of Tic-Tac-Toe.
It should behave like you'd expect a 3rd party library to.
Do not modify the code.
