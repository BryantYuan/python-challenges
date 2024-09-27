import unittest

import betty_the_cat2


class PerfectNumberTest(unittest.TestCase):
    def test1(self):
        result = betty_the_cat2.findTarget(10, 2, 5)
        expected = (0, 2)
        self.assertEqual(expected, result)

    def test2(self):
        result = betty_the_cat2.findTarget(14, 7, 5)
        expected = (0, 2)
        self.assertEqual(expected, result)

    def test3(self):
        result = betty_the_cat2.findTarget(10, 1, 12)
        expected = (0, 10)
        self.assertEqual(expected, result)


class MixedNumberTest(unittest.TestCase):
    def test1(self):
        result = betty_the_cat2.findTarget(10, 2, 6)
        expected = (0, 3)
        self.assertEqual(expected, result)

    def test2(self):
        result = betty_the_cat2.findTarget(19, 7, 5)
        expected = (0, 3)
        self.assertEqual(expected, result)

    def test3(self):
        result = betty_the_cat2.findTarget(10, 1, 3)
        expected = (0, 4)
        self.assertEqual(expected, result)


class CombinationNotPerfectTest(unittest.TestCase):
    def test1(self):
        result = betty_the_cat2.findTarget(50, 12, 13)
        expected = (1, 4)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()