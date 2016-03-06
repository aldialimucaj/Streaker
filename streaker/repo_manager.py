from git import Repo
import logging
import arrow
import os
import config

logger = logging.getLogger(__name__)
"""
RepoManager takes care of the repository operations such as
 - creating/opening a repo
 - generating change
 - committing with date
 - pushing
"""
class RepoManager(object):

    """
    RepoManager with set up date

    :param path: set a specific path to repo
    """
    def __init__(self, path=os.getcwd()):
        self.path = os.path.abspath(path)
        self.commit_file = config.COMMIT_FILE

    """
    Open existing repo passed in the constructor
    """
    def open_repo(self):
        pass
    """
    Create new repo from the path passed in the constructor
    """
    def create_repo(self):
        pass

    def create_commit(self, date=arrow.utcnow()):
        logger.info('Creating Commit on %s at %s', self.commit_file, date)
        commit_file = open(self.commit_file, 'w')
        commit_file.write('.')

    def test(self):
        logger.info('DateManager: test() > %s', self.path)
