#!/usr/bin/env python3

import unittest
from ranker import Ranker

class RankerTestCase(unittest.TestCase):
    def setUp(self):
        self.ranker = Ranker(())

    def test_it(self):
        self.assertEqual(self.ranker.rank(), 1, 'incorrect')