from abc import ABCMeta

class CommitGenerator(metaclass=ABCMeta):
    """
    Base class for commit generator. It could be inherited by random
    generators, ascii to bitmap writers or plain pixed drawing.
    """

    @abstractmethod
    def get_commits(self):
        pass

class Commit():
    """
    Commit model holding information about the commit
    """
    __slots__ = ('date')

    def __init__(self, date):
        self.date = date
