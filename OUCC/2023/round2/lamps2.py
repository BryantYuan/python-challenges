result: list = []

for i in range(5):
    row = input()
    result.append([i for i in row])

_len = len(result)

# find start node and initialize nodeAndDirection
def compare_and_assign_to_dict(_row, _col, _dir):
    if cur_board[_row][_col] != result[_row][_col]:
        nodeAndDirection[(_row, _col)] = _dir if _dir == 'R' else 'C'


def change(grid: list, _row: int, _col: int) -> list:
    if grid[_row][_col] == '0':
        grid[_row][_col] = '1'
    else:
        grid[_row][_col] = '0'
    return grid




# print(nodeAndDirection)
start_node = (0, 0)
best = float('inf')

cur_row = start_node[0]
for _dir in ['R', 'C']:
    total = 0
    cur_board: list = [['0' for i in range(_len)] for j in range(_len)]
    nodeAndDirection: dict = {(0,0): _dir}

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

    for _row in range(start_node[0], _len):
        for _col in range(start_node[1], _len):

            if cur_board[_row][_col] != result[_row][_col]:
                total += 1


                if (_row, _col) in nodeAndDirection:
                    direction = nodeAndDirection[(_row, _col)]

                for i in range(5):

                    if direction == 'R':
                        change(cur_board, _row, i)
                    else:
                        change(cur_board, i, _col)

            for j in range(1, 5):
                compare_and_assign_to_dict(_row, j, 'C')
            for j in range(1, 5):
                compare_and_assign_to_dict(j, _col, 'R')

    if total < best:
        best = total

print(best)
