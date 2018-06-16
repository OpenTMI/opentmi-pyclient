import unittest
from opentmi_client.utils.Base import BaseApi


class TestBase(unittest.TestCase):
    def test_basics(self):
        base = BaseApi()
        self.assertEqual(base.data, {})
        self.assertEqual(str(base), '{}')
        self.assertTrue(base.empty)

    def test_set(self):
        base = BaseApi()
        base.set('a', 1)
        self.assertEqual(base.data, {'a': 1})
        self.assertEqual(str(base), '{\n  "a": 1\n}')
        self.assertFalse(base.empty)
        self.assertEqual(base.get('a'), 1)

    def test_unset(self):
        base = BaseApi()
        base.set('a', 1)
        base.unset('a')
        self.assertTrue(base.empty)

    def test_nested(self):
        base = BaseApi()
        base.set('a.b.c', 2)
        self.assertEqual(base.data, {'a': {'b': {'c': 2}}})
        self.assertEqual(str(base), '{\n  "a": {\n    "b": {\n      "c": 2\n    }\n  }\n}')
        self.assertEqual(base.get('a.b.c'), 2)
