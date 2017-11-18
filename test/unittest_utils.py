import os
import unittest
from .mock import MagicMock
from opentmi_client.utils import Query, Find, is_object_id, resolve_host, archive_files


class TestRequest(unittest.TestCase):

    def test_query_empty(self):
        self.assertEqual(Query().to_string(), "{}")

    def test_query_set(self):
        self.assertEqual(Query().set("a", "b").to_string(), '{"a": "b"}')

    def test_find_empty(self):
        self.assertDictEqual(Find().params(), {"t": "find", "q": "{}"})

    def test_find_limit(self):
        self.assertDictEqual(Find().limit(1).params(), {"t": "find", "l": 1, "q": "{}"})

    def test_find_skip(self):
        self.assertDictEqual(Find().skip(1).params(), {"t": "find", "sk": 1, "q": "{}"})

    def test_find_select(self):
        self.assertDictEqual(Find().select("aa").params(), {"t": "find", "f": "aa", "q": "{}"})

    def test_find_select_multi(self):
        self.assertDictEqual(Find()
                             .select("aa")
                             .select("bb")
                             .params(),
                             {"t": "find", "f": "aa bb", "q": "{}"})

    def test_find_query(self):
        find = Find()
        find.query.set("a", "b")
        self.assertDictEqual(find.params(), {"t": "find", "q": '{"a": "b"}'})


class TestTools(unittest.TestCase):
    def test_is_object_id(self):
        self.assertEqual(is_object_id(""), False)
        self.assertEqual(is_object_id("asd"), False)
        self.assertEqual(is_object_id(None), False)
        self.assertEqual(is_object_id(1), False)
        self.assertEqual(is_object_id("1234567890abcdef78901234"), True)

    def test_resolve_host(self):
        self.assertEqual(resolve_host("1.2.3.4"), "http://1.2.3.4")
        self.assertEqual(resolve_host("1.2.3.4", 80), "http://1.2.3.4")
        self.assertEqual(resolve_host("1.2.3.4", 8000), "http://1.2.3.4:8000")
        self.assertEqual(resolve_host("1.2.3.4:3000"), "http://1.2.3.4:3000")
        self.assertEqual(resolve_host("http://1.2.3.4"), "http://1.2.3.4")
        self.assertEqual(resolve_host("https://1.2.3.4"), "https://1.2.3.4")
        self.assertEqual(resolve_host("https://1.2.3.4:3000"), "https://1.2.3.4:3000")
        self.assertEqual(resolve_host("https://1.2.3.4", 3000), "https://1.2.3.4:3000")

    def test_archive(self):
        zip = 'temp.zip'
        archive_files(['unittest_utils.py'], zip, os.path.dirname(__file__))
        self.assertTrue(os.path.exists(zip))
        os.remove(zip)

if __name__ == '__main__':
    unittest.main()