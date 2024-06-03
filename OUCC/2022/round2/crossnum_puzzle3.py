area = input().split(' ')
row_len = int(area[0])
col_len = int(area[1])
crossword = []

for i in range(row_len):
    new_line = input()
    crossword_line = []
    for j in new_line:
        crossword_line.append(j)
    crossword.append(crossword_line)


def find_number(_row, _col, _direction):
    number = ''
    if _direction == 'right':
        if _col >= col_len:
            return ''
        if crossword[_row][_col] == 'X':
            return ''
        number += crossword[_row][_col]
        _col += 1
        new = find_number(_row, _col, 'right')
        if new == '':
            return number
        number += new
    else:
        if _row >= row_len:
            return ''
        if crossword[_row][_col] == 'X':
            return ''
        number += crossword[_row][_col]
        _row += 1
        new = find_number(_row, _col, 'down')
        if new == '':
            return number
        number += new
    return number


best = 0
col = 0
# There is some sort of error in here
for row in range(row_len):
    while col < col_len:
        node = crossword[row][col]
        if node == 'X':
            pass
        else:
            new_number = int(find_number(row, col, 'right'))
            if new_number > best:
                best = new_number

            new_number = int(find_number(row, col, 'down'))
            if new_number > best:
                best = new_number

        col += 1
    col = 0

print(best)