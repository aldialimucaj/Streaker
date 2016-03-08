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
        self.commit_file = os.path.join(self.path, config.COMMIT_FILE)

    """
    Open existing repo passed in the constructor
    """
    def open_repo(self):
        if os.path.isdir(os.path.join(self.path, '.git')):
            self.repo = Repo(self.path)
            return self.repo != None

        return False

    """
    Create new repo from the path passed in the constructor.

    Returns true if new repo created
    """
    def create_repo(self):
        if not os.path.isdir(os.path.join(self.path, '.git')):
            os.mkdir(self.path)
            self.repo = Repo.init(self.path)
            return True
        else:
            self.repo = Repo(self.path)

        return False

    """
    Generate change to the COMMIT_FILE in order to create a commit.
    """
    def generate_change(self):
        logger.info('Generating change on %s ', self.commit_file)
        commit_file = open(self.commit_file, 'w')
        # write a predefined value to the file
        commit_file.write(config.COMMIT_VALUE)

    """
    Commit changes with date.

    :param date: specific date to commit changes to. defaults to now
    """
    def commit(self, date=arrow.utcnow()):
        logger.info('Commiting > %s at %s', self.commit_file, date)
