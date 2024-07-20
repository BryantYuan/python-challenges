import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        matrix = [[1, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 1, 1],
                  [0, 0, 1, 0, 1, 0],
                  [1, 1, 0, 0, 1, 0],
                  [1, 0, 1, 1, 0, 0],
                  [1, 0, 0, 0, 0, 1]]
        result = solution.removeIslands(matrix)
        actual = [[1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 1, 0],
                  [1, 1, 0, 0, 1, 0],
                  [1, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 1]]
        self.assertEqual(actual, result)

    def test2(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        target = 10
        result = solution.removeIslands(array)
        actual = [[1, 2, 3, 4]]
        result.sort()
        actual.sort()
        self.assertEqual(actual, result)

    def test3(self):
        array = [5, -5, -2, 2, 3, -3]
        target = 0
        result = solution.removeIslands(array)
        actual = [[5, -5, -2, 2], [5, -5, 3, -3], [-2, 2, 3, -3]]
        result.sort()
        actual.sort()
        self.assertEqual(actual, result)

    def test4(self):
        array = [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 4
        result = solution.removeIslands(array)
        actual = [[-2, -1, 1, 6], [-2, 1, 2, 3], [-2, -1, 2, 5], [-2, -1, 3, 4]]
        result.sort()
        actual.sort()
        self.assertEqual(actual, result)

    def test5(self):
        array = [-1, 22, 18, 4, 7, 11, 2, -5, -3]
        target = 30
        result = solution.removeIslands(array)
        actual = [[-1, 22, 7, 2], [22, 4, 7, -3], [-1, 18, 11, 2], [18, 4, 11, -3], [22, 11, 2, -5]]
        result.sort()
        actual.sort()
        self.assertEqual(actual, result)

    #
    # def test6(self):
    #     array = [7, 6, 4, -1, 1, 2]
    #     target = 16
    #     result = solution.removeIslands(array)
    #     actual = [[7, 6, -1, 2], [7, 6, 1, 2]]
    #     self.assertEqual(actual, result)
    #
    def test7(self):
        array = [1, 2, 3, 4, 5]
        target = 100
        result = solution.removeIslands(array)
        actual = []
        self.assertEqual(actual, result)
        result.sort()
        actual.sort()

    def test8(self):
        array = [1, 2, 3, 4, 5, -5, 6, -6]
        target = 5
        result = solution.removeIslands(array)
        actual = [[2, 3, 5, -5], [1, 4, 5, -5], [2, 4, 5, -6], [1, 3, -5, 6], [2, 3, 6, -6], [1, 4, 6, -6]]
        result.sort()
        actual.sort()
        self.assertEqual(actual, result)


if __name__ == '__main__':
    unittest.main()