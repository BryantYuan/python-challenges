class LinkedLists:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head: LinkedLists, k: int):
    length = 0
    next_val = head
    while next_val is not None:
        length += 1
        next_val = next_val.next

    length -= k

    for i in range(length - 1):
        head = head.next

    head.next = head.next.next