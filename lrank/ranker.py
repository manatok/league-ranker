import os.path
import csv
from .error import FileNotFoundError


class Ranker:
    """
    This class will:
    1. Read a formatted CSV file of match results.
    2. Update a leaderboard with allocated points per match.
    3. Return a ordered list of team standings.

    Example Usage:
        ranker = Ranker()
        leaderboard = ranker.rank("match_results.csv")

    Example file contents:
        Lions 3, Snakes 3
        Tarantulas 1, FC Awesome 0
        Lions 1, FC Awesome 1
        Tarantulas 3, Snakes 1
        Lions 4, Grouches 0

    Example Output:
        ['1. Tarantulas, 6 pts', '2. Lions, 5 pts', '3. FC Awesome, 1 pt', '3. Snakes, 1 pt', '5. Grouches, 0 pts']

    """
    def __init__(self):
        self._leaderboard = {}

    def rank(self, filename):
        """
        The entry point of this class. Takes a CSV file of league match results and
        returns an ordered list of team points in descending order.

        :param filename: str
        :return: list of str
        :raises: FileNotFoundError
        """
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename, 'File not found.')

        for team1_result, team2_result in self._get_next_result(filename):
            self._update_leaderboard(self._get_assigned_points(
                team1_result, team2_result))

        return self._get_formatted_leaderboard()


    def _get_next_result(self, filename):
        """
        A generator function for looping over input file.

        :param filename: str
        :return: str
        """
        with open(filename, "rt") as input_file:
            reader = csv.reader(input_file)
            for row in reader:
                yield row


    def _update_leaderboard(self, results):
        """
        Assign the allocated points to the teams in the leaderboard.

        :param results: dict {team_name: points, ...}
        :return: None
        """
        for team_name in results:
            self._leaderboard[team_name] = self._leaderboard.get(team_name, 0) + \
                                           results[team_name]


    def _get_assigned_points(self, team1_result, team2_result):
        """
        Based on the score of the match, assign points to the two teams.

        Win = 3 points
        Draw = 1 point
        Loss = 0 points

        :param team1_result: str
        :param team2_result: str
        :return: dict {team_name: points, ...}
        """
        team1_score = self._get_score(team1_result)
        team2_score = self._get_score(team2_result)

        team1_points = team2_points = 0

        if team1_score == team2_score:
            team1_points = team2_points = 1
        elif team1_score > team2_score:
            team1_points = 3
        else:
            team2_points = 3

        return {self._get_team_name(team1_result): team1_points,
                self._get_team_name(team2_result): team2_points}


    def _get_formatted_leaderboard(self):
        """
        Sorts the leaderboard and returns a nice human-readable points list.

        :return: list of str
        """
        i = 0
        formatted_output = []
        last_team_points = -1
        position = -1

        for row in self._sort():
            i = i + 1

            if last_team_points != row[1]:
                position = i

            last_team_points = row[1]

            metric = 'pts'
            if row[1] == 1:
                metric = 'pt'

            formatted_output.append("%d. %s, %d %s" % (position, row[0], row[1], metric))

        return formatted_output

    def _sort(self):
        """
        Sorts by value desc, key asc

        :return: list of dict
        """
        return sorted(self._leaderboard.items(), key=lambda x: (-x[1], x[0]))

    def _get_score(self, team_result):
        """
        Remove the score portion from the result string. Assumes the score is the value after
        the last space.

        :param team_result: str
        :return: int
        """
        return team_result.rsplit(" ", 1)[1]

    def _get_team_name(self, team_result):
        """
        Remove the team name portion from the result string. Assumes the name is the section
        before the last space.

        :param team_result:
        :return:
        """
        return team_result.rsplit(" ", 1)[0].strip()

