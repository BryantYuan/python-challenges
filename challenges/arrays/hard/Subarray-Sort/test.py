import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test2(self):
        self.assertEqual(solution.subarraySort([1, 2]), [-1, -1])

    def test3(self):
        self.assertEqual(solution.subarraySort([2, 1]), [0, 1])

    def test4(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]), [4, 9])

    def test5(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]), [4, 6])

    def test6(self):
        self.assertEqual(solution.subarraySort([1, 2, 8, 4, 5]), [2, 4])

    def test7(self):
        self.assertEqual(solution.subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]), [0, 12])

    def test8(self):
        self.assertEqual(solution.subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 51]), [0, 11])

    def test9(self):
        self.assertEqual(solution.subarraySort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]), [1, 11])

    def test10(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test11(self):
        self.assertEqual(solution.subarraySort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]), [1, 12])

    def test12(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test13(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test14(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test15(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test16(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

    def test17(self):
        self.assertEqual(solution.subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])