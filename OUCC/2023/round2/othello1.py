board = []
for i in range(8):
    line = []
    for s in input():
        line.append(s)
    board.append(line)

cur_position = input().split(',')
row = 8 - int(cur_position[1])
col = int(cur_position[0]) - 1

if board[row][col] == '0':
    print('empty')
elif board[row][col] == 'w':
    print('white')
elif board[row][col] == 'b':
    print('black')
