import unittest
from math_forge.complex_numbers import modulus


class TestComplexNumbers(unittest.TestCase):
    def test_modulus_on_axis(self):
        self.assertEqual(modulus(3, 0), 3.0)  # purely real
        self.assertEqual(modulus(0, 4), 4.0)  # purely imaginary

    def test_modulus_basic(self):
        self.assertAlmostEqual(modulus(3, 4), 5.0)   # 3-4-5 triangle
        self.assertAlmostEqual(modulus(1, 1), 2 ** 0.5)  # √2

    def test_modulus_symmetry(self):
        # modulus should be the same regardless of sign of x/y
        self.assertEqual(modulus(3, 4), modulus(-3, 4))
        self.assertEqual(modulus(3, 4), modulus(3, -4))
        self.assertEqual(modulus(3, 4), modulus(-3, -4))

    def test_modulus_zero(self):
        self.assertEqual(modulus(0, 0), 0.0)


if __name__ == "__main__":
    unittest.main()
