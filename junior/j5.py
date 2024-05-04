import sys


def find(row, col, cur_row, cur_col, harvest):
    if -1 < cur_row < row and -1 < cur_col < col:
        place = harvest[cur_row][cur_col]
        if place == '*':
            return 0
    else:
        return 0
    total = 0
    if place == "L":
        total += 10
    elif place == 'M':
        total += 5
    elif place == 'S':
        total += 1
    harvest[cur_row][cur_col] = '*'
    four_dir = [[cur_row + 1, cur_col], [cur_row - 1, cur_col], [cur_row, cur_col - 1], [cur_row, cur_col + 1]]
    for direction in four_dir:
        total += find(row, col, direction[0], direction[1], harvest)
    return total


sys.setrecursionlimit(1000000)
r = int(input())
c = int(input())
farm = []
for i in range(r):
    lis = []
    line = input()
    for l in line:
        lis.append(l)
    farm.append(lis)
cur_r = int(input())
cur_c = int(input())
print(find(r, c, cur_r, cur_c, farm))
