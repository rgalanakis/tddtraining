import mock
import sys
import unittest

from .. import mocking


class SpecTests(unittest.TestCase):

    def testUsingSpec(self):
        nospec = mock.Mock()
        nospec.wriite('hi')

        spec = mock.create_autospec(sys.stdout)
        self.assertRaises(AttributeError, getattr, spec, 'wriite')


def patchstdout():
    return mock.patch('sys.stdout', spec=sys.stdout)


class PrintStringTests(unittest.TestCase):

    def testPatchContextManager(self):
        """Use mock.patch as a context manager on mocking.print_string."""
        with patchstdout() as m:
            mocking.print_string('hi')
            m.write.assert_called_once_with('hi\n')

    @patchstdout()
    def testPatchDecorator(self, stdout):
        """Same as above, but use patch as a decorator."""
        mocking.print_string('hi')
        stdout.write.assert_called_once_with('hi\n')

    @patchstdout()
    def testMockCallArgsList(self, stdout):
        """Tests that passing a list of strings will print each of them
        individually."""
        mocking.print_string(['hello', 'world'])
        self.assertEqual(
            stdout.write.call_args_list,
            [mock.call('hello\n'), mock.call('world\n')]
        )

    @patchstdout()
    def testUnicodeErrorReturnsFalse(self, stdout):
        stdout.write.side_effect = UnicodeError()
        result = mocking.print_string('')
        self.assertFalse(result)

    def testDoesNotWriteIfIsATtyFalse(self):
        with patchstdout() as m:
            m.isatty.return_value = False
            self.assertFalse(mocking.print_string(''))
        self.assertFalse(m.write.called)


class LogFileTests(unittest.TestCase):

    def testMockOpen(self):
        mopen = mock.mock_open(read_data='{"hi": 2}')
        with mock.patch('__builtin__.open', mopen):
            got = mocking.load_settings()
            self.assertTrue(mopen().__exit__.called)
        self.assertEqual(got, {'hi': 2})
