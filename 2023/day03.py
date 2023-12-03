# https://adventofcode.com/2023/day/3

TEST=0
file='input/'+('test.txt' if TEST else 'in.txt')

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]

# Solution (both parts):

# if number neighbors a symbol, return 'True'
# also, handle the case if neighbor is a gear
def checkNeighborsForSymbols(rows, i, j, number):
    hasSymbol=False
    if (i,j) in symbols:
        hasSymbol=True
        if rows[i][j]=='*':
            gears[(i,j)].append(number)
    return hasSymbol


# iterate from start to end index of number and read value.
# afterwards, process neighbors for symbols and count appropriately.
def getnum(rows,i, j, nums):
    digits=[]
    x=j
    while x<len(rows[i]) and rows[i][x].isnumeric():
        digits.append(rows[i][x])
        x+=1
    number = int(''.join(digits))

    # check if possible due to any neighbor:
    mustCount=False
    # check leftmost 3 spaces
    mustCount|=checkNeighborsForSymbols(rows, i-1, j-1, number)
    mustCount|=checkNeighborsForSymbols(rows, i, j-1, number)
    mustCount|=checkNeighborsForSymbols(rows, i+1, j-1, number)

    # check all spaces above and below number
    x=0
    while x<len(str(number)):
        mustCount|=checkNeighborsForSymbols(rows, i-1, j+x, number)
        mustCount|=checkNeighborsForSymbols(rows, i+1, j+x, number)
        x+=1
    # check all spaces to the right of number
    mustCount|=checkNeighborsForSymbols(rows, i-1, j+x, number)
    mustCount|=checkNeighborsForSymbols(rows, i, j+x, number)
    mustCount|=checkNeighborsForSymbols(rows, i+1, j+x, number)

    # count each number exactly once.
    if mustCount:
        nums.append(number)
    return number

rows = lines()
nums=[]
tot1=0
tot2=0
i=0

symbols=set()      # track symbol locations for part 1
gears=dict()        # track {gear location: list of nums} for part 2

# first, store all symbol/gear locations in hashsets.
while i<len(rows):
    j=0
    while j<len(rows[i]):
        if not rows[i][j].isnumeric() and rows[i][j]!='.':
            if rows[i][j]=='*':
                gears[(i,j)]=[]
            symbols.add((i,j))
        j+=1
    i+=1


# next, iterate over the rows and read integers.
# check each number's neighbors to see if a symbol or gear is found
i=0
while i<len(rows):
    j=0
    while j<len(rows[i]):
        if rows[i][j].isnumeric():
            result = getnum(rows, i, j, nums)
            j+=len(str(result))-1
        j+=1
    i+=1

# tot1 is the sum of ALL numbers that neighbor 1 or more symbols
tot1=sum(nums)

# tot2 is the sum of cardinality of gears
# product of numbers when a single gear neighbors exactly 2 numbers
for i,j in gears.items():
    tot2+=j[0]*j[1] if len(j)==2 else 0

print(f'Part 1: {tot1}')
print(f'Part 2: {tot2}')
