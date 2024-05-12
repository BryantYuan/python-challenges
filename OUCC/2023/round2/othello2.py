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

cur_position = input().split(',')
row = 8 - int(cur_position[1])
col = int(cur_position[0]) - 1
valid = False

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


def do_check(_row, _col, cur_dir) -> (bool, int):
    if (_row >= 8 or _col >= 8 or _row < 0 or _col < 0) or board[_row][_col] == '0':
        return False, 0

    if board[_row][_col] == colour:
        return True, 0

    captured = 0

    if board[_row][_col] == target:
        captured = 1

    next_row, next_col = directions[cur_dir](_row, _col)

    _result = do_check(next_row, next_col, cur_dir)
    if _result[0]:
        return True, captured + _result[1]

    return _result


for d in directions:
    _row, _col = directions[d](row, col)
    result = do_check(_row, _col, d)
    if result[0]:
        print('valid')
        valid = True
        break

if not valid:
    print('invalid')
