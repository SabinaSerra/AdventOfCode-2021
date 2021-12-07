import unittest
import solution
import numpy as np

class TestSolution(unittest.TestCase):

    def test_solve_part1(self):
        pos = np.array([16,1,2,0,4,2,7,1,2,14])
        self.assertEqual(solution.solve_part1(pos), 37)

    def test_solve_part2(self):
        pos = np.array([16,1,2,0,4,2,7,1,2,14])
        self.assertEqual(solution.solve_part2(pos), 168)


if __name__ == '__main__':
    unittest.main()