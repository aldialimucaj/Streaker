import os
import shutil
import config
import unittest
from streaker.repo_manager import RepoManager
from git import Repo

# CAREFUL this path will be deleted
TEST_PATH = '/tmp/streaker_repo'

class RepoManagerTest(unittest.TestCase):

    def setUp(self):
        self.repo = RepoManager(TEST_PATH)
        print('RepoManagerTest::setup()')

    def tearDown(self):
        if os.path.isdir(TEST_PATH):
            shutil.rmtree(TEST_PATH)
        print('RepoManagerTest::teardown()')

    # testing default constructor with no path -> current dir
    def test_repo_manager_c1_1(self):
        repo_mgr = RepoManager()
        self.assertEqual(repo_mgr.path, os.getcwd())
        self.assertEqual(repo_mgr.commit_file, config.COMMIT_FILE)

    def test_open_repo(self):
        self.assertFalse(os.path.isdir(TEST_PATH))
        self.assertFalse(self.repo.open_repo())
        # create a repo and try to open it
        Repo.init(TEST_PATH)
        self.assertTrue(self.repo.open_repo())


    def test_create_repo(self):
        self.assertFalse(os.path.isfile(TEST_PATH))
        self.assertTrue(self.repo.create_repo())
        self.assertFalse(self.repo.create_repo())
