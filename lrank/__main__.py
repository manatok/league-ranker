#!/usr/bin/env python3

"""Ranker.

Usage:
  lrank <input>
  lrank (-h | --help)
  lrank --version

Options:
  -h --help             Show this screen.
  --version             Show version.
  <input>               Path to the input file.
  example:              `lrank test/data/input_single_duplicate.txt`


"""

from docopt import docopt
from .ranker import Ranker
from .error import FileNotFoundError
import sys


def main():
    args = docopt(__doc__, version='Ranker 1.0')
    try:
        ranker = Ranker()
        leaderboard = ranker.rank(args.get('<input>'))

        print ("\n".join(leaderboard))

    except FileNotFoundError:
        print("Error: {0}".format(sys.exc_info()[1]))


if __name__ == '__main__':
    main()
