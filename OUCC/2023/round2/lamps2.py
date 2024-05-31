result: list = []

for i in range(5):
    row = input()
    result.append([i for i in row])

_len = len(result)


# find start node and initialize nodeAndDirection
def compare_and_assign_to_dict(_row, _col, _dir):
    if cur_board[_row][_col] != result[_row][_col]:
        nodeAndDirection[(_row, _col)] = _dir if _dir == 'R' else 'C'


start_node = (0, 0)
best = float('inf')

for _row in range(_len):
    for _col in range(_len):
        if result[_row][_col] == '1':
            cur_col = _col + 1
            for cur_col in range(cur_col, _len):
                compare_and_assign_to_dict(_row, cur_col, 'R')
            cur_row = _row + 1
            for cur_row in range(cur_row, _len):
                compare_and_assign_to_dict(cur_row, _col, 'C')
            break

cur_row = start_node[0]
for _dir in ['R', 'C']:
    total = 0
    cur_board: list = [['0' for i in range(_len)] for j in range(_len)]
    nodeAndDirection: dict = {(0, 0): _dir}

    for _row in range(start_node[0], _len):
        for _col in range(start_node[1], _len):

            if cur_board[_row][_col] != result[_row][_col]:
                total += 1

                direction = nodeAndDirection[(_row, _col)]

                for i in range(_len):
                    if direction == 'R':
                        cur_board[_row][i] = '1' if cur_board[_row][i] == '0' else '0'
                    else:
                        cur_board[i][_col] = '1' if cur_board[i][_col] == '0' else '0'

            for j in range(1, _len):
                compare_and_assign_to_dict(_row, j, 'C')
            for j in range(1, _len):
                compare_and_assign_to_dict(j, _col, 'R')

    if total < best:
        best = total

print(best)
