#!/usr/bin/env python3

import unittest
from lrank.ranker import Ranker
from lrank.error import FileNotFoundError


class RankerTestCase(unittest.TestCase):
    def setUp(self):
        return

    def test_file_not_exits(self):
        """
        If the input file is not found a FileNotFoundError should be raised.
        """
        test_ranker = Ranker()
        with self.assertRaises(FileNotFoundError):
            test_ranker.rank('missing_file.txt')

    def test_base_case(self):
        """
        Make sure the basic provided example passes the test.
        """
        example_input = 'test/data/input_single_duplicate.txt'
        expected_output = 'test/data/output_single_duplicate.txt'

        expected_results = get_expected_results(expected_output)

        test_ranker = Ranker()
        self.assertEqual(test_ranker.rank(example_input), expected_results, 'Did not rank the data correctly.')

    def test_multiple_duplicates(self):
        """
        Make sure that multiple duplicates are handled.
        """
        example_input = 'test/data/input_multiple_duplicates.txt'
        expected_output = 'test/data/output_multiple_duplicates.txt'

        expected_results = get_expected_results(expected_output)

        test_ranker = Ranker()
        self.assertEqual(test_ranker.rank(example_input), expected_results, 'Did not rank the data correctly.')


def get_expected_results(filename):
    """
    A utility method for reading the lines of a file and returning them as a list

    :param filename: str
    :return: list of str
    """
    with open(filename, 'r') as file_handle:
        expected_results = []

        for row in file_handle:
            expected_results.append(row.rstrip())

    return expected_results
