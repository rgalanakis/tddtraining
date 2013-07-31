Overview
===

What do we want participants to walk away with?

  * Understand how to do TDD
  * Understand why TDD results in testable code and why testable code is good
  * Have a technical understanding of how Python unit testing works
  * Understand mocking and how to mock

Part I: How unittest works and IDE setup
===

We’ll start with a straightforward explanation of how testing works technically,
and making sure everyone is setup to do TDD.

1. A “unit” is smallest portion of code, such as a method or function
2. A “test” asserts a condition, such as 1 + 1 == 2.
3. Python’s unittest module
    1. Based on xUnit framework, which specifies a certain architecture we don’t need to cover right now.
    2. Subclass unittest.TestCase. All ‘test*’ methods are tests.
    3. Tests can succeed (assertEqual(2, 1 + 1))
    4. Tests can fail (assertEqual(3, 1 + 1))
    5. Tests can error (assertEqual(2, 1 + ‘’))
    6. There are many specific assert methods. Use the most specific one possible (ie, assertIn(a, [1, 2]) rather than assertTrue(a in [1, 2]))
    7. A ‘setUp’ method can be run before each test.
    8. A ‘tearDown’ method can be run after each test.
    9. There’s setUpClass, tearDownClass, and addCleanup, if you’re interested.
1. Package setup for testing
    1. Have a test folder with an __init__.py file so it’s importable.
    2. Test files should be ‘test_<modulename>.py’
1. Run tests with unittest.main(), or test discovery through nose. Best handled through your IDE!
    1. Demo with PyCharm
    2. Demo with Sublime
1. Now, you’re turn!
    1. Make sure everyone can write and run very simple unit tests.

Part II: TDD Demo
===

Instructors will do a TDD demo to create a TicTacToe game.
The resulting game will be used for the rest of the exercises.
The demo may result in an incomplete game,
a full implementation made in advance will be provided.
Red-Green-Refactor, the TDD process,
and TDD benefits (as a design mechanism, as a regression testing mechanism)
will be explained and demonstrated.

Part III: Head-first into TDD
===

Students will create a perfect AI for the TicTacToe game.

1. AI requirements (adapted from Wikipedia). AI should choose the first possible item:
    1. Win: If AI has two in a row, place a third to win.
    2. Block. If opponent has two in a row, play the block.
    3. Fork: Create two non-blocked lines of 2.
    4. Block a fork:
        1. Create two in a row to force opponent into defending as long as defense does not create a fork.
        2. If the opponent can fork, block the fork.
    1. Play the center.
    2. If the opponent is in a corner, play the opposite corner.
    3. Play an empty corner.
    4. Play an empty side.
    5. Remember:
        1. TicTacToe between perfect players (like our AI) always results in a tie.
        2. An O playing an imperfect strategy should always lose against an X with a perfect strategy.
1. Implement. Instructors will walk around and guide students.
2. Analyze solutions together. Look at use of state, exceptions, etc.

Part IV: Mocking and Dependency Injection
===

We’ll go through some terminology and uses for mocking to get everyone on the same page.

1. A mock is a stand-in for a piece of code with external dependencies.
2. External dependencies should be factored out so they are passed into code that needs them (dependency injection)
3. Or external dependencies can be patched (monkeypatching). Prefer dependency injection, use whatever makes the code and tests simpler.
4. Wrap hard dependencies (DB, RESTful API) in a Pythonic wrapper. “Business” code shouldn’t access resources directly.
5. Use a stub to return a known value (very simple).
6. Use a fake as a lightweight API implementation (simple when done well, reusable).
7. Use a mock to ensure something is called in a certain way (most confusing).

Part V: Practical TDD
===

Applying TDD for a new project, with clear requirements, is straightforward.
In this part, we’ll use TDD on a less academic example.
Students will need to make a tic-tac-toe game that reports completed games
to a database.
Instructors will walk through what’s expected in the implementation.

1. Requirements
    1. When a game starts, the gmtime is recorded in the DB
    2. After each game, the gmtime and result (player A win, player B win, tie, abort) should be reported to the database.
    3. Results are persisted.
1. Instructions/suggestions
    1. Wrap the original tictactoe library into a version that does the necessary calls (do not modify the original library to add DB support)
    2. Provide a domain-specific interface for the DB calls (record_game_started, record_game_result) that has the DB dependency injected.
    3. Inject this interface into the game wrapper, and test with a mock (ensure that things are called in a proper order with proper args)
    4. You may also want to inject the tictactoe game itself as a stub
    5. Test db interface separately with in-memory sqlite DB, not as part of game.
    6. Provide psuedo-code or diagrammatic implementation for students to base off of.
1. Implementation. Instructors walk around and help students.
