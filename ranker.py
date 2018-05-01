#!/usr/bin/env python3

"""Ranker.

Usage:
  ranker.py rank <input> [--output=<output>]
  ranker.py (-h | --help)
  ranker.py --version

Options:
  -h --help             Show this screen.
  --version             Show version.
  <input>               Path to the input file.
  --output=<output>     Path to output file, default prints to stdout.

"""

from docopt import docopt
import os.path

class Ranker:
    def __init__(self, args):
        self.args = args
        self.leaderboard = {}

    def rank(self):
        if not os.path.isfile(self.args.get('<input>')):
            raise FileNotFoundError(self.args.get('<input>'), 'File not found.')
        return 1


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class FileNotFoundError(Error):
    """If the input file is not found.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


if __name__ == '__main__':
    args = docopt(__doc__, version='Ranker 1.0')
    ranker = Ranker(args)
    ranker.rank()
