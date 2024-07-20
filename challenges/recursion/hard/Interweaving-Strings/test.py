import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test2(self):
        one = "a"
        two = "b"
        three = "ab"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test3(self):
        one = "a"
        two = "b"
        three = "ba"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test4(self):
        one = "a"
        two = "b"
        three = "ac"
        self.assertEqual(solution.interweavingStrings(one, two, three), False)

    def test5(self):
        one = "abc"
        two = "def"
        three = "abcdef"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test6(self):
        one = "abc"
        two = "def"
        three = "adbcef"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test7(self):
        one = "abc"
        two = "def"
        three = "deabcf"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test8(self):
        one = "aabcc"
        two = "dbbca"
        three = "aadbbcbcac"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test9(self):
        one = "aabcc"
        two = "dbbca"
        three = "aadbbbaccc"
        self.assertEqual(solution.interweavingStrings(one, two, three), False)

    def test10(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "aylogoure-xdpreeratm-job"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test11(self):
        one = "aaaaaaa"
        two = "aaaabaaa"
        three = "aaaaaaaaaaaaaab"
        self.assertEqual(solution.interweavingStrings(one, two, three), False)

    def test12(self):
        one = "aaaaaaa"
        two = "aaaaaaa"
        three = "aaaaaaaaaaaaaa"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test13(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test14(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test15(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test16(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test17(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test18(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test19(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)

    def test20(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(solution.interweavingStrings(one, two, three), True)