tddtraining
===

Resources for a TDD training course. 
Initially created for a TDD in Python training for CCP developers
at CCP Reykjavik, Iceland.
Feel free to adapt and use for your own training,
but please give me feedback if you find it useful.

Code Directories and Exercises
===

The `code` directory contains several subdirectories that are meant
to be used in very particular ways.
This is because code may need to be developed inside one folder
but then copied to another folder.

Note that all code folders contain an `__init__.py`
file to support cross-package imports.
Use these carefully, please- they should only be used in the private
instructor code.
Preferably we'd use symlinks instead of copying things around
but they have some issues on Windows.

Let's go through each exercise and its corresponding directory.

instructor_sources
---

Contains all authoritative source code that may go into exercise folders,
along with supporting resources.

- `mocking_resources`

  Contains the "guerilla" features to use during the mocking exercise,
  an example mocking exercise implementation developed by instructors,
  and any other supporting stuff.
  Should not be given to students.

- `tddai_resources`

  Contains an example TicTacToe AI implementation developed by instructors.
  Not to be given to students.

- `tddai_source`

  Contains the source code for the TDD exercise.
  `tictactoegame.py` and `run.py` should be copied to `exercise_tdd`
  to give students a working TicTacToe game
  and a way to use it interactively.

exercise_mocking
---

Starter code for the mocking exercise.
Give to students.
Instructions are included in `feature_requirements.rst`.

exercise_tdd
---

Starter code for TDD exercise.
Give to students.
Instructions included in `ai_requirements.rst`.
`run.py` and `tictactoegame.py` should be copied from
`instructor_sources/tddai_source` directory.


Presenting
===

Being redone to use reveal.js. Will update when I have it working.

All code compatible with Python 2.6+.

Authors
===

* Rob Galanakis: <rob.galanakis@gmail.com>
* Alex Couper: <info@alexcouper.com>
