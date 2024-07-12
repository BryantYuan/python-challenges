import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        array = [2]
        expected = 2
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test2(self):
        array = [1, 2, 1]
        expected = 1
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test3(self):
        array = [3, 3, 1]
        expected = 3
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test4(self):
        array = [4, 5, 5]
        expected = 5
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test5(self):
        array = [1, 2, 3, 2, 2, 1, 2]
        expected = 2
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test6(self):
        array = [1, 2, 3, 2, 3, 2, 2, 4, 2]
        expected = 2
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test7(self):
        array = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = 1
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test8(self):
        array = [5, 4, 3, 2, 1, 1, 1, 1, 1, ]
        expected = 1
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test9(self):
        array = [1, 1, 1, 1, 1, 5, 4, 3, 2]
        expected = 1
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test10(self):
        array = [1, 1, 1, 1, 2, 2, 2, 2, 2]
        expected = 2
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test11(self):
        array = [453, 6543, 6543, 435, 535, 6543, 6543, 12, 43, 6543, 6543]
        expected = 6543
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test12(self):
        array = [1, 2, 2, 2, 1]
        expected = 2
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test13(self):
        array = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1]
        expected = 4
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)

    def test14(self):
        array = [1, 2, 3, 2, 2, 4, 2, 2, 5, 2, 1]
        expected = 2
        actual = solution.majorityElement(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()