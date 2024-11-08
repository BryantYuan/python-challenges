"""
2024 CAT Coding free trial

Bus Passengers, CAT 2024 intermediate
"""

import os

from test_data import test_data


def solution(passengers_on, passengers_off):
    """
    Implement solution to Bus Passengers here

    Inputs:
        passengers_on: list of integers representing passengers getting on
        passengers_off: list of integers representing passengers getting off

    Returns:
        greatest possible number of passengers to take the full journey
    """

    # TODO: your code goes here
    max_full_journey = passengers_on[0]
    passengers = 0

    index = 1
    while index < len(passengers_on) - 1:
        on = passengers_on[index]
        off = passengers_off[index]

        if off > passengers:
            rem = off - passengers
            max_full_journey -= rem
            passengers = 0
        else:
            passengers -= off

        passengers += on

        index += 1

    return max_full_journey


"""
The code below runs the test cases. You do NOT need to modify it.
"""


def one_test(test_num, bus_journey):
    """
    One test.
    Writes to test file + print to console for testing
    """

    max_full_journey = solution(bus_journey[0], bus_journey[1])
    print(f"Test {test_num + 1}: Max passengers entire journey = {max_full_journey}")
    with open("test_results.txt", "a") as f:
        print(f"{max_full_journey}", file=f)


""" delete file before writing to it
    else it will append results to results of previous runs """
if os.path.isfile("test_results.txt"):
    os.unlink("test_results.txt")

""" this is the main processing loop """
for test_num in range(0, len(test_data)):
    one_test(test_num, test_data[test_num])