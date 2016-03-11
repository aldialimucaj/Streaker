from git import (Repo, Actor, GitCommandError)
import logging
import arrow
import os
import config

logger = logging.getLogger(__name__)


class RepoManager(object):
    """
    RepoManager takes care of the repository operations such as
     - creating/opening a repo
     - generating change
     - committing with date
     - pushing
    """

    def __init__(self, **kwargs):
        """
        RepoManager with set up date

        :param path: set a specific path to repo
        """
        self.path = os.path.abspath(kwargs.get('path',os.getcwd()))
        self.remote_url = kwargs.get('remote_url')
        self.commit_file = os.path.join(self.path, config.COMMIT_FILE)

    def open_repo(self):
        """
        Open existing repo passed in the constructor

        :return: True if repo exists and accessable
        """
        if self.check_rights and os.path.isdir(os.path.join(self.path, '.git')):
            self.repo = Repo(self.path)
            return self.repo != None

        return False

    def create_repo(self):
        """
        Create new repo from the path passed in the constructor.

        :return: True if new repo created
        """
        if not os.path.isdir(os.path.join(self.path, '.git')):
            try:
                os.mkdir(self.path)
                self.repo = Repo.init(self.path)
                return True
            except (IOError, OSError) as e:
                logger.error('create_repo(%s) - %s', self.path, e)
        else:
            self.repo = Repo(self.path)

        return False

    def generate_change(self):
        """
        Generate change to the COMMIT_FILE in order to create a commit.

        :return: True if could write to file
        """
        logger.info('Generating Change > %s ', self.commit_file)
        try:
            commit_file = open(self.commit_file, 'w')
            # write a predefined value to the file
            commit_file.write(config.COMMIT_VALUE)
            return True
        except (IOError, OSError) as e:
            logger.error('generate_change(%s) - %s', self.commit_file, e)

        return False

    def commit(self, date=arrow.utcnow()):
        """
        Commit changes with date.

        :param date: specific date to commit changes to. defaults to now
        """
        logger.info('Commiting > %s at %s', self.commit_file, date)
        index = self.repo.index
        index.add([self.commit_file])
        commit_time = date.format('YYYY-MM-DDTHH:mm:ss')
        index.commit(config.COMMIT_MESSAGE, commit_date=commit_time, author_date=commit_time)


    def push_to_remote(self):
        """
        Push new commits to GitHub repository

        :return: True if succeeded
        """
        # if the remote url was not specified then return
        if not self.remote_url:
            logger.error('push_to_remote() without URL')
            return False

        origin = None

        # only one remote will be used
        if len(self.repo.remotes) > 0 and self.repo.remotes[0]:
            origin = self.repo.remotes.origin

        if not origin:
            # if origin does not exist, then create a local one with remote origin url
            origin = self.repo.create_remote(name='origin',url=self.remote_url)

        try:
            origin.push(self.repo.heads.master,force=True)
        except GitCommandError as e:
            logger.error('push_to_remote(%s) - %s', self.remote_url, e)

        return True

    def pull_from_remote(self):
        """
        Pull changes from remote GitHub repo_mgr

        :return: True if succeeded
        """
        # if the remote url was not specified then return
        if not self.remote_url:
            logger.error('push_to_remote() without URL')
            return False

        origin = None

        # only one remote will be used
        if len(self.repo.remotes) > 0 and self.repo.remotes[0]:
            origin = self.repo.remotes.origin

        if not origin:
            # if origin does not exist, then create a local one with remote origin url
            origin = self.repo.create_remote(name='origin',url=self.remote_url)

        # pull and push to remote
        try:
            origin.fetch()
            origin.pull('master', force=True)
        except GitCommandError as e:
            logger.error('push_to_remote(%s) - %s', self.remote_url, e)

        return True

    def check_rights(self):
        """
        Checks if the user has write access to the member path.
        If the path does not exist, than it checks the parent folder.

        :return: True if user has os.W_OK rights on the folder
        """
        # check full path
        if os.path.isdir(self.path):
            return os.access(self.path,os.W_OK)
        # check parent
        else:
            return os.access(os.path.dirname(self.path),os.W_OK)
