import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        array = [7, 6, 4, -1, 1, 2]
        target = 16
        result = solution.fourNumberSum(array, target)
        actual = [[7, 6, 4, -1], [7, 6, 1, 2]]
        self.assertEqual(actual, result)

    def test2(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        target = 10
        result = solution.fourNumberSum(array, target)
        actual = [[1, 2, 3, 4]]
        self.assertEqual(actual, result)

    def test3(self):
        array = [5, -5, -2, 2, 3, -3]
        target = 0
        result = solution.fourNumberSum(array, target)
        actual = [[5, -5, -2, 2], [5, -5, 3, -3], [-2, 2, 3, -3]]
        self.assertEqual(actual, result)

    def test4(self):
        array = [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 4
        result = solution.fourNumberSum(array, target)
        actual = [[-2, -1, 1, 6], [-2, 1, 2, 3], [-2, -1, 2, 5], [-2, -1, 3, 4]]
        self.assertEqual(actual, result)

    # def test5(self):
    #     array = [7, 6, 4, -1, 1, 2]
    #     target = 16
    #     result = solution.fourNumberSum(array, target)
    #     actual = [[7, 6, -1, 2], [7, 6, 1, 2]]
    #     self.assertEqual(actual, result)
    #
    # def test6(self):
    #     array = [7, 6, 4, -1, 1, 2]
    #     target = 16
    #     result = solution.fourNumberSum(array, target)
    #     actual = [[7, 6, -1, 2], [7, 6, 1, 2]]
    #     self.assertEqual(actual, result)
    #
    # def test7(self):
    #     array = [7, 6, 4, -1, 1, 2]
    #     target = 16
    #     result = solution.fourNumberSum(array, target)
    #     actual = [[7, 6, -1, 2], [7, 6, 1, 2]]
    #     self.assertEqual(actual, result)
    #
    # def test8(self):
    #     array = [7, 6, 4, -1, 1, 2]
    #     target = 16
    #     result = solution.fourNumberSum(array, target)
    #     actual = [[7, 6, -1, 2], [7, 6, 1, 2]]
    #     self.assertEqual(actual, result)


if __name__ == '__main__':
    unittest.main()