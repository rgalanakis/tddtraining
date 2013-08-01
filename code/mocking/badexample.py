import os
import sqlite3
import time

import tictactoegame as ttt

_DBPATH = os.path.splitext(__file__)[0] + '.db'

def _getconn():
    needstables = not os.path.isfile(_DBPATH)
    conn = sqlite3.connect('badexample.db')
    if needstables:
        c = conn.cursor()
        c.execute('CREATE TABLE scoreboard '
                  '(starttime text, endtime text, result text)')
        conn.commit()
    return conn


def play_and_record_game():
    conn = _getconn()
    c = conn.cursor()
    starttime = time.time()
    c.execute("INSERT INTO scoreboard(starttime) values('%s')" % starttime)
    try:
        result = ttt.simulate_game()
    except:
        result = 'ERROR'
    endtime = time.time() + 0.01
    c.execute("""UPDATE scoreboard SET
        endtime = '%(endtime)s',
        result = '%(result)s'
    WHERE starttime = '%(starttime)s'""" % locals())
    conn.commit()


if __name__ == '__main__':
    for i in range(10):
        play_and_record_game()
    conn = _getconn()
    print 'DATABASE:'
    for row in conn.cursor().execute('SELECT * FROM scoreboard'):
        print row
