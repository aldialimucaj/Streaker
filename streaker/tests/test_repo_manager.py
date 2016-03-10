import os
import shutil
import config
import unittest
import arrow
from streaker.repo_manager import RepoManager
from git import Repo

# CAREFUL this path will be deleted
TEST_PATH = '/tmp/streaker_repo'
TMP_PATH = '/tmp/'

class RepoManagerTest(unittest.TestCase):

    def setUp(self):
        self.repo = RepoManager(path=TEST_PATH)
        print('RepoManagerTest::setup()')

    def tearDown(self):
        if os.path.isdir(TEST_PATH):
            shutil.rmtree(TEST_PATH)
        print('RepoManagerTest::teardown()')

    # testing default constructor with no path -> current dir
    def test_repo_manager_c1_1(self):
        repo_mgr = RepoManager()
        self.assertEqual(repo_mgr.path, os.getcwd())
        self.assertEqual(repo_mgr.commit_file, os.path.join(os.getcwd(),config.COMMIT_FILE))

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
        # should not be able to create repo in restricted dir
        new_repo = RepoManager(path='/root/repo')
        self.assertFalse(new_repo.create_repo())

    def test_generate_change(self):
        full_path = os.path.join(TEST_PATH, config.COMMIT_FILE)
        print(full_path)
        self.assertFalse(os.path.isfile(full_path))
        self.assertTrue(self.repo.create_repo())
        self.repo.generate_change()
        self.assertTrue(os.path.isfile(full_path))

    def test_commit(self):
        # prepare the repo
        new_repo = RepoManager(path='/tmp/tostay')
        new_repo.create_repo()
        new_repo.generate_change()
        # create a date at set to a year ago
        commit_time = arrow.utcnow()
        commit_time= commit_time.replace(year=2015,month=1,day=1)
        # commit with fake date
        new_repo.commit(commit_time)
        headcommit = new_repo.repo.head.commit
        test_commit_date = arrow.get(headcommit.authored_date)
        self.assertEqual(test_commit_date.year, 2015)
        self.assertEqual(test_commit_date.month, 1)
        self.assertEqual(test_commit_date.day, 1)

    def test_push_to_remote(self):
        # this test would fail on Travis because of credentials
        if os.getenv('TRAVIS'): return

        self.assertFalse(self.repo.push_to_remote())
        # repo with remote
        new_repo = RepoManager(path='/tmp/tostay', remote_url='git@github.com:aldialimucaj/streaker_test.git')
        new_repo.create_repo()
        new_repo.generate_change()
        self.assertTrue(new_repo.push_to_remote())


    def test_check_rights(self):
        self.assertTrue(self.repo.check_rights())
        # should not be able to create repo in restricted dir
        new_repo = RepoManager(path='/root/repo')
        self.assertFalse(new_repo.check_rights())
        new_repo = RepoManager(path='/')
        self.assertFalse(new_repo.check_rights())
