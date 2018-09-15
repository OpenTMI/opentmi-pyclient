import os
import unittest
from opentmi_client.utils import is_object_id, resolve_host, archive_files, remove_empty_from_dict


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
        self.assertEqual(resolve_host("https://mydomain"), "https://mydomain")
        self.assertEqual(resolve_host("https://1.2.3.4:3000"), "https://1.2.3.4:3000")
        self.assertEqual(resolve_host("https://1.2.3.4", 3000), "https://1.2.3.4:3000")

    def test_archive(self):
        zip = 'temp.zip'
        cur_dir = os.path.dirname(__file__)
        file_to_zip = os.path.join(cur_dir, 'test_tools.py')
        archive_files([file_to_zip], zip, cur_dir)
        self.assertTrue(os.path.exists(zip))
        os.remove(zip)

    def test_remove_empty_from_dict(self):
        data = {"a": {"b": {}, "c": [], "d": 1}}
        self.assertEqual(remove_empty_from_dict(data), {"a": {"d": 1}})

if __name__ == '__main__':
    unittest.main()
