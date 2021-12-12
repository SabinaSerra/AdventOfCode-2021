import unittest
import solution
import numpy as np

class TestSolution(unittest.TestCase):

    def test_convert_input(self):
        problem_input = [["start","A"],
                        ["start","b"],
                        ["A","c"],
                        ["A","end"],
                        ["b","end"]]
        expected_res = {"start": set(["A", "b"]), "A": set(["start", "c", "end"]), "b": set(["start", "end"]),"c": set(["A"]), "end": set(["A", "b"])}
        actual_res = solution.convert_to_cave_map(problem_input)
        self.assertDictEqual(actual_res, expected_res)

    def test_solve_part1(self):
        problem_input = [["start","A"],
                        ["start","b"],
                        ["A","c"],
                        ["A","b"],
                        ["b","d"],
                        ["A","end"],
                        ["b","end"]]
        cave_map = solution.convert_to_cave_map(problem_input)
        self.assertEqual(len(solution.find_paths(cave_map, "part1")), 10)



if __name__ == '__main__':
    unittest.main()