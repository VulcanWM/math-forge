import unittest
from math_forge.algebra import quadratic_roots, completing_the_square


class TestQuadraticFunctions(unittest.TestCase):
    def test_quadratic_roots_two_real(self):
        # x^2 - 5x + 6 = 0 -> roots 2 and 3
        roots = quadratic_roots(1, -5, 6)
        self.assertIsInstance(roots, tuple)
        self.assertAlmostEqual(roots[0], 3.0)
        self.assertAlmostEqual(roots[1], 2.0)

    def test_quadratic_roots_one_real(self):
        # x^2 - 2x + 1 = 0 -> root 1 (double root)
        root = quadratic_roots(1, -2, 1)
        self.assertAlmostEqual(root, 1.0)

    def test_quadratic_roots_no_real(self):
        # x^2 + x + 1 = 0 -> discriminant < 0 -> no real roots
        self.assertIsNone(quadratic_roots(1, 1, 1))

    def test_completing_the_square_simple(self):
        # x^2 + 2x + 1 = (x + 1)^2
        self.assertEqual(completing_the_square(1, 2, 1), [1, 1.0, 0.0])

    def test_completing_the_square_with_coeff(self):
        # 2x^2 + 8x + 6 = 2(x + 2)^2 - 2
        result = completing_the_square(2, 8, 6)
        self.assertEqual(result, [2, 2.0, -2.0])


if __name__ == "__main__":
    unittest.main()
