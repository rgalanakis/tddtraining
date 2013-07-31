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

!

Running tests
===

* Run tests with `unittest.main()`,
  or test discovery through nose.
* Best handled through your IDE!
  * *Demo with PyCharm*
  * *Demo with Sublime*

!

Now, you’re turn!
===

Let's make sure everyone can write and run very simple unit tests.

Next, we'll demo TDD, so we need to make sure everyone can follow along.

