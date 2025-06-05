import unittest
from typing import List
from solution import Solution

class TestWordSearch(unittest.TestCase):
    def test_example_cases(self):
        sol = Solution()

        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "ABCCED"
        self.assertTrue(sol.exist(board, word))

        word = "SEE"
        self.assertTrue(sol.exist(board, word))

        word = "ABCB"
        self.assertFalse(sol.exist(board, word))

        board = [['A']]
        word = "A"
        self.assertTrue(sol.exist(board, word))

        word = "B"
        self.assertFalse(sol.exist(board, word))

if __name__ == "__main__":
    unittest.main()