def minimumPassesOfMatrix(matrix: list, status=None) -> int:
    """
    This will calculate the number of rounds to change every single number in the matrix to positive.
    Exempts 0

    :param matrix: The matrix we are going to go through
    :param status: False means the matrix[row, col] is negative, True is positive and None is zero.
    :return: How many rounds to turn the status all to True or None
    """
    col: int = len(matrix[0])
    row: int = len(matrix)

    if status is None:
        status = [[False for i in range(col)] for j in range(row)]  # Assume all is negative
        for r in range(row):
            for c in range(col):
                node: int = matrix[r][c]

                if node > 0:
                    status[r][c] = True
                    continue

                if node == 0:
                    status[r][c] = None
                    continue

    total = 0
    while checkNegative(status):
        total += 1
        for r in range(row):
            for c in range(col):
                node: int = matrix[r][c]

                if node > 0:
                    status[r][c] = True
                    continue

                if node < 0:
                    result = checkForPositive(status, row, col, c, r)
                    if result:
                        matrix[r][c] *= -1
    return total


def checkNegative(status):
    for row in status:
        for i in row:
            if i is False and i is not None:
                return True
    return False


def checkForPositive(status: list, row: int, col: int, cur_col: int, cur_row: int) -> bool:
    """
    Checks if there are any positive numbers around the cur node
    :param cur_row: The current row we are on
    :param cur_col: The current col we are on
    :param status: A 2d array telling us about the numbers
    :param row: How many rows in the matrix.
    :param col: How many columns in the matrix.
    :return: True or False
    """

    four_dir = [[cur_row, cur_col + 1], [cur_row, cur_col - 1], [cur_row - 1, cur_col],
                [cur_row + 1, cur_col]]

    for direction in four_dir:
        new_r: int = direction[0]
        new_c: int = direction[1]

        if 0 < new_r >= row or 0 < new_c >= col:
            continue

        t_or_f = status[new_r][new_c]
        if t_or_f:
            return True

    return False