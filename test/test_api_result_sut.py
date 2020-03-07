import unittest
from opentmi_client.api import Sut


class TestResultSut(unittest.TestCase):
    def test_construct(self):
        sut = Sut()
        sut.branch = 'test'
        self.assertIsInstance(sut, Sut)
        self.assertEqual(sut.branch, 'test')
        self.assertEqual(sut.data, {'branch': 'test'})

    def test_build_sha1(self):
        sut = Sut()
        sut.build_sha1 = '123'
        self.assertEqual(sut.build_sha1, '123')
        self.assertEqual(sut.data, {'buildSha1': '123'})

    def test_commit_id(self):
        sut = Sut()
        sut.commit_id = '123'
        self.assertEqual(sut.commit_id, '123')
        self.assertEqual(sut.data, {'commitId': '123'})

    def test_tag(self):
        sut = Sut()
        sut.tag = ['123', '456']
        self.assertEqual(sut.tag, ['123', '456'])
        self.assertEqual(sut.data, {'tag': ['123', '456']})
