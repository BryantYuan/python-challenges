class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedList1, linkedList2):
    while linkedList1 is not None and linkedList2 is not None:
        if linkedList1 == linkedList2:
            return linkedList1

        linkedList1 = linkedList1.next
        linkedList2 = linkedList2.next

    return None