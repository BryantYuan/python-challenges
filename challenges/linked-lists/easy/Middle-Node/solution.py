import math


class LinkedLists:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList: LinkedLists):
    length = 0
    next_val = linkedList
    while next_val is not None:
        length += 1
        next_val = next_val.next

    if length % 2 == 0:
        length += 1

    for i in range(math.ceil(length) + 1):
        linkedList = linkedList.next

    return linkedList