# https://adventofcode.com/2023/day/9
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


p=print

# finished if all 0s
def finished(ar):
    for i in ar:
        if i!=0:
            return False
    return True

# handle each row:
def handle(nums):
    ans=0
    # create a pyramid, base layer is 'nums'
    pyramid=[nums]
    # iterate until all 0 differences
    while not finished(nums):
        # store differences, reset each round.
        curr=[]
        for i in range(1,len(nums)):
            curr.append(nums[i]-nums[i-1])
        pyramid.append(curr)
        nums=curr
    # get total suffix
    for i in pyramid:
        ans+=i[-1]
    return ans


all = lines()
total1=0
total2=0

for line in all:
    # part 2 = part 1 with reversed input
    total1+=handle(list(map(int, line.split())))
    total2+=handle(list(map(int, line.split()[::-1])))

p('Part 1:',total1)
p('Part 2:',total2)


