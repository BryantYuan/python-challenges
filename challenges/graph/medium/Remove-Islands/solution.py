def removeIslands(matrix):
    to_delete = [[True for j in range(len(matrix[0]))] for i in range(len(matrix))]

    runHorizontal(matrix, 0, to_delete)
    runHorizontal(matrix, len(matrix) - 1, to_delete)
    runVertical(matrix, 0, to_delete)
    runVertical(matrix, len(matrix[0]) - 1, to_delete)

    for row in range(1, len(matrix) - 1):  # I have already run the entire outside, this is for the inside.
        for col in range(1, len(matrix[0]) - 1):
            node = matrix[row][col]
            if node == 0:
                to_delete[row][col] = False

            if matrix[row][col] == 1 and to_delete[row][col] == True:
                matrix[row][col] = 0

    return matrix


def runHorizontal(matrix, row, to_delete):
    for col, val in enumerate(matrix[row]):
        to_delete[row][col] = False

        if val == 1:
            notAnIsland(matrix, row, col, to_delete)


def runVertical(matrix, col, to_delete):
    row = 0
    while row < len(matrix):
        val = matrix[row][col]
        to_delete[row][col] = False

        if val == 1:
            notAnIsland(matrix, row, col, to_delete)

        row += 1


def notAnIsland(matrix, row, col, to_delete):
    to_delete[row][col] = False
    four_dir = [[row + 1, col], [row - 1, col], [row, col - 1], [row, col + 1]]

    if matrix[row][col] == 0:
        return

    for direction in four_dir:
        cur_row = direction[0]
        cur_col = direction[1]

        if len(matrix) <= cur_row or cur_row < 0 or cur_col < 0 or cur_col >= len(matrix[0]):
            continue

        if to_delete[cur_row][cur_col]:
            notAnIsland(matrix, cur_row, cur_col, to_delete)

    return