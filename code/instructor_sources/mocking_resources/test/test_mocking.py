import mock
import sys
import unittest

from .. import mocking


class PrintStringTests(unittest.TestCase):

    def testPatchContextManager(self):
        """Use mock.patch as a context manager on mocking.print_string."""
        with mock.patch('sys.stdout.write') as m:
            mocking.print_string('hi')
            m.assert_called_once_with('hi\n')

    @mock.patch('sys.stdout.write')
    def testPatchDecorator(self, write):
        """Same as above, but use patch as a decorator."""
        mocking.print_string('hi')
        write.assert_called_once_with('hi\n')

    @mock.patch('sys.stdout.write')
    def testMockCallArgsList(self, write):
        """Tests that passing a list of strings will print each of them
        individually."""
        mocking.print_string(['hello', 'world'])
        self.assertEqual(
            write.call_args_list,
            [mock.call('hello\n'), mock.call('world\n')]
        )

    @mock.patch('sys.stdout.write')
    def testUnicodeErrorReturnsFalse(self, write):
        write.side_effect = UnicodeError()
        result = mocking.print_string('')
        self.assertFalse(result)

    def testDoesNotWriteIfIsATty(self):
        with mock.patch('sys.stdout') as m:
            m.isatty.return_value = True
            mocking.print_string('')
        self.assertFalse(m.write.called)

    def testUsingSpec(self):
        nospec = mock.Mock()
        nospec.wriite('hi')

        spec = mock.create_autospec(sys.stdout)
        self.assertRaises(AttributeError, getattr, spec, 'wriite')


class LogFileTests(unittest.TestCase):

    def testMockOpen(self):
        mopen = mock.mock_open(read_data='{"hi": 2}')
        with mock.patch('__builtin__.open', mopen):
            got = mocking.load_settings()
            self.assertTrue(mopen().__exit__.called)
        self.assertEqual(got, {'hi': 2})
