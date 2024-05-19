result: list = []
start: list = [['0' for i in range(5)] for j in range(5)]

for i in range(5):
    row = input()
    result.append([i for i in row])

possibles: dict = {}


def change(grid: list, _row: int, _col: int) -> list:
    if grid[_row][_col] == '0':
        grid[_row][_col] = '1'
    else:
        grid[_row][_col] = '0'
    return grid


total = 0
for _row in range(5):
    for _col in range(5):
        # print(_row, _col)

        if start[_row][_col] != result[_row][_col]:
            # print('OK?')
            total += 1

            if (_row, _col) in possibles:
                pos = possibles[(_row, _col)]
            else:
                pos = ['C']
                for i in range(5):
                    possibles[(_row, i)] = ['C']
                for i in range(5):
                    possibles[(i, _col)] = ['R']

            for p in pos:
                for i in range(5):

                    if p == 'R':
                        change(start, _row, i)
                    else:
                        change(start, i, _col)

        if _col + 1 >= 5:
            _col = 0
            _row += 1
        else:
            _col += 1

print(total)
