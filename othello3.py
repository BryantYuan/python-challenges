board = []
for i in range(8):
    line = []
    for s in input():
        line.append(s)
    board.append(line)

colour = input()
if colour == 'black':
    target = 'w'
    colour = 'b'
else:
    target = 'b'
    colour = 'w'


# def valid(r, c, b, t):
#     directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1], [r + 1, c + 1], [r + 1, c - 1], [r - 1, c - 1],
#                   [r - 1, c + 1], [r - 1, c - 1]]
#     for d in directions:
#         if 0 > d[0] or d[0] >= 8 or 0 > d[1] or d[1] >= 8:
#             continue
#         if b[d[0]][d[1]] == t:
#             continue
#         else:
#             return False
#     return True


def check(r, c, b, t, cur_colour):
    captured = 0
    directions = ['north', 'south', 'east', 'west', 'north_east', 'north_west', 'south_west', 'south_east']
    for d in directions:
        result = capture(r, c, b, t, cur_colour, d)
        if result:
            captured += result

    return captured


def capture(r, c, b, t, cur_colour, cur_dir):
    """

    :param r: row
    :param c: col
    :param b: board
    :param t: target
    :param cur_colour: current colour the player is
    :param cur_dir: the direction that the player is going
    :return: how many captured moves
    """
    captured = 0
    if b[r][c] == cur_colour:
        return True
    elif b[r][c] == t:
        captured += 1

    if cur_dir == 'north':
        r += 1
    elif cur_dir == 'south':
        r -= 1
    elif cur_dir == 'east':
        c += 1
    elif cur_dir == 'west':
        c -= 1
    elif cur_dir == 'north_east':
        c += 1
        r += 1
    elif cur_dir == 'north_west':
        r += 1
        c -= 1
    elif cur_dir == 'south_west':
        r -= 1
        c -= 1
    elif cur_dir == 'south_east':
        r -= 1
        c += 1

    if r >= 8 or c >= 8 or r < 0 or c < 0:
        return False
    if b[r][c] == '0':
        return False

    result = capture(r, c, b, t, cur_colour, cur_dir)
    if result:
        return captured + result
    else:
        return False


best = 0
best_squares = None
for row in range(8):
    for col in range(8):
        square = board[row][col]
        if square == '0':
            new = check(row, col, board, target, colour)
            if new > best:
                best = new
                best_squares = f'{col + 1},{8 - row}'
        else:
            continue
print(best_squares)
