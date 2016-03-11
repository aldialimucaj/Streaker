from streaker.commit_generator import (CommitGenerator, Commit)


class RandomGenerator(CommitGenerator):
    """
    Generate random commits
    """

    def __init__(self, probability_day='50%',commits_per_day='0'):
        self.probability_day = probability_day
        self.commits_per_day = commits_per_day
        self.commits = []

    """
    Returns all generated commits as a list

    :return: list of commit objects
    """
    def get_commits(self):
        return self.commits
