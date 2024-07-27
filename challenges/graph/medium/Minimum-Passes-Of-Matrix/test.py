import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        matrix = [[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]]
        result = 3
        actual = solution.minimumPassesOfMatrix(matrix)
        self.assertEqual(actual, result)


if __name__ == '__main__':
    unittest.main()