import json
import sys


def print_string(s):
    """Prints a string to sys.stdout.
    If the string prints, return True.
    Return False if it does not print because sys.stdout is not a terminal,
    or the string cannot be decoded.

    If s is not a string, iterate over s and print_string on each item.
    Return True if all strings were printed, False if any failed.
    """

    if not sys.stdout.isatty():
        return False
    if isinstance(s, basestring):
        try:
            sys.stdout.write(s + '\n')
            return True
        except UnicodeError:
            return False
    results = True
    for item in s:
        results = results and print_string(item)
    return results


def load_settings():
    """Loads the contents of the cwd's .settings file."""
    with open('.settings', 'r') as f:
        return json.load(f)
