board = []
for i in range(8):
    line = []
    for s in input():
        line.append(s)
    board.append(line)

colour = input()
if colour == 'black':
    target = 'w'
else:
    target = 'b'


def check(r, c, b, t):
    captured = 0
    directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1], [r + 1, c + 1], [r + 1, c - 1], [r - 1, c - 1],
                  [r - 1, c + 1], [r - 1, c - 1]]
    for d in directions:
        if 0 > d[0] or d[0] >= 8 or 0 > d[1] or d[1] >= 8:
            continue
        if b[d[0]][d[1]] == t:
            captured += 1

    return captured


best = 0
best_squares = None
for row in range(8):
    for col in range(8):
        square = board[row][col]
        if square == '0':
            new = check(row, col, board, target)
            if new > best:
                best = new
                best_squares = f'{col + 1},{8-row}'
        else:
            continue
print(best_squares)
