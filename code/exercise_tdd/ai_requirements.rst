Overview
========

Implement a perfect Tic-Tac-Toe AI.
You must use TDD to develop it,
but you can choose whatever AI approach you wish
(rule-based, brute force).
A perfect AI should never lose,
and should win against an imperfect player.

Rule-Based AI
-------------

If you choose a rule-based AI (which is recommended),
here is some information.

These Tic Tac Toe AI Requirements are adapted from Wikipedia.
See http://en.wikipedia.org/wiki/Tic-tac-toe#Strategy if you need
more information (it has the most concise and complete strategy rules
I've found).

AI should choose the first possible item/subitem in the list.

    # Win: If AI has two in a row, place a third to win.
    # Block. If opponent has two in a row, play the block.
    # Fork: Create two non-blocked lines of 2.
      # An example would be if you have the top left and bottom right corners,
        a fork would be created by taking the bottom left if the
        left edge and bottom edge are free.
    # Block a fork:
      # Create two in a row to force opponent into defending
        as long as defense does not create a fork.
      # If the opponent can fork, block the fork.
    # Play the center.
    # If the opponent is in a corner, play the opposite corner.
    # Play an empty corner.
    # Play an empty side.

Suggestions
===========

- Focus on the algorithm, not having the AI 'play' the game.
- If you need help coming up with boards to exercise the rules,
  talk to the instructor.
  Some of them, such as creating or block forks, can be tricky.
