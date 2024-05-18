result: list = []
start: list = [['0' for i in range(5)] for j in range(5)]

for i in range(5):
    row = input()
    result.append([i for i in row])
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
    print(_row, _col)
    if start[_row][_col] != result[_row][_col]:
        if (_row, _col) in possibles.keys():
            pos = possibles[_row][_col]
        else:
            pos = ['R', 'C']
        if _col + 1 >= 5:
            _col = 0
            _row += 1
        else:
            _col += 1
        for p in pos:
            total += 1
            if p == 'C':
                new = iterate(_row, _col, change(_start, _col, p))
            else:
                new = iterate(_row, _col, change(_start, _row, p))
            total += new
            if total < best:
                best = total
    return best

print(iterate(0, 0 , start))
