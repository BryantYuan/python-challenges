class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedLists1, linkedLists2):
    l1 = ''
    l2 = ''
    while linkedLists1 is not None:
        l1 = str(linkedLists1.value) + l1
        linkedLists1 = linkedLists1.next

    while linkedLists2 is not None:
        l2 = str(linkedLists2.value) + l2
        linkedLists2 = linkedLists2.next

    sum_of_lists = str(int(l1) + int(l2))
    prev_node = None
    head = None

    for num in reversed(sum_of_lists):
        node = LinkedList(int(num))

        if prev_node is not None:
            prev_node.next = node
        else:
            head = node

        prev_node = node

    return head