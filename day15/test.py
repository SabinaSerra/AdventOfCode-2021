import unittest
import solution
from pprint import pprint

class TestSolution(unittest.TestCase):

    def test_part1(self):
        problem_input = [[1,1,6,3,7,5,1,7,4,2],
                        [1,3,8,1,3,7,3,6,7,2],
                        [2,1,3,6,5,1,1,3,2,8],
                        [3,6,9,4,9,3,1,5,6,9],
                        [7,4,6,3,4,1,7,1,1,1],
                        [1,3,1,9,1,2,8,1,3,7],
                        [1,3,5,9,9,1,2,4,2,1],
                        [3,1,2,5,4,2,1,6,3,9],
                        [1,2,9,3,1,3,8,5,2,1],
                        [2,3,1,1,9,4,4,5,8,1]]
        problem_input = [[solution.Node(x) for x in line] for line in problem_input]

        actual = solution.solve_part1(problem_input)
        for line in problem_input:
            print(line)
        self.assertEqual(actual, 40)


    def test_part1(self):
        problem_input = [[8,8],
                        [8,8]]
        problem_input = [[solution.Node(x) for x in line] for line in problem_input]
        actual = solution.get_new_data(problem_input)
        for line in actual:
            print(line)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()