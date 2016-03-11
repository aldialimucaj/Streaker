import unittest
import arrow
from streaker.random_generator import RandomGenerator


class TestRandomGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = RandomGenerator()
        print('RandomGenerator::setup()')

    def tearDown(self):
        print('RandomGenerator::teardown()')

    def test_random_generator_c1(self):
        self.assertEqual(self.generator.day_occurrence, '50%')
        self.assertEqual(self.generator.commits_per_day, '0')
        self.assertEqual(len(self.generator.commits), 0)

    def test_get_commits(self):
        self.assertIsNotNone(self.generator.get_commits())

    def test_parse_dates(self):
        commits = self.generator.parse_dates('50%')

    def test_generate_commits(self):
        now = arrow.utcnow()
        yesteryear = now.replace(year=now.year-1)
        self.generator.generate_commits(now, yesteryear, .5, 5)
        # assuming there will be more than 30%
        self.assertGreater(len(self.generator.commits), int(.3*365*5))
