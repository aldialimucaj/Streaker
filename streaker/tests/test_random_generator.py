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
        self.assertEqual(self.generator.probability_day, '50%')
        self.assertEqual(self.generator.commits_per_day, '0')
        self.assertEqual(len(self.generator.commits), 0)

    def test_get_commits(self):
        self.assertIsNotNone(self.generator.get_commits())
