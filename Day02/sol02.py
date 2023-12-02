# https://adventofcode.com/2023/day/2
import pathlib

def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]

TEST = 0

file = "/input/in.txt"
if TEST:
    file = "/input/test.txt"
file = str(pathlib.Path(__file__).parent.resolve()) + file

rows = lines()
total1 = total2 = 0
colorLimits = [12, 13, 14]

for line in rows:
    # get component parts of each line
    id = int(line.split(":")[0].split()[1])
    rounds = line.split(": ")[1]
    # keep a 'possible' flag for part 1
    possible = True
    # keep track of total counts of r,g,b for part 2
    counts = [0, 0, 0]
    # handle each subset:
    for subset in rounds.split(";"):
        check = [0, 0, 0]
        colorCounts = subset.strip().split(",")
        # handle each `<count> <color>` occurence
        for count, color in map(lambda x:x.split(), colorCounts):
            count = int(count)
            colorIndex = ['r','g','b'].index(color[0])
            counts[colorIndex] = max(count, counts[colorIndex])
            check[colorIndex]+=count
        # Part 1: check that every color condition is met
        for ch, col in zip(check, colorLimits):
            possible &= ch<=col
    # if so, this ID is a possible bag
    if possible:
        total1 += id
    # Part 2: add the cardinality of this bag to the total
    total2 += counts[0] * counts[1] * counts[2]

print(f"Part 1:", total1)
print(f"Part 2:", total2)
