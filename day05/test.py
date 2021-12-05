import unittest
import solution

class TestSolution(unittest.TestCase):

    def test_solve_part1(self):
        lines2 = [["8", "0", "0","8"], ["0", "9", "5","9"], ["9", "4", "3","4"], ["2", "2", "2","1"], ["7", "0", "7","4"], ["6", "4", "2","0"], ["0", "9", "2","9"], ["3", "4", "1","4"], ["0", "0", "8","8"], ["5", "5", "8","2"]]
        self.assertEqual(solution.solve_part1(lines2), 5)

    def test_solve_part2(self):
        lines2 = [["8", "0", "0","8"], ["0", "9", "5","9"], ["9", "4", "3","4"], ["2", "2", "2","1"], ["7", "0", "7","4"], ["6", "4", "2","0"], ["0", "9", "2","9"], ["3", "4", "1","4"], ["0", "0", "8","8"], ["5", "5", "8","2"]]
        self.assertEqual(solution.solve_part2(lines2), 12)

if __name__ == '__main__':
    unittest.main()