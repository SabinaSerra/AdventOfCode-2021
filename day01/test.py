import unittest
import solution

class TestAoc(unittest.TestCase):

    def test_is_prime_returns_true_(self):
        primes = [3, 5, 7, 11]
        for prime in primes:
            self.assertEqual(solution.is_prime(3), True)
    
    def test_is_prime_returns_false(self):
        primes = [2, 4, 6, 9]
        for prime in primes:
            self.assertEqual(solution.is_prime(3), True)

    def test_solve_part2(self):
        numbers = [0, 3, 4, 42, 106, 107, 267, 269]
        self.assertEqual(solution.solve_part2(numbers), 335)




if __name__ == '__main__':
    unittest.main()