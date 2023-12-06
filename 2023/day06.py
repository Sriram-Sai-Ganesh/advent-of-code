# https://adventofcode.com/2023/day/6

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

from re import *

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]

p=print

all = lines()
total1=1

# simulate runs to check # of ways
def ways(t,d):
    w=0
    for i in range(t):
        if i*(t-i)>d:
            w+=1
    return w

# Part 1: times read independently
times=map(int,sub('\D+',' ',all[0]).strip().split())
dists=map(int,sub('\D+',' ',all[1]).strip().split())

# run sim for Part 1
for t, d in zip(times, dists):
    total1*=ways(t,d)

# Part 2: concat all digits
time2=int(sub('\D','',all[0]))
dist2=int(sub('\D','',all[1]))

# print results
p('Part 1:',total1)
p('Part 2:',ways(time2, dist2))