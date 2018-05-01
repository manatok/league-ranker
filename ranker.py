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
import csv


class Ranker:
    def __init__(self, args):
        self._args = args
        self._leaderboard = {}

    def rank(self):
        filename = self._args.get('<input>')

        if not os.path.isfile(filename):
            raise FileNotFoundError(filename, 'File not found.')

        for team1_result, team2_result in self._get_game_result(filename):
            self._update_leaderboard(self.get_assigned_points(team1_result, team2_result))

        for row in self._format():
            print (row)

    def _format(self):
        i = 0
        for row in self._sort():
            i = i + 1
            metric = 'pts'
            if row[1] == 1:
                metric = 'pt'

            yield "%d. %s, %d %s" % (i, row[0], row[1], metric)

    def _sort(self):
        return sorted(self._leaderboard.items(), key=lambda x: (-x[1],x[0]))

    def _update_leaderboard(self, results):
        for team_name in results:
            self._leaderboard[team_name] = self._leaderboard.get(team_name, 0) + results[team_name]

    def _get_game_result(self, filename):
        with open(filename, "rt") as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                yield row

    def get_assigned_points(self, team1_result, team2_result):
        team1_score = self.get_score(team1_result)
        team2_score = self.get_score(team2_result)

        team1_points = team2_points = 0

        if team1_score == team2_score:
            team1_points = team2_points = 1
        elif team1_score > team2_score:
            team1_points = 3
        else:
            team2_points = 3

        return {self.get_team_name(team1_result): team1_points, self.get_team_name(team2_result): team2_points}


    def get_score(self, team_result):
        return team_result.rsplit(" ", 1)[1]

    def get_team_name(self, team_result):
        return team_result.rsplit(" ", 1)[0].strip()


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
