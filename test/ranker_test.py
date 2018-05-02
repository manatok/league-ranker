#!/usr/bin/env python3

import unittest
from lrank.ranker import Ranker
from lrank.error import FileNotFoundError

class RankerTestCase(unittest.TestCase):
    def setUp(self):
        return

    def test_file_not_exits(self):
        test_ranker = Ranker()
        with self.assertRaises(FileNotFoundError):
            test_ranker.rank('missing_file.txt')

    def test_single_duplicate(self):
        example_input = 'test/data/input_single_duplicate.txt'
        expected_output = 'test/data/output_single_duplicate.txt'

        with open(expected_output, 'r') as file_handle:
            expected_results = []

            for row in file_handle:
                expected_results.append(row.rstrip())

            test_ranker = Ranker()
            self.assertEqual(test_ranker.rank(example_input), expected_results, 'Did not rank the data correctly.')

    def test_multiple_duplicates(self):
        example_input = 'test/data/input_multiple_duplicates.txt'
        expected_output = 'test/data/output_multiple_duplicates.txt'

        with open(expected_output, 'r') as file_handle:
            expected_results = []

            for row in file_handle:
                expected_results.append(row.rstrip())

            test_ranker = Ranker()
            self.assertEqual(test_ranker.rank(example_input), expected_results, 'Did not rank the data correctly.')