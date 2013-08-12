import argparse
import os
import shutil
import SimpleHTTPServer
import sys

THISDIR = os.path.dirname(__file__)

# noinspection PyUnresolvedReferences
PRESMD = os.path.join(THISDIR, 'presentation.md')


def main():
    p = argparse.ArgumentParser()
    p.add_argument(
        'presentation',
        default=os.path.join(THISDIR, 'defaultpresentation.md'))
    p.add_argument('--port', type=int, default=34567)
    p.add_argument(
        '-u', '--update', action='store_true',
        help='If provided, just copy the presentation so it can be '
             'reloaded by the browser.')
    opts = p.parse_args()

    presentation = os.path.abspath(opts.presentation)
    print 'Presenting', presentation
    shutil.copyfile(presentation, PRESMD)

    if opts.update:
        print 'Updated, not serving.'
        return

    del sys.argv[1:]
    sys.argv.append(str(opts.port))

    os.chdir(THISDIR)
    SimpleHTTPServer.test()

if __name__ == '__main__':
    main()
