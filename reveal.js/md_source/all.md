# Test Driven Development in a Day

Presented by Alex Couper and Rob Galanakis

>

# Why TDD?

V

## TDD is a **design**  process.
## not a **testing** process.

V

## Regression tests are a **side product**.
## not the goal.

V

> TDD doesn't drive good design.
> TDD gives you immediate feedback about what is likely to be bad design.

Note: Kent Beck

>

# Why today?

Today's goal is to teach you the **skill** of TDD by
explanation, demonstration, and **participation**.

V

# Be skeptical

### The best way to justify TDD is by doing it.

>

# Agenda

* Unit Testing introduction
* TDD Explanation and Demo
* You do TDD
* Lunch
* Continue TDD
* Review solutions
* Dependency Injection and Mocking Introduction
* Mocking Exercise
* Review

>

# Pair Programming

V

Note: Explain what pair programming is and why it is valuable.

V

Note: Show this via images

* **Driver** writes code.
* **Navigator** guides and reviews.
* Switch frequently.

V

Everything today should be done in pairs.

>

# What is a Unit Test?

Note: Let's talk about what unit testing is at a technical level,
so we're all up to speed with the same vocabulary.

V

## A "unit" is smallest portion of code, such as a method or function.

V

## A "test" asserts a condition, such as:

### `1 + 1 == 2`

V

`import unittest`

Note: Python's `unittest` module is based on the **xUnit** framework

V

## Test cases and tests

    class CalculatorTests(unittest.TestCase):
        def testOnePlusOne(self):  # Is a test
            ...
        def someHelper(self):  # Is not a test
            ...

Note: Subclass `unittest.TestCase`. All `test*` methods are tests:

V

### Tests can succeed:

  `self.assertEqual(2, 1 + 1)`

### Tests can fail:

  `assertEqual(3, 1 + 1)`

### Tests can error:

  `assertEqual(2, 1 + '')`

V

## Assertions

    self.assertTrue(1 + 1 == 3)
    # AssertionError: False is not True

    self.assertEqual(1 + 1, 3)
    # AssertionError: 2 != 3

V

## Setting up and tearing down

![setUp->runTest->tearDown](/images/setupteardown.png)

V

## Package setup for testing

    eggs/
        __init__.py
        spam.py
        test/
            __init__.py
            test_eggs.py
            test_spam.py

Note: Have a test folder with an `__init__.py` file so it's importable.
Test files should be `test_<modulename>.py`

V

## Running tests

    if __name__ == '__main__':
        unittest.main()

    $ python -c "import nose; nose.run()"

    But best handled through your IDE.

Note: Demo with commandline, PyCharm, and Sublime with Kristinn's plugin.

>

# Now, your turn!

Note: Next we'll introduce the interesting concepts of Test Driven Development,
so we need to make sure everyone can follow along.

Let's make sure everyone can write and run very simple unit tests.

>

TDD Intro
===

Now that we've covered unit testing,
we'll go into the TDD process.

V

![Design->Implement->Test](/images/design_impl_test.png)

V

Normal development has testing come at the end.

V

![Design->Test->Implement->Test](/images/tdd_linear.png)

V

Test Driven Development has testing come before implementation.

V

![Design->Test->Implement->Test Cycle](/images/tdd_cycle.png)

V

Actually, it is a short cycle that happens many times
as you "implement" something.

V

![Design->Test->Implement->Test Cycle](/images/tdd_cycle_rgr.png)

V

Red->Green->Refactor->(Repeat) is the **fundamental** concept of TDD.

V

* Write a test.
* Run the test and ensure it fails.
* Do the **simplest** implementation to get the test to pass.
* Run the test and ensure it passes.
* **Refactor** to clean up tests or code.

>

Refactoring
===

V

> A disciplined technique for restructuring an existing body of code,
> altering its internal structure without changing its external behavior.

V

Too easy?
===

It requires a huge amount of discipline to do this.

But the more it's done, the easier it is, because of your skills *and*
an improved codebase.

We'll go into each step in detail during the demo.

>

Demo time
===

We're going to build a Tic-Tac-Toe game using TDD.

This is an exercise in **Mob Programming**,
so please participate!

>

Step 0 (Prep)
===

Figure out what you are making!

>

Step 1 (Prep)
===

Create file structure.

>

Step 2
===

Figure out the first behavior we want to test.

The first test is the hardest to write!

>

Step 3
===

Create the test.

>

Step 4
===

Run the test. It must fail.

>

Step 5
===

Write the code.

The first implementation is the easiest to write!

>

Step 6
===

Run the tests.

>

Step 7
===

Refactor yet? No.

>

TODO: Red

>

TODO: Green

>

TODO: Refactor

>

The End
===

Know when you're done. Your code should do only what it needs to do.

>

Your turn!
===

Take the Tic-Tac-Toe game provided and write a "perfect" AI using TDD.

See `tictactoe/ai_requirements.rst` for your AI's logic.

You can use any AI strategy you want but it must be developed with TDD.

>

Let's review a couple solutions.

>

OLD
===

We'll go through some terminology and uses for mocking to get everyone on the same page.

1. A mock is a stand-in for a piece of code with external dependencies.
2. External dependencies should be factored out so they are passed into code that needs them (dependency injection)
3. Or external dependencies can be patched (monkeypatching). Prefer dependency injection, use whatever makes the code and tests simpler.
4. Wrap hard dependencies (DB, RESTful API) in a Pythonic wrapper. "Business" code shouldn't access resources directly.
5. Use a stub to return a known value (very simple).
6. Use a fake as a lightweight API implementation (simple when done well, reusable).
7. Use a mock to ensure something is called in a certain way (most confusing).
