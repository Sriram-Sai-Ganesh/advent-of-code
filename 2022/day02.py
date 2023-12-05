# https://adventofcode.com/2022/day/2

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]

p=print

total1=0
total2=0

# index into these to check score:
# rock=A=X=1, paper=B=Y=2, scissors=C=Z=3
opponent=['A','B','C']
mine=['X','Y','Z']

# get points based on move
def points(move):
    if move in opponent:
        return opponent.index(move)+1
    else:
        return mine.index(move)+1

# iterate over rounds
for row in lines():
    # Part 1:
    first,second=row.split()
    total1+=points(second)
    firstIndex=opponent.index(first)
    secondIndex=mine.index(second)
    # win, lose or draw based on the indices of each move
    total1+=6 if secondIndex==(firstIndex+1)%3 else 3 if secondIndex==firstIndex else 0

    # Part 2:
    # 0 1 or 2 for lose, win, draw
    move=points(second) - 1
    # add outcome score by default
    total2+=move*3
    # add move score
    total2+=(points(first)+move-2)%3 + 1

print('Part 1:',total1)
print('Part 2:',total2)