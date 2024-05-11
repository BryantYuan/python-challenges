board = []
for i in range(8):
    line = []
    for s in input():
        line.append(s)
    board.append(line)

input_colour = input()
target = 'b'
colour = 'w'

if input_colour == 'black':
    target = 'w'
    colour = 'b'

directions = {
    'north': lambda r, c: (r + 1, c),
    'south': lambda r, c: (r - 1, c),
    'east': lambda r, c: (r, c + 1),
    'west': lambda r, c: (r, c - 1),
    'north_east': lambda r, c: (r + 1, c + 1),
    'north_west': lambda r, c: (r + 1, c - 1),
    'south_west': lambda r, c: (r - 1, c - 1),
    'south_east': lambda r, c: (r - 1, c + 1),
}


def check(_row, _col):
    captured = 0
    for d in directions:
        r, c = directions[d](_row, _col)
        result = do_check(r, c, d)
        if result[0]:
            captured += result[1]

    return captured


def do_check(_row, _col, cur_dir) -> (bool, int):
    if (_row >= 8 or _col >= 8 or _row < 0 or _col < 0) or board[_row][_col] == '0':
        return False, 0

    if board[_row][_col] == colour:
        return True, 0

    captured = 0

    if board[_row][_col] == target:
        captured = 1

    next_row, next_col = directions[cur_dir](_row, _col)

    result = do_check(next_row, next_col, cur_dir)
    if result[0]:
        return True, captured + result[1]

    return result


best = 0
best_squares = None
for row in range(8):
    for col in range(8):
        square = board[row][col]
        if square != '0':
            continue
        new = check(row, col)
        if new > best:
            best = new
            best_squares = f'{col + 1},{8 - row}'

print(best_squares)
