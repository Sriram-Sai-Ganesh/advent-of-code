# https://adventofcode.com/2023/day/1

import pathlib
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]
file = str(pathlib.Path(__file__).parent.resolve()) + "/input/in.txt"

# Part 1:
import re
allLines = lines()
total = 0

for s    in allLines:
    s = re.sub("[a-z]", "", s.lower())
    total += int(s[0] + s[-1])
print(f"Part 1: {total}")


# Part 2
total = 0
mapping = [("one", 1),("two", 2),("three", 3),("four", 4),("five", 5),("six", 6),("seven", 7),("eight", 8),("nine", 9)]
mapping.extend([(str(i), i) for i in range(1, 10)])

for s in allLines:
    s = s.lower()
    # check every possible prefix string
    # until we find a number
    digit1 = None
    i = 0  # index of end of prefix, increasing.
    while not digit1:
        currentSlice = s[i:]
        for strNumber, numValue in mapping:
            if strNumber == currentSlice[: min(len(currentSlice),len(strNumber))]:
                digit1 = numValue
                break
        i += 1

    # check every possible suffix string
    # (of a given candidate number's length) in reverse order.
    digit2 = None
    i = 1
    while not digit2:
        for strNumber, numValue in mapping:
            currentSlice = s[-i::1]
            if strNumber == currentSlice[: min(len(strNumber), len(currentSlice))]:
                digit2 = numValue
                break
        i += 1
    total += int(digit1 * 10 + digit2)
print(f"Part 2: {total}")
