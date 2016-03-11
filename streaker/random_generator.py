import arrow
import random
import logging
from streaker.commit_generator import (CommitGenerator, Commit)

logger = logging.getLogger(__name__)


class RandomGenerator(CommitGenerator):
    """
    Generate random commits
    """

    def __init__(self, day_occurrence='50%', commits_per_day='0'):
        self.day_occurrence = day_occurrence
        self.commits_per_day = commits_per_day
        self.commits = []

    def get_commits(self):
        """
        Returns all generated commits as a list

        :return: list of commit objects
        """
        return self.commits

    def parse_dates(self, day_occurrence):
        """
        Parses the dates from an input string.

        :param day_occurrence: string representing dates with following options
            - percentage: 50% every day has a 50% chance of getting chosen.
        """
        pass

    def generate_commits(self, start_date, end_date, probability=.5, daily_commits=17):
        """
        Generate commits based on the predicates

        :param start_date: when should it start. this should be the more current date eg. 2016
        :param end_date: when should it stop. this should be the older date eg. 2015
        :param probability: what probability should be used to pick a day to generate commits
        :param daily_commits: repeat the same probability if that day was picked many times
        """
        if end_date > start_date:
            return False, 'start_date hast to be the most recent one'

        cursor_date = arrow.get(start_date)
        cursor_date = cursor_date.replace(hour=1, minute=1, second=1)
        while cursor_date > end_date:
            r = random.random()
            if r <= probability:
                continue
            for i in range(daily_commits):
                r = random.random()
                if r <= probability:
                    #logger.debug('generate_commits(%s, %s) adding commit on %s',start_date,end_date,cursor_date)
                    cursor_date = cursor_date.replace(seconds=+1)
                    c = Commit(cursor_date)
                    self.commits.append(c)
            cursor_date = cursor_date.replace(days=-1, hour=1, minute=1, second=1)

        return True
