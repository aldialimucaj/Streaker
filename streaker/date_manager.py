import logging


logger = logging.getLogger(__name__)

class DateManager(object):

    """docstring for DateManager"""
    def __init__(self, date):
        self.date = date

    def test(self):
        logger.info('DateManager: test')
