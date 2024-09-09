from solve_puzzle import solve_puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW (forward) moves"""
                test_board_CW = [3, 6, 7, 1, 1, 2]
                self.assertTrue(solve_puzzle(test_board_CW))

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW (backward) moves"""
                test_board_CCW = [4, 1, 3, 6, 7, 4]
                self.assertTrue(solve_puzzle(test_board_CCW))

        def testMixed(self):
                """Tests a board solveable using only a combination of CW (forward) and CCW (backward) moves"""
                test_board_CW_CCW = [7, 5, 0, 1, 2] # TIP: Add overflow handling
                self.assertTrue(solve_puzzle(test_board_CW_CCW))

        def testUnsolveable(self):
                """Tests an unsolveable board"""
                test_board_unsolvable = [4, 1, 1, 0, 0, 0] # TIP: Add memoization, infinite loop handling
                self.assertFalse(solve_puzzle(test_board_unsolvable))

unittest.main()