lamps = []
for i in range(5):
    row = input().split(' ')
    lamps.append(row)


def change(grid, pos, area):
    if area == 'C':
        for index in range(len(grid)):
            if grid[pos][index] == 0:
                grid[pos][index] = 1
            else:
                grid[pos][index] = 0
    else:
        for index in range(grid[pos]):
            g = grid[index]
            if g == 1:
                grid[index] = 0
            else:
                grid[index] = 1


for line in lamps:
    for light in line:
        pass
