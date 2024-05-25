result: list = []

for i in range(5):
    row = input()
    result.append([i for i in row])

_len = len(result)

cur_board: list = [['0' for i in range(_len)] for j in range(_len)]

start_node = None
nodeAndDirection: dict = {}


# find start node and initialize nodeAndDirection
def compare_and_assign_to_dict(_row, _col, _dir):
    if cur_board[_row][_col] != result[_row][_col]:
        nodeAndDirection[(_row, _col)] = _dir if _dir == 'R' else 'C'


for _row in range(_len):
    for _col in range(_len):
        if result[_row][_col] == '1':
            start_node = (_row, _col)
            cur_col = _col + 1
            for cur_col in range(_len):
                compare_and_assign_to_dict(_row, cur_col, 'R')
            cur_row = _row + 1
            for cur_row in range(_len):
                compare_and_assign_to_dict(cur_row, _col, 'C')
            break

cur_row = start_node[0]

for _row in range(start_node[0], _len):
    for _col in range(start_node[1] + 1, _len)):

