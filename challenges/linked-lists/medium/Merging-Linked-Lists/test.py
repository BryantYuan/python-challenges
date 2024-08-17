import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        l1 = solution.LinkedList(1)
        l1.next = solution.LinkedList(2)
        l2 = solution.LinkedList(3)
        l2.next = l1.next

        expected = l1.next
        actual = solution.mergingLinkedLists(l1, l2)
        self.assertEqual(actual, expected)