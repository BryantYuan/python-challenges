result: list = []
start: list = [['0' for i in range(5)] for j in range(5)]

for i in range(5):
    row = input().split(' ')
    result.append(row)
possibles: dict = {}

def change(grid: list, _pos: int, direction: str) -> list:
    if direction == 'R':
        for index in range(5):
            if grid[_pos][index] == 0:
                grid[_pos][index] = 1
            else:
                grid[_pos][index] = 0
    else:
        for index in range(5):
            g = grid[index][_pos]
            if g == 1:
                grid[index][_pos] = 0
            else:
                grid[index][_pos] = 1
    return grid


def iterate(_row: int, _col: int, _start: list) -> int :
    best = float('inf')
    total = 0
    if _row == 4 and _col == 4:
        return 0
    if start[_row][_col] != result[_row][_col]:
        if (_row, _col) in possibles.keys():
            pos = possibles[_row][_col]
        else:
            pos = ['R', 'C']

        for p in pos:
            if _row + 1 == 5:
                _col += 1
                _row = 0
            else:
                _row += 1
            total += 1
            new = iterate(_row, _col, change(_start, _row, p))
            total += new
            if total < best:
                best = total
    return best

print(iterate(0, 0 , start))
