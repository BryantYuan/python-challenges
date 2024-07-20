import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        string = 'AlgoExpert is the best!'
        result = 'best! the is AlgoExpert'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test2(self):
        string = 'Reverse These Words'
        result = 'Words These Reverse'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test3(self):
        string = '..H hello 678'
        result = '678 hello ..H'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test4(self):
        string = 'this this words this this this words this'
        result = 'this words this this this words this this'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test5(self):
        string = '1 12 23 34 56'
        result = '56 34 23 12 1'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test6(self):
        string = 'APPLE PEAR PLUM ORANGE'
        result = 'ORANGE PLUM PEAR APPLE'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test7(self):
        string = 'this-is-one-word'
        result = 'this-is-one-word'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test8(self):
        string = 'a'
        result = 'a'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test9(self):
        string = 'ab'
        result = 'ab'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test10(self):
        string = ''
        result = ''
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test11(self):
        string = 'algoexpert is the best platform to use to prepare for coding interviews!'
        result = 'interviews! coding for prepare to use to platform best the is algoexpert'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test12(self):
        string = 'words, seperated, by, commas'
        result = 'commas by, seperated, words,'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test13(self):
        string = 'this     string    has a     lot of     whitespaces'
        result = 'whitespaces     of lot     a has    string     this'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test14(self):
        string = 'a ab a'
        result = 'a ab a'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test15(self):
        string = 'test            '
        result = '            test'
        self.assertEqual(result, solution.reverseWordsInString(string))

    def test16(self):
        string = ' '
        result = ' '
        self.assertEqual(result, solution.reverseWordsInString(string))


if __name__ == '__main__':
    unittest.main()