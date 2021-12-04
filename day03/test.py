import unittest
import solution

class TestSolution(unittest.TestCase):

    def test_solve_part1_(self):
        input_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
        self.assertEqual(solution.solve_part1(input_list), 198)

    def test_solve_part2_(self):
        input_list = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
        self.assertEqual(solution.solve_part2(input_list), 230)


if __name__ == '__main__':
    unittest.main()