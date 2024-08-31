class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedLists1, linkedLists2):
    prev_node = None
    carry = 0
    while linkedLists1 is not None or linkedLists2 is not None:
        val1 = linkedLists1.value if linkedLists1 is not None else 0
        val2 = linkedLists2.value if linkedLists2 is not None else 0
        _sum = val1 + val2 + carry

        if _sum >= 10:
            carry = 1
            _sum -= 10
        else:
            carry = 0
        new_object = LinkedList(_sum)

        if prev_node is not None:
            prev_node.next = new_object
        else:
            head = new_object

        prev_node = new_object

        linkedLists1 = linkedLists1.next if linkedLists1 is not None else None
        linkedLists2 = linkedLists2.next if linkedLists2 is not None else None

    return head