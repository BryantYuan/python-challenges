"""
2024 CAT Coding free trial

Row Delete, CAT 2024 intermediate
A little analysis of the algorithm will help
"""

import os

from test_data import test_data

MAX_ROWS = 100


def row_delete(deletions):
    """
    Implement solution to Row Delete here

    Inputs:
        deletions: list of integers representing the rows deleted in order

    Returns:
        cost of cheapest sequence with the same effect as the given row sequence
    """

    min_cost = 0  # replace with result

    # TODO: your code goes here
    cur_list_len = 0
    after_delete_list = []

    # To find end result
    for index in deletions:
        if cur_list_len == 0:
            original_list = [i for i in range(1, index + 1)]
            after_delete_list = [i for i in range(1, index + 1)]
            cur_list_len = index

        if index > cur_list_len:
            original_list = [i for i in range(1, index + 1 + cur_list_len)]
            cur_list_len = index + index

            # Editing the list
            length = len(after_delete_list)
            start = after_delete_list[-1] + 1
            end = start + cur_list_len - length
            after_delete_list.extend([i for i in range(start, end)])

        # Deleting the values and replacing them.
        after_delete_list.append(after_delete_list[-1] + 1)
        original_list.append(original_list[-1] + 1)
        del after_delete_list[index - 1]

    index1 = 0
    index2 = 0

    # Find the min_cost
    while index1 < len(original_list):
        val1 = original_list[index1]

        if index2 >= len(after_delete_list):
            val2 = 0
        else:
            val2 = after_delete_list[index2]

        if val1 != val2:
            min_cost += index1 + 1
            del original_list[index1]
        else:
            index1 += 1
            index2 += 1

    return min_cost


'''
The code below runs the test cases. You do NOT need to modify it.
'''


def one_test(test_num, deletions):
    """
    One test.
    Writes to test file + print to console for testing
    """

    min_cost_deletions = row_delete(deletions)
    print(f"Test {test_num + 1}: Min cost to delete = {min_cost_deletions}")
    with open("test_results.txt", "a") as f:
        print(f"{min_cost_deletions}", file=f)


''' delete file before writing to it
    else it will append results to results of previous runs '''
if os.path.isfile("test_results.txt"):
    os.unlink("test_results.txt")

''' this is the main processing loop '''
for test_num in range(0, len(test_data)):
    one_test(test_num, test_data[test_num])