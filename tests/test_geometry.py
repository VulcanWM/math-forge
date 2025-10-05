import unittest
from math_forge.geometry import area_of_triangle


class TestGeometryFunctions(unittest.TestCase):
    def test_area_triangle_positive(self):
        # Basic triangle
        self.assertEqual(area_of_triangle(4, 5), 10.0)
        self.assertEqual(area_of_triangle(10, 2), 10.0)
        self.assertAlmostEqual(area_of_triangle(3.5, 4.2), 7.35)

    def test_area_triangle_zero(self):
        # Zero base or height should give area 0
        self.assertEqual(area_of_triangle(0, 5), 0.0)
        self.assertEqual(area_of_triangle(4, 0), 0.0)
        self.assertEqual(area_of_triangle(0, 0), 0.0)


if __name__ == "__main__":
    unittest.main()
