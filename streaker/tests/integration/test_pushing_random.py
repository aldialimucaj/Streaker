import os
import shutil
import config
import unittest
import arrow
from git import Repo
from streaker.repo_manager import RepoManager
from streaker.random_generator import RandomGenerator
from streaker.commit_generator import Commit

TEST_PATH   = '/tmp/streaker_repo'
REMOTE_URL='git@github.com:aldialimucaj/streaker_test.git'


class PushingWithRandom(unittest.TestCase):

    def setUp(self):
       self.repo = RepoManager(path=TEST_PATH, remote_url=REMOTE_URL)
       self.generator = RandomGenerator()
       print('RepoManagerTest::setup()')

    def tearDown(self):
        self.rm_dir(TEST_PATH)
        print('RepoManagerTest::teardown()')

    def test_push_50_percent(self):
        # create commits
        now = arrow.utcnow()
        yesteryear = now.replace(year=now.year-1)
        self.generator.generate_commits(now, yesteryear, .5, 5)
        commits = self.generator.get_commits()
        # create repo
        self.repo.create_repo()
        for c in commits:
            self.repo.generate_change()
            self.repo.commit(c.date)
        # push
        self.repo.push_to_remote()