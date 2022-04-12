# Simulate a sports tournament
# In soccer’s World Cup, the knockout round consists of 16 teams. In each round, each team plays another
#  team and the losing teams are eliminated. When only two teams remain, the winner of the final match 
#  is the champion.

# In soccer, teams are given FIFA Ratings, which are numerical values representing each team’s relative 
# skill level. Higher FIFA ratings indicate better previous game results, and given two teams’ FIFA ratings, 
# it’s possible to estimate the probability that either team wins a game based on their current ratings. 
# The FIFA Ratings from just before the two previous World Cups are available as the May 2018 Men’s FIFA 
# Ratings and March 2019 Women’s FIFA Ratings.

# Using this information, we can simulate the entire tournament by repeatedly simulating rounds until 
# we’re left with just one team. And if we want to estimate how likely it is that any given team wins 
# the tournament, we might simulate the tournament many times (e.g. 1000 simulations) and count how many 
# times each team wins a simulated tournament.


import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    filename = sys.argv[1]

    teams = []

    # First up is opening provided file and by using dictreader from csv
    # populating our teams list. Here is csv documenation necessary. By
    # reading the file row by row, and changing the rating from default
    # string to int, we can just append this new dicts to our list.

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['rating'] = int(row['rating'])
            teams.append(row)

    counts = {}

    # Last up is populating our counts dict. This one is best done by
    # iterating n times, creating winners by using sim_tour func. and
    # checking if the name of the winner is already in counts. If it
    # is then we just increment the value by one. If not, we set the
    # value to 1, as it is their first win.

    for i in range(N):
        winner = simulate_tournament(teams)
        if winner in counts:
            counts[winner] += 1
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners

# Second is creating a simulate tournament function. Here we needed
# a little help from Brian. This function creates a loop that goes on
# until one team is left, and for each it simulates a round leaving
# only one winner from clash of two teams. The function then returns
# just a name of the team that won, which is at [0] of teams list,
# and that name is later passed onto counts function.


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    while len(teams) > 1:
        teams = simulate_round(teams)
    return teams[0]['team']


if __name__ == "__main__":
    main()
