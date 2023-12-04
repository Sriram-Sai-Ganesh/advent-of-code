# https://adventofcode.com/2023/day/4

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

import re

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]

p=print

# Part 1: track points earned
totalPoints=0
rows = lines()

# Part 2: store cards for later
cards=[]

for line in rows:
    # process digit parsing from line
    line=re.sub(' +',' ',line).split(': ')
    cardnum=int(line[0].split(' ')[1])
    parts=line[1].split(' | ')

    # calculate number of matching #s
    winSet=set(list(map(int, parts[0].split(' '))))
    hand=set(list(map(int, parts[1].split(' '))))

    # part 1: add to running point total
    matches=len(winSet.intersection(hand))
    totalPoints+=int(2**(matches - 1))

    # part 2: store number of matches
    cards.append([cardnum, 1, matches])


totalCards=0
i=0
# process each card, updating copies as we go
while i<len(cards):
    cardnum, copies, matches=cards[i]
    # increment score -- 
    # the number of copies of the current card won't change.
    totalCards+=copies
    # add copies for all 'matches' cards below this one:
    for j in range(matches):
        cards[i+j+1][1]+=copies    
    i+=1

# print results
p(f'Part 1: {totalPoints}')
p(f'Part 2: {totalCards}')
