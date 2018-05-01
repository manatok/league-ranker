#!/usr/bin/env python3

import unittest
from ranker import *

class RankerTestCase(unittest.TestCase):
    def setUp(self):
        return

    def test_file_exits(self):
        test_ranker = Ranker({'<input>': 'example_input.txt'})
        self.assertEqual(test_ranker.rank(), 1, 'incorrect')

    def test_file_not_exits(self):
        test_ranker = Ranker({'<input>': 'unknown_file.txt'})
        with self.assertRaises(FileNotFoundError):
            test_ranker.rank()