import logging
import arrow

logger = logging.getLogger(__name__)

class RepoManager(object):

    """
    RepoManager with set up date

    :param path: set a specific path to repo
    """
    def __init__(self, date='.'):
        self.date = date

    def test(self):
        logger.info('DateManager: test() > %s', self.date)
