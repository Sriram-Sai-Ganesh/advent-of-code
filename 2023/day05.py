# https://adventofcode.com/2023/day/5

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

from re import *

# read all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]
    
# read empty-line-separated groups of lines
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
# get input
rows = groups_of_lines()

# store seeds as range objects (memory efficient)
seedRangesPart1 = []
parse=list(map(int, rows[0][0].split(': ')[1].split()))

seedRangesPart2 = []
totalSeeds2=0
i=0
while i<len(parse):
    seedRangesPart1.append(range(parse[i], parse[i]+1))
    seedRangesPart2.append(range(parse[i], parse[i]+parse[i+1]))
    i+=2
    totalSeeds2+=len(seedRangesPart2[-1])

# find end location of every possible seed
# track minimum as we go
minloc=10**15

# create and store resource bounds as 'groups' of bounds
groups=[]
for i,group in enumerate(rows[1:]):
    current=[]
    name=group[0].split()[0].split('-')[2]
    for row in group[1:]:
        next, prev, end = map(int,row.split())
        current.append([[prev, prev+end],[next, next+end]])
    current.sort(key=lambda x:x[0][0])
    groups.append(current)

def getMinLocation(currentSeedRanges):
    minloc = 10**15
    # helper function to get the location 
    # that a particular seed maps to
    def getloc(seed):
        for g in groups:
            for mapping in g:
                preimage, image=mapping
                if seed>=preimage[0] and seed<preimage[1]:
                    seed=image[0]+seed-preimage[0]
                    break
        return seed

    count=0 # track progress
    # run sim for all possible seeds:
    for singleRange in currentSeedRanges:
        for seed in singleRange:
            # periodically print progress
            count+=1
            if count%100_000==0:
                print(f'{count/totalSeeds2 * 100}\t%')
            # keep track of minimum possible location
            minloc=min(minloc, getloc(seed))
    return minloc

# takes around 80 minutes to run:
ans2='<PLACEHOLDER>'
# ans2=getMinLocation(seedRangesPart2)

# takes around 0.1 seconds to run:
p(f'Part 1: {getMinLocation(seedRangesPart1)}')

p(f'Part 2: {ans2}')