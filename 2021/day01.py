# https://adventofcode.com/2023/day/5

TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip('\n') for x in f.readlines()]

# list of 1 int on each line
def ints():
    return list(map(int, lines()))

# get # of times that the list increases
def getinc(nums):
    # indicator list for increase
    indicator = [1 if nums[i+1]>nums[i] else 0 for i in range(len(nums)-1)]

    return sum(indicator)

all = ints()
# calculate windows
window = [all[i]+all[i+1]+all[i+2] for i in range(len(all)-2)]
# ans
print('Part 1:', getinc(all))
print('Part 2:', getinc(window))

