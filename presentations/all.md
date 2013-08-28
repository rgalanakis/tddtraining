Test Driven Development in a Day
===

Presented by Alex Couper and Rob Galanakis

!

Agenda
===

* Introductions
* Pairing
* Unit Testing introduction
* TDD Explanation and Demo
* You do TDD
* Lunch
* Continue TDD
* Review solutions
* Dependency Injection and Mocking Introduction
* Mocking Exercise
* Review

!

Introductions
===

!

Why TDD
===

* TDD is a **design** process, not a **testing** process.
* Regression tests are a **side product** of the process, not the goal.
* Using TDD results in fundamentally better code than not using it.
* You will feel the same way by the end of the day.

!

Why today?
===

Today's goal is to teach you the **skill** of TDD by
explanation, demonstration, and **participation**.

**Be skeptical**: the best way to justify TDD is by doing it.
If you're still not convinced, talk to me.

!

Legacy Code
===

* Today is focused on new code,
  but it is vital for legacy code as well.
* More on this when Michael Feathers visits CCP in late October.

!

Pair Programming
===

...is a tenet of eXtreme Programming and valuable when learning TDD.

* All exercises will be done in pairs.
* You should not pair with the same person twice.
* Leads to huge gains on production work!

!

Pair Programming
===

* **Driver** writes code.
* **Navigator** guides and reviews.
* Switch frequently.

!

Let's get started!
===

!

I. Unit Testing Intro
===

Let's talk about what unit testing is at a technical level,
so we're all up to speed with the same vocabulary.

!

What's a "unit"?
===

A “unit” is smallest portion of code, such as a method or function.

!

What's a "test"?
===

A “test” asserts a condition, such as:

`1 + 1 == 2`

!

`import unittest`
===

Python's `unittest` module is based on the **xUnit** framework,
which specifies a certain architecture we don’t need to cover right now.

!

Test cases and tests
===

* Subclass `unittest.TestCase`.
* All `test*` methods are tests:

        class CalculatorTests(unittest.TestCase):
            def testOnePlusOne(self):  # Is a test
                ...
            def someHelper(self):  # Is not a test
                ...

!

Test results
===

* Tests can succeed:
  * `self.assertEqual(2, 1 + 1)`
* Tests can fail:
  * `assertEqual(3, 1 + 1)`
* Tests can error:
  * `assertEqual(2, 1 + ‘’)`

!

Assertions
===

* There are many specific assert methods.
* Use the most specific one possible to generate better failure messages.

        self.assertIn(a, [1, 2]) # Good!
        self.assertTrue(a in [1, 2]) # Bad!

!

Setting up and tearing down
===

* A `setUp` method can be run before each test.
* A `tearDown` method can be run after each test.
* There’s `setUpClass`, `tearDownClass`, and `addCleanup`, if you’re interested.

!

Package setup for testing
===

* Have a test folder with an `__init__.py` file so it’s importable.
* Test files should be `test_<modulename>.py`

    eggs/
        __init__.py
        spam.py
        test/
            __init__.py
            test_eggs.py
            test_spam.py

!

Running tests
===

* Run tests with `unittest.main()`,
  or test discovery through nose.
* Best handled through your IDE!
  * *Demo with commandline with nose*
  * *Demo with PyCharm*
  * *Demo with Sublime plugin*

!

Now, your turn!
===

Next we'll introduce the interesting concepts of Test Driven Development,
so we need to make sure everyone can follow along.

Let's make sure everyone can write and run very simple unit tests.

!

TDD Intro
===

Now that we've covered unit testing,
we'll go into the TDD process.

!

Normal Dev
===

![Design->Implement->Test](/images/design_impl_test.png)

!

Test Driven Dev
===

![Design->Test->Implement->Test](/images/tdd_linear.png)

!

Test Driven Dev
===

![Design->Test->Implement->Test Cycle](/images/tdd_cycle.png)

!

Red->Green->Refactor->(Repeat) is the **fundamental** concept of TDD.

!

* Write a test.
* Run the test and ensure it fails.
* Do the **simplest** implementation to get the test to pass.
* Run the test and ensure it passes.
* **Refactor** to clean up tests or code.

!

Refactoring
===

*A disciplined technique for restructuring an existing body of code,*
*altering its internal structure without changing its external behavior.*

!

Too easy?
===

It requires a huge amount of discipline to do this.

But the more it's done, the easier it is, because of your skills *and*
an improved codebase.

We'll go into each step in detail during the demo.

!

Demo time
===

We're going to build a Tic-Tac-Toe game using TDD.

This is an exercise in **Mob Programming**,
so please participate!

!

Step 0 (Prep)
===

Figure out what you are making!

!

Step 1 (Prep)
===

Create file structure.

!

Step 2
===

Figure out the first behavior we want to test.

The first test is the hardest to write!

!

Step 3
===

Create the test.

!

Step 4
===

Run the test. It must fail.

!

Step 5
===

Write the code.

The first implementation is the easiest to write!

!

Step 6
===

Run the tests.

!

Step 7
===

Refactor yet? No.

!

TODO: Red

!

TODO: Green

!

TODO: Refactor

!

The End
===

Know when you're done. Your code should do only what it needs to do.

!

Your turn!
===

Take the Tic-Tac-Toe game provided and write a "perfect" AI using TDD.

See `tictactoe/ai_requirements.rst` for your AI's logic.

You can use any AI strategy you want but it must be developed with TDD.

!

Let's review a couple solutions.

!

OLD
===

We’ll go through some terminology and uses for mocking to get everyone on the same page.

1. A mock is a stand-in for a piece of code with external dependencies.
2. External dependencies should be factored out so they are passed into code that needs them (dependency injection)
3. Or external dependencies can be patched (monkeypatching). Prefer dependency injection, use whatever makes the code and tests simpler.
4. Wrap hard dependencies (DB, RESTful API) in a Pythonic wrapper. “Business” code shouldn’t access resources directly.
5. Use a stub to return a known value (very simple).
6. Use a fake as a lightweight API implementation (simple when done well, reusable).
7. Use a mock to ensure something is called in a certain way (most confusing).
