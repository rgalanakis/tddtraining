import unittest
import mock
import random


JUDGEMENTS = ['a', 'b', 'c']

def get_judgement():
    return random.choice(JUDGEMENTS)


class TestGetJudgement(unittest.TestCase):

    def testReturnsValidOutcome(self):
        j = get_judgement()
        self.assertIn(j, JUDGEMENTS)


ASK_NAME = 'What is your name?'
ASK_QUESTION = 'Hello, %s, what is your question?'

def play_game(getjudgement=get_judgement):
    name = raw_input(ASK_NAME)
    raw_input(ASK_QUESTION % name)
    sys.stdout.write('Your answer is: %s\n' % getjudgement())

import sys

@mock.patch('__builtin__.raw_input', mock.Mock())
@mock.patch('sys.stdout', mock.Mock())
class TestPlay(unittest.TestCase):

    def testAsksName(self):
        play_game()
        raw_input.assert_any_call(ASK_NAME)

    def testAsksQuestionWithName(self):
        raw_input.return_value = 'Putin'
        play_game()
        raw_input.assert_any_call(ASK_QUESTION % 'Putin')

    def testPrintsResult(self):
        play_game(lambda: 'Yes.')
        sys.stdout.write.assert_any_call('Your answer is: Yes.\n')
