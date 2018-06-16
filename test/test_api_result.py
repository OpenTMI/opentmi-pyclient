import unittest
from opentmi_client.api import Result


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