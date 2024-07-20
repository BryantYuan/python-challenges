import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, solution.numberOfWaysToMakeChange(6, [1, 5]))

    def test2(self):
        self.assertEqual(1, solution.numberOfWaysToMakeChange(0, [2, 3, 4, 7]))

    def test3(self):
        self.assertEqual(0, solution.numberOfWaysToMakeChange(9, [5]))

    def test4(self):
        self.assertEqual(0, solution.numberOfWaysToMakeChange(7, [2, 4]))

    def test5(self):
        self.assertEqual(1, solution.numberOfWaysToMakeChange(4, [1, 5, 10, 25]))

    def test6(self):
        self.assertEqual(2, solution.numberOfWaysToMakeChange(5, [1, 5, 10, 25]))

    def test7(self):
        self.assertEqual(4, solution.numberOfWaysToMakeChange(10, [1, 5, 10, 25]))

    def test8(self):
        self.assertEqual(13, solution.numberOfWaysToMakeChange(25, [1, 5, 10, 25]))

    def test9(self):
        self.assertEqual(4, solution.numberOfWaysToMakeChange(12, [2, 3, 7]))

    def test10(self):
        self.assertEqual(3, solution.numberOfWaysToMakeChange(7, [2, 3, 4, 7]))


if __name__ == '__main__':
    unittest.main()