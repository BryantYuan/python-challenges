area = input().split(' ')
col_len = int(area[0])
row_len = int(area[1])
crossword = []

for i in range(row_len):
    new_line = input()
    crossword_line = []
    for j in new_line:
        crossword_line.append(j)
    crossword.append(crossword_line)

max_cols: dict = {}


def find_numbers_horizontal(_row, _col):
    number = ''
    while _col < col_len:
        if crossword[_row][_col] == 'X':
            break
        number += crossword[_row][_col]
        _col += 1
    return number


def find_numbers_vertical(_row, _col):
    number = ''
    while _row < row_len:
        if crossword[_row][_col] == 'X':
            break
        number += crossword[_row][_col]
        _row += 1
    max_cols[_col] = _row
    return number


best = 0
# There is some sort of error in here
for row in range(row_len):
    col = 0
    while col < col_len:
        if crossword[row][col] == 'X':
            col += 1
            continue

        horizontal_number = int(find_numbers_horizontal(row, col))
        vertical_number = 0
        if row > max_cols[col]:
            vertical_number = int(find_numbers_vertical(row, col))

        best = max(best, horizontal_number, vertical_number)

print(best)
