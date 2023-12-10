# https://adventofcode.com/2022/day/6

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip('\n') for x in f.readlines()]

p=print

all = lines()
line=all[0]

def solve(line, doPart2=False):
    # only difference between parts 1 and 2 is # of chars to look ahead
    num=4 if not doPart2 else 14
    for i in range(len(line)):
        # size of (set of chars) should be 4 (or 14 for part 2)
        if len(set(line[i:i+num]))==num:
            return i+num

p('Part 1:',solve(line, False))
p('Part 2:',solve(line, True))