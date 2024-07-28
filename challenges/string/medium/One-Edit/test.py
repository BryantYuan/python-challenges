import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        stringOne = "a"
        stringTwo = "a"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test2(self):
        stringOne = "aaa"
        stringTwo = "aaa"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test3(self):
        stringOne = "a"
        stringTwo = "b"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test4(self):
        stringOne = "ab"
        stringTwo = "b"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test5(self):
        stringOne = "abc"
        stringTwo = "b"
        expected = False
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test6(self):
        stringOne = "ab"
        stringTwo = "a"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test7(self):
        stringOne = "b"
        stringTwo = "ab"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test8(self):
        stringOne = "bb"
        stringTwo = "a"
        expected = False
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test9(self):
        stringOne = "a"
        stringTwo = "ab"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test10(self):
        stringOne = "bb"
        stringTwo = "ab"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test11(self):
        stringOne = "ab"
        stringTwo = "bb"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test12(self):
        stringOne = "hello"
        stringTwo = "helo"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test13(self):
        stringOne = "hello"
        stringTwo = "heo"
        expected = False
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test14(self):
        stringOne = "hello"
        stringTwo = "heloo"
        expected = True
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test15(self):
        stringOne = "hello"
        stringTwo = "heloos"
        expected = False
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test16(self):
        stringOne = "hello"
        stringTwo = "heloos"
        expected = False
        actual = solution.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)