import unittest

import solution


class Test(unittest.TestCase):
    def test1(self):
        edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)

    def test2(self):
        edges = [[1, 2], [2], []]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(False, program_result)

    def test3(self):
        edges = [[1, 2], [2], [1]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)

    def test4(self):
        edges = [[1, 2], [2], [1, 3], [3]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)

    def test5(self):
        edges = [[], [0, 2], [0, 3], [0, 4], [0, 5], [0]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(False, program_result)

    def test6(self):
        edges = [[0]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)

    def test7(self):
        edges = [[8], [0, 2], [0, 3], [0, 4], [0, 5], [0], [7], [8], [6]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)

    def test8(self):
        edges = [[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], []]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(False, program_result)

    def test9(self):
        edges = [[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], [0]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)

    def test10(self):
        edges = [[0], [1]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)

    def test11(self):
        edges = [[1, 2], [2], []]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(False, program_result)

    def test12(self):
        edges = [[], [0, 3], [0], [1, 2]]
        program_result = solution.cycleInGraph(edges)
        self.assertEqual(True, program_result)


if __name__ == '__main__':
    unittest.main()