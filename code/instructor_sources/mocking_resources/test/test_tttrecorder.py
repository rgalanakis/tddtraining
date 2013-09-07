import mock
import sqlite3
import uuid
import unittest

from .. import tttrecorder


class TestRecordGame(unittest.TestCase):

    def setUp(self):
        self.uuid = 'uid'
        self.uuidpatch = mock.patch('uuid.uuid4').__enter__()
        self.uuidpatch.return_value = self.uuid

    def tearDown(self):
        self.uuidpatch.__exit__()

    def testRecordsStartTime(self):
        recorder = mock.Mock()
        tttrecorder.record_game(lambda: 'XWIN', recorder, gettime=lambda: 10)
        recorder.new_game.assert_called_once_with(self.uuid, 10)

    def testRecordsResultAndEndTime(self):
        recorder = mock.Mock()
        tttrecorder.record_game(lambda: 'XWIN', recorder, gettime=lambda: 10)
        recorder.end_game.assert_called_once_with(self.uuid, 'XWIN', 10)

    def testHandlesExceptionInGame(self):
        recorder = mock.Mock()
        sim = mock.Mock()
        sim.side_effect = RuntimeError
        tttrecorder.record_game(sim, recorder, gettime=lambda: 10)
        recorder.end_game.assert_called_once_with(self.uuid, 'ERROR', 10)


class TestRecorder(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect(':memory:')
        c = conn.cursor()
        c.execute('CREATE TABLE scoreboard '
                  '(guid text, starttime int, endtime int, result text)')
        conn.commit()
        self.conn = conn

    # def testNewGameQuery(self):
    #     conn = mock.Mock()
    #     rec = tttrecorder.Recorder(conn)
    #     rec.new_game('uid', 10)
    #     conn.execute.assert_called_once_with('INSERT INTO scoreboard(id, starttime) values(uid, 10)')
    #
    # def testEndGameQuery(self):
    #     conn = mock.Mock()
    #     rec = tttrecorder.Recorder(conn)
    #     rec.end_game('uid', 'XWIN', 10)
    #     conn.execute.assert_called_once_with('UPDATE scoreboard SET endtime=10, result=XWIN WHERE id=uid')

    def testNewGameCreatesRowAndSetsTime(self):
        rec = tttrecorder.Recorder(self.conn)
        uid = uuid.uuid4()
        rec.new_game(uid, 100)
        items = list(self.conn.execute('SELECT * FROM scoreboard'))
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][0], uid)
        self.assertEqual(items[0][1], 100)

        self.assertDictContainsSubset({'1': 1}, {'2': 2})


