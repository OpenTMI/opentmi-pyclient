import unittest
from opentmi_client.api import Build, Ci, Vcs


class TestBuild(unittest.TestCase):
    def test_construct(self):
        build = Build()
        build.name = 'test'
        self.assertIsInstance(build, Build)
        self.assertEqual(build.name, 'test')
        self.assertEqual(build.data, {'name': 'test'})

    def test_type(self):
        build = Build()
        with self.assertRaises(ValueError):
            build.type = 'invalid'
        build.type = 'test'
        self.assertEqual(build.type, 'test')

    def test_compiledBy(self):
        build = Build()
        with self.assertRaises(ValueError):
            build.compiledBy = 'invalid'
        build.compiledBy = 'CI'
        self.assertEqual(build.compiledBy, 'CI')

    def test_ci(self):
        build = Build()
        with self.assertRaises(TypeError):
            build.ci_tool = 'invalid'
        ci = Ci()
        with self.assertRaises(ValueError):
            ci.system = 'invalid'
        build.ci_tool = ci
        build.ci_tool.system = 'Jenkins'
        self.assertEqual(ci.system, 'Jenkins')


    def test_vcs(self):
        build = Build()
        with self.assertRaises(TypeError):
            build.vcs = 'invalid'
        vcs = Vcs()
        build.vcs = [vcs]
        build.vcs[0].name = 'wc'
        self.assertEqual(vcs.name, 'wc')
        vcs.type = 'PR'
        self.assertEqual(vcs.type, 'PR')
        vcs.base_branch = 'base'
        self.assertEqual(vcs.base_branch, 'base')
        vcs.branch = 'master'
        self.assertEqual(vcs.branch, 'master')
        vcs.base_commit = '123'
        self.assertEqual(vcs.base_commit, '123')
        vcs.clean_wa = True
        self.assertTrue(vcs.clean_wa)
        vcs.pr_number = '123'
        self.assertEqual(vcs.pr_number, '123')
        vcs.commitId = '123'
        self.assertEqual(vcs.commitId, '123')
        vcs.system = 'git'
        self.assertEqual(vcs.system, 'git')
        vcs.url = 'url'
        self.assertEqual(vcs.url, 'url')