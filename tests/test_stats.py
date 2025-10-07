import unittest
from math_forge.stats import arithmetic_mean, geometric_mean, median, data_range


class TestStatsFunctions(unittest.TestCase):
    def test_arithmetic_mean(self):
        self.assertEqual(arithmetic_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(arithmetic_mean([10, 20]), 15.0)
        self.assertAlmostEqual(arithmetic_mean([0.1, 0.2, 0.3]), 0.2)

    def test_geometric_mean(self):
        self.assertEqual(geometric_mean([1, 1, 1, 1]), 1.0)
        self.assertEqual(geometric_mean([4, 1]), 2.0)   # sqrt(4*1) = 2
        self.assertAlmostEqual(geometric_mean([1, 2, 3, 6]), 2.4494897, places=6)

    def test_median_odd(self):
        self.assertEqual(median([1, 3, 2]), 2)  # sorted -> [1, 2, 3]

    def test_median_even(self):
        self.assertEqual(median([4, 1, 2, 3]), 2.5)  # sorted -> [1, 2, 3, 4]

    def test_median_with_floats(self):
        self.assertEqual(median([1.5, 2.5, 3.5]), 2.5)
        self.assertEqual(median([1.0, 2.0, 3.0, 4.0]), 2.5)

    def test_data_range(self):
        self.assertEqual(data_range([10.0, 0.9, 5.5]), 9.1)
        self.assertEqual(data_range([-5.4, -0.4, -3.4]), 5.0)
        self.assertEqual(data_range([1.0, 1.0, 1.0]), 0.0)
        self.assertEqual(data_range([0]), 0)

if __name__ == "__main__":
    unittest.main()
