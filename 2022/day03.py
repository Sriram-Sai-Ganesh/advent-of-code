# https://adventofcode.com/2022/day/3

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]

p=print

total1=0
total2=0

all=lines()

# helper
def getScore(letter):
    if letter.isupper():
        return ord(letter)-ord('A')+27
    return ord(letter)-ord('a')+1

# generous use of set.intersection(set)

# Part 1:
for row in all:
    # get sublists
    a,b=list(map(set, [row[:len(row)//2], row[len(row)//2:]]))
    # get common letter and score
    letter=a.intersection(b).pop()
    score=getScore(letter)
    # add to total1
    total1+=score

i=0
# Part 2:
while i<len(all):
    # intersection of sets of 3 lines
    shared=set(all[i]).intersection(set(all[i+1])).intersection(set(all[i+2])).pop()
    # add to total2 and increment counter
    score=getScore(shared)
    total2+=score
    i+=3

print('Part 1:',total1)
print('Part 2:',total2)