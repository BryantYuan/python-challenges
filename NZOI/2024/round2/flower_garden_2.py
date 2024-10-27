input_amount, distance = map(int, input().split(' '))
total_width = distance * 2 + 1
longest_y = -1
longest_x = -1
total = 0
list_of_nodes = []


def fill(_board, _x, _y):
    h_start = _y - distance
    h_end = _y + distance
    w_start = _x - distance
    w_end = _x + distance
    cur = 0

    for height in range(h_start, h_end + 1):
        if height < 0:
            continue

        for width in range(w_start, w_end + 1):
            if width < 0:
                continue

            node = board[height][width]
            if node == '0':
                board[height][width] = '1'
                cur += 1
    return cur


for i in range(input_amount):
    center = input().split(' ')
    x = int(center[0])
    y = int(center[1])
    list_of_nodes.append((x, y))

    if y + distance + 1 > longest_y:
        longest_y = y + distance + 1

    if x + distance + 1 > longest_x:
        longest_x = x + distance + 1

board = [['0' for i in range(longest_x)] for i in range(longest_y)]

for pair in list_of_nodes:
    x, y = pair
    total += fill(board, x, y)

print(total)