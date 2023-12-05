# https://adventofcode.com/2022/day/4

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

from re import *

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]
p=print

all=lines()

total1=0
total2=0
for row in all:
    # get nums
    s1,e1,s2,e2=map(int,split(',|\\-',row))
    # Part 1: check if fully contained
    total1+=1 if (s1<=s2 and e1>=e2) or (s2<=s1 and e2>=e1) else 0
    # Part 2: any overlap occurs if they are NOT disjoint
    total2+=1 if not(e1<s2 or e2<s1) else 0

p('Part 1:', total1)
p('Part 2:', total2)










