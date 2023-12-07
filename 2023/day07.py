# https://adventofcode.com/2023/day/7

from collections import *

TEST = 0

file = 'input/' + ('test.txt' if TEST else 'in.txt')


# read all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]


# get total hand's stregth by checking # of occurences of each card
def getType(hand, part2=False):
    numjokers = 0
    if part2:  # if part 2, get count of jokers
        numjokers = hand.count('J')
        hand = hand.replace('J', '')
    faceCounts = sorted(Counter(hand).values(), reverse=True)
    faceCounts.append(0)
    faceCounts[0] += numjokers

    # check counts of most occuring card to
    # decide what kind of hand it is
    if faceCounts[0] == 5:  # Five of a kind
        return 7
    elif faceCounts[0] == 4:  # Four of a kind
        return 6
    elif faceCounts[0] == 3:
        if faceCounts[1] == 2:
            return 5  # Full house
        else:
            return 4  # Three of a kind
    elif faceCounts[0] == 2:
        if faceCounts[1] == 2:
            return 3  # Two pair
        else:
            return 2  # One pair
    else:
        return 1  # High Card


# convert letter values into numbers
def getCardValues(card):
    return [int(i) if i.isdigit() else letterValues[i] for i in card]


# solve for entire input
def solve(isPart2=False):
    # first, collect all hands' types, values (array of card values -- A=14, K=13 and so on) and bids.
    game = []
    for line in all:
        hand, bid = line.split()
        bid = int(bid)
        game.append((getType(hand, part2=isPart2), getCardValues(hand), bid, hand))

    # sort cards based primarily on strength, followed by on values of the faces
    sortedgame = sorted(
        game,
        key=lambda hand: (15**10) * hand[0]
        + sum(
            [15 ** (6 - index) * faceValue for index, faceValue in enumerate(hand[1])]
        ),
    )

    # game score is the sum of rank*bid for all cards.
    return sum([(i + 1) * c[2] for i, c in enumerate(sortedgame)])


p = print
all = lines()

# dict cardValue:numericalValue
letterValues = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}


print('Part 1:', solve())

# Jokers have value 1 for any calculations
letterValues['J'] = 1
print('Part 2:', solve(isPart2=True))