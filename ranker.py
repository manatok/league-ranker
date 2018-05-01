#!/usr/bin/env python3

"""Ranker.

Usage:
  ranker.py rank [--input=<input>] [--output=<output>]
  ranker.py (-h | --help)
  ranker.py --version

Options:
  -h --help             Show this screen.
  --version             Show version.
  --input=<input>       Path to the input file.
  --output=<output>     Path to output file.

"""

from docopt import docopt


class Ranker:
    def __init__(self, args):
        self.args = args

    def rank(self):
        return 1


if __name__ == '__main__':
    args = docopt(__doc__, version='Ranker 1.0')
    ranker = Ranker(args)
    print (ranker.rank())
