result: list = []
start: list = [['0' for i in range(5)] for j in range(5)]

for i in range(5):
    row = input()
    result.append([i for i in row])

possibles: dict = {}


def change(grid: list, _row: int, _col: int) -> list:
    if grid[_row][_col] == 0:
        grid[_row][_col] = 1
    else:
        grid[_row][_col] = 0
    return grid


def change_dict(dictionary: dict, _row: int, _col: int, _pos) -> dict:
    dictionary[(_row, _col)] = _pos
    return dictionary


def next_index(_row: int, _col: int) -> (int, int):
    if _col + 1 >= 5:
        _col = 0
        _row += 1
    else:
        _col += 1
    return _row, _col


def iterate(_row: int, _col: int, start: list) -> int:
    best = float('inf')
    total = 0
    print(_row, _col)

    if _row == 4 and _col == 4:
        return 0

    if start[_row][_col] != result[_row][_col]:

        if (_row, _col) in possibles:
            pos = possibles[(_row, _col)]
        else:
            pos = ['R', 'C']
            for i in range(5):
                change_dict(possibles, _row, i, ['C'])
            for i in range(5):
                change_dict(possibles, i, _row, ['R'])

        index = next_index(_row, _col)
        _row = index[0]
        _col = index[1]
        total += 1

        for p in pos:
            for i in range(5):

                if p == 'R':
                    start = change(start, _row, i)
                else:
                    start = change(start, i, _col)

            new = iterate(_row, _col, start)
            total += new
            if total < best:
                best = total

    return best


print(iterate(0, 0, start))
