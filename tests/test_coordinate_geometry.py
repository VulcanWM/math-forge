import unittest
from math_forge.coordinate_geometry import distance_between_two_points
# adjust the import if your file is named differently


class TestCoordinateGeometry(unittest.TestCase):
    def test_same_point(self):
        # Distance from a point to itself should be 0
        self.assertEqual(distance_between_two_points(0, 0, 0, 0), 0.0)
        self.assertEqual(distance_between_two_points(5, 7, 5, 7), 0.0)

    def test_horizontal_vertical(self):
        # Horizontal distance
        self.assertEqual(distance_between_two_points(0, 0, 5, 0), 5.0)
        # Vertical distance
        self.assertEqual(distance_between_two_points(0, 0, 0, -3), 3.0)

    def test_diagonal(self):
        # Classic 3-4-5 triangle
        self.assertAlmostEqual(distance_between_two_points(0, 0, 3, 4), 5.0)
        # Shifted points
        self.assertAlmostEqual(distance_between_two_points(1, 2, 4, 6), 5.0)

    def test_symmetry(self):
        # Order of points shouldn’t matter
        d1 = distance_between_two_points(2, 3, -1, -1)
        d2 = distance_between_two_points(-1, -1, 2, 3)
        self.assertEqual(d1, d2)

    def test_negative_coordinates(self):
        self.assertAlmostEqual(distance_between_two_points(-2, -3, -5, -7), 5.0)


if __name__ == "__main__":
    unittest.main()
