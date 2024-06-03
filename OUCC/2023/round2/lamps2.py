result: list = []

for i in range(5):
    row = input()
    result.append([i for i in row])

_len = len(result)


# find start node and initialize nodeAndDirection
def do_compare_and_assign_to_dict(_board, _row, _col, _dir):
    if _board[_row][_col] != result[_row][_col]:
        nodeAndDirection[(_row, _col)] = _dir if _dir == 'R' else 'C'


best = float('inf')


def find_start_node() -> tuple:
    for _r in range(_len):
        for _c in range(_len):
            if result[_r][_c] == '1':
                return _r, _c


def compare_and_assign_to_dict(_board, _row, _col):
    for cur_col in range(_col, _len):
        do_compare_and_assign_to_dict(cur_board, start_node[0], cur_col, 'C')
    for cur_row in range(_row, _len):
        do_compare_and_assign_to_dict(cur_board, cur_row, start_node[1], 'R')


start_node = find_start_node()

for _dir in ['R', 'C']:
    total = 0
    cur_board: list = [['0' for i in range(_len)] for j in range(_len)]
    nodeAndDirection: dict = {start_node: _dir}

    compare_and_assign_to_dict(cur_board, start_node[0], start_node[1])

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

            compare_and_assign_to_dict(cur_board, _row, _col)

    if total < best:
        best = total

print(best)
