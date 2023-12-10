# https://adventofcode.com/2022/day/6

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

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
    return list(map(int,sub('\D+',' ',line).strip().split()))


# empty-line-separated groups of lines
def groups_of_lines():
    result=[]
    i=0
    li=lines()
    while i<len(li):
        group=[]
        while i<len(li) and li[i]!='':
            group.append(li[i])
            i+=1
        result.append(group)
        i+=1
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


"""
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
"""

p=print

all = lines()



