import collections
import unittest

import pinecones


class GetNumbersTest(unittest.TestCase):
    def test1(self):
        # For now, we will only give one scenario
        result = list(pinecones.getNumbers(_scenario=2, numberOfPineCones=4, listOfPineCones=[2, 4, 5, 4]))
        expected = [4, 5]
        self.assertEqual(expected, result)

    def test2(self):
        # For now, we will only give one scenario
        result = list(pinecones.getNumbers(_scenario=10, numberOfPineCones=4, listOfPineCones=[2, 4, 5, 4]))
        expected = [2, 4, 4, 5]
        self.assertEqual(expected, result)

    def test3(self):
        # For now, we will only give one scenario
        result = list(
            pinecones.getNumbers(_scenario=3, numberOfPineCones=4, listOfPineCones=[84, 91, 85, 1, 4, 51, 187, 18]))
        expected = [85, 91, 187]
        self.assertEqual(expected, result)

    def test4(self):
        # For now, we will only give one scenario
        result = list(pinecones.getNumbers(_scenario=6, numberOfPineCones=4, listOfPineCones=[2, 4, 5, 4]))
        expected = [2, 4, 4, 5]
        self.assertEqual(expected, result)

    def test5(self):
        # For now, we will only give one scenario
        result = list(pinecones.getNumbers(_scenario=2, numberOfPineCones=4, listOfPineCones=[2, 4, 5, 4, 4, 6, 3]))
        expected = [5, 6]
        self.assertEqual(expected, result)


class FindValueTest(unittest.TestCase):
    def test1(self):
        result = pinecones.findValue(collections.deque([2, 3, 4, 4, 4, 5, 6]), 3, 7)
        expected = 16
        self.assertEqual(expected, result)

    def test2(self):
        result = pinecones.findValue(collections.deque([3, 4, 5, 5, 9]), 6, 5)
        expected = 40
        self.assertEqual(expected, result)

    def test3(self):
        result = pinecones.findValue(collections.deque([3, 5]), 10, 2)
        expected = 21
        self.assertEqual(expected, result)

    def test4(self):
        result = pinecones.findValue(collections.deque([8, 8, 9]), 31, 3)
        expected = 117
        self.assertEqual(expected, result)

    def test5(self):
        result = pinecones.findValue(collections.deque([2, 3, 4, 4, 4, 5, 6]), 4, 7)
        expected = 20
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()