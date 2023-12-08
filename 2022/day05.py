# https://adventofcode.com/2022/day/5

TEST = 0
file = 'input/' + ('test.txt' if TEST else 'in.txt')

from re import *

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip('\n') for x in f.readlines()]

# return a list of all nums in the line
def nums(line):
    return list(map(int, sub('\D+', ' ', line).strip().split()))

# read input and get the configuration of crates
def getCrates(numCrates):
    crates = [[] for _ in range(numCrates)]
    for i in range(cratesLines):
        for j in range(numCrates):
            char = all[i][1 + j * 4]
            if char.isalpha():  # ignore empty spaces
                crates[j].append(char)
    return crates

# run through moves,
# calculate final configuration of crates,
# return answer
def solveCrates(crates, doPart2=False):
    for line in all[cratesLines + 2 :]:
        count, sourceIndex, destinationIndex = nums(line)
        sourceIndex -= 1
        destinationIndex -= 1
        for i in range(count):
            # part 1: pop topmost crate 'count' times
            # part 2: pop the crate with a decreasing offset, 'count' times.
            l = crates[sourceIndex].pop(count - i - 1 if doPart2 else 0)
            crates[destinationIndex].insert(0, l)
    # return list of topmost crates
    return ''.join([str(c[0]) for c in crates])


p = print

all = lines()
cratesLines = -1
# get index of line with crate numbers
for i in all:
    if i == '':
        break
    # cratesLines ends up being index of
    # the first line storing integers
    cratesLines += 1

# get total number of crates
numCrates = list(map(int, sub(' +', ' ', all[cratesLines]).split()))[-1]

crates = getCrates(numCrates)
p(f'Part 1:', solveCrates(crates, doPart2=False))
crates = getCrates(numCrates)
p(f'Part 2:', solveCrates(crates, doPart2=True))
