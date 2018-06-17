import unittest
from opentmi_client.api import Result, Execution


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
