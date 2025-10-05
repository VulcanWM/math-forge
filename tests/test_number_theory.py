import unittest
from math_forge.number_theory import gcd, lcm, is_prime, prime_factors


class TestMathFunctions(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(17, 13), 1)

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(10, 5), 10)
        self.assertEqual(lcm(7, 3), 21)
        self.assertEqual(lcm(0, 5), 0)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(15))

    def test_prime_factors(self):
        self.assertEqual(prime_factors(28), [2, 7])
        self.assertEqual(prime_factors(60), [2, 3, 5])
        self.assertEqual(prime_factors(13), [13])
        self.assertEqual(prime_factors(1), [])

if __name__ == '__main__':
    unittest.main()
