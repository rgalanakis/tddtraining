import uuid

def record_game(simulate_game, recorder, gettime):
    recorder.new_game(uuid.uuid4(), gettime())
    try:
        result = simulate_game()
    except Exception:
        result = 'ERROR'
    recorder.end_game(uuid.uuid4(), result, gettime())


class Recorder(object):

    def __init__(self, conn):
        self.conn = conn

    def new_game(self, uid, starttime):
        self.conn.cursor().execute("INSERT INTO scoreboard(guid, starttime) values('%s', %s);" % (uid, starttime))

    def end_game(self, uid, result, endtime):
        self.conn.cursor().execute('UPDATE scoreboard SET endtime=%(endtime)s, result=%(result)s WHERE id=%(uid)s' % locals())
