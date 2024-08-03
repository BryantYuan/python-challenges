import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('clementiscap'), 'mentiscap')

    def test2(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('a'), 'a')

    def test3(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('abc'), 'abc')

    def test4(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('abcd'), 'abcd')

    def test5(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('abcdeabcdefc'), 'abcdef')

    def test6(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('abccdeaabbcddef'), 'cdea')

    def test7(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('abacacacaaabacaaaeaaafa'), 'bac')

    def test8(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('abcdabcef'), 'dabcef')

    def test9(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('abcbde'), 'cbde')

    def test10(self):
        self.assertEqual(solution.longestSubstringWithoutDuplication('clementisanaram'), 'mentisa')