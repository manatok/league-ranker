# Welcome to lrank!

lrank is a basic Python3 cli application used for generating a sorted leaderboard from soccer league match results.

### Example Input:
Here is the content of an example input file:
```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```
### Example Output:
Given the example input file above, the app will output the follow:
```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

## Installation and Running
### Requirements
1. Python3
2. pip3
### Installation
1. Clone out the repo.
2. `cd league-ranker/`
3. `chown +x install.sh`
4. `./install.sh`

At this point you should have a binary `lrank` available to use.

### Running
`lrank path/to/input/file.txt`

This will output to stdout, so if you want to write the output to a file you can simply run:

`lrank path/to/input/file.txt > path/to/output.txt`


## Running the Tests
1. `cd league-ranker/`
2. `python3 -m unittest test.ranker_test`

