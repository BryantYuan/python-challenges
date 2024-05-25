result: list = []

for i in range(5):
    row = input()
    result.append([i for i in row])




def opposite(direction):
    if direction == 'R':
        return 'C'
    else:
        return 'R'


def change(grid: list, _row: int, _col: int) -> list:
    if grid[_row][_col] == '0':
        grid[_row][_col] = '1'
    else:
        grid[_row][_col] = '0'
    return grid


best = float('inf')
for _ in ['R', 'C']:
    possibles: dict = {}
    total = 0
    possibles[(0,0)] = _
    start: list = [['0' for i in range(5)] for j in range(5)]

    for _row in range(5):

        for _col in range(5):

            if start[_row][_col] != result[_row][_col]:
                total += 1

                if (_row, _col) in possibles:
                    pos = possibles[(_row, _col)][0]

                    for i in range(5):
                        if (_row, i) not in possibles:
                            possibles[(_row, i)] = [opposite(pos)]

                    for i in range(5):
                        if (i, _col) not in possibles:
                            possibles[(i, _col)] = [pos]
                else:
                    pos = ['R', 'C']

                for i in range(5):

                    if pos == 'R':
                        change(start, _row, i)
                    else:
                        change(start, i, _col)
    if total < best:
        best = total

print(best)
