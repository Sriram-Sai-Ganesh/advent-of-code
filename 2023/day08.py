# https://adventofcode.com/2023/day/8

TEST = 0

file = 'input/' + ('test.txt' if TEST else 'in.txt')

from re import *
from math import *
from collections import *
import numpy as np
import itertools


# all lines from file
def lines():
    with open(file) as f:
        return [x.strip('\n') for x in f.readlines()]


# ignore everything except numbers, return a list of nums
def nums(line):
    return list(map(int, sub('\D+', ' ', line).strip().split()))


# empty-line-separated groups of lines
def groups_of_lines():
    result = []
    i = 0
    li = lines()
    while i < len(li):
        group = []
        while i < len(li) and li[i] != '':
            group.append(li[i])
            i += 1
        result.append(group)
        i += 1
    return result


# empty-line-separated groups of integers
def groups_of_ints():
    return [list(map(int, row)) for row in groups_of_lines()]


# list of 1 int on each line
def ints():
    return list(map(int, lines()))


# 2D list of strings or characters, separated by @param separ.
def line_grid(separ=''):
    return [x.split(separ) for x in lines()]


# 2D list of ints, separated by @param separ.
def int_grid(separ=''):
    return [list(map(int, row)) for row in line_grid(separ)]


'''
lines(): 
    all lines from file
nums(line):
    ignore everything except numbers, return a list of nums
groups_of_lines():
    empty-line-separated groups of lines
string_grid(separ=''):
    2D list of strings or characters, separated by @param separ.
groups_of_ints():
    empty-line-separated groups of integers
ints():
    list of 1 int on each line
int_grid(separ=''):
    2D list of ints, separated by @param separ.
'''

p = print

all = lines()


def solve(doPart2=False):
    # create adjacency dict
    adj = {}
    allPaths = []

    instructions = all[0]
    for line in all[2:]:
        lhs, rhs = line.split(' = ')
        left, right = rhs[1:-1:1].split(', ')
        # Part 2: track all starting points
        if lhs[-1] == 'A':
            allPaths.append(lhs)
        adj[lhs] = [left, right]
    # Part 1: the only starting point is 'AAA'
    if not doPart2:
        allPaths = ['AAA']
    # iterate over instructions as long as necessary
    instIndex = 0
    # keep track of num of steps for path terminations:
    stepCounts = []

    totalSteps = 0
    # iterate as long as we have unfinished paths
    while allPaths != []:
        totalSteps += 1
        pathIndex = 0
        # for each unfinished path:
        while pathIndex < len(allPaths):
            # advance 1 step (following instructions)
            allPaths[pathIndex] = adj[allPaths[pathIndex]][instructions[instIndex]=='R']
            # Part 1 & Part 2 have different termination conditions
            if (doPart2 and allPaths[pathIndex][-1] == 'Z') or (not doPart2 and allPaths[pathIndex]=='ZZZ'):
                # if this path ends, remove it from the path list &
                allPaths.pop(pathIndex)
                # add its total steps to the result list
                stepCounts.append(totalSteps)
                pathIndex -= 1
            pathIndex += 1
        # loop over instructions & wrap around
        instIndex += 1
        instIndex = instIndex % len(instructions)

    # calculate final result from the LCM 
    # of all path termination step counts
    stepLCM = 1
    for term in stepCounts:
        stepLCM = lcm(stepLCM, term)
    return stepLCM

print('Part 1:',solve(doPart2=False))
print('Part 2:',solve(doPart2=True))
