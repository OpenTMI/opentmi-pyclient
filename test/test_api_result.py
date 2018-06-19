import unittest
from opentmi_client.api import Result, Execution, File


class TestResult(unittest.TestCase):
    def test_construct(self):
        result = Result()
        result.tcid = 'test'
        self.assertIsInstance(result, Result)
        self.assertEqual(result.tcid, 'test')
        self.assertEqual(result.data, {'tcid': 'test'})

    def test_verdict(self):
        result = Result()
        result.verdict = 'pass'
        self.assertEqual(result.verdict, 'pass')

    def test_execution(self):
        result = Result()
        result.execution.duration = 12.0
        self.assertEqual(result.execution.duration, 12.0)
        result.execution = Execution()
        result.execution.note = 'notes'
        self.assertEqual(result.execution.note, 'notes')
        self.assertEqual(result.execution.duration, None)

    def test_file(self):
        result = Result()
        log_file = File()
        log_file.name = "stderr.log"
        self.assertEqual(log_file.name, "stderr.log")
        log_file.set_data("test")
        self.assertEqual(log_file.encoding, "raw")
        self.assertEqual(str(log_file), "stderr.log")
        self.assertEqual(log_file.data.decode(), "test")
        result.execution.append_log(log_file)
        self.assertEqual(len(result.execution.logs), 1)
        self.assertEqual(result.execution.logs[0], log_file)
