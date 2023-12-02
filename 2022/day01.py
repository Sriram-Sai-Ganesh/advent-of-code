# https://adventofcode.com/2022/day/1

# all lines from file
def lines():
    with open(file) as f:
        return [x.strip() for x in f.readlines()]
# empty-line-separated groups of lines
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

# empty-line-separated groups of integers
def groups_of_ints():
    return [list(map(int, row)) for row in groups_of_lines()]


TEST=0

file='input/'+('test.txt' if TEST else 'in.txt')

p=print

groups = groups_of_ints()
# Part 1: largest element in a list of (sums of groups of integers)
p('Part 1:', max(list(map(sum, groups))))
# Part 2: sum of largest 3 elements in a list of (sums of groups of integers)
# we get the sum by using last 3 elemenst in the sorted list of sums
p('Part 2:', sum(sorted(list(map(sum, groups)))[-3::1]))