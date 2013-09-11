Overview
========

Applying TDD for a new project, with clear requirements, is straightforward.
For this exercise, we will use TDD on a less academic example.
Take an existing implementation of chess
and make it save game results.

Requirements
============

    # When a game starts, the gmtime is written.
    # After each game, the gmtime and result 
      (white win, black win, draw, abort, error)
      should be written.
    # Results are persisted.

Suggestions
===========

    # Wrap the `simchess` library into a version that does
      the necessary calls
      (ie, do not modify the library to add these calls).
    # Provide a domain-specific interface for the file system calls
      (`record_game_started`, `record_game_result`).
    # This interface should have file system access methods injected
      so it can be mocked.
    # Inject this interface into the game wrapper,
      and test with a mock
      (ensure that things are called in a proper order with proper args).
    # You may also want to inject the game itself as a stub,
      since the implementation may be unreliable.

Resources
=========

See `simchess.py` for the implementation of Chess you should use.
It should behave like you'd expect a 3rd party library to.
Do not modify the code.
