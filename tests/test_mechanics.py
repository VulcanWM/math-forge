import unittest
from math_forge.mechanics import find_acceleration_of_pulley_system, G


class TestPulleySystem(unittest.TestCase):
    def test_basic_acceleration(self):
        # Typical cases
        self.assertAlmostEqual(find_acceleration_of_pulley_system(5, 3), (5-3)*G/(5+3))
        self.assertAlmostEqual(find_acceleration_of_pulley_system(10, 2), (10-2)*G/(10+2))
        self.assertAlmostEqual(find_acceleration_of_pulley_system(7, 7), 0.0)  # equal masses

    def test_symmetry(self):
        # Switching masses should give same magnitude
        a1 = find_acceleration_of_pulley_system(4, 9)
        a2 = find_acceleration_of_pulley_system(9, 4)
        self.assertAlmostEqual(a1, a2)

    def test_edge_cases(self):
        # Very small differences
        self.assertAlmostEqual(find_acceleration_of_pulley_system(1e-3, 1e-6), (1e-3 - 1e-6)*G/(1e-3 + 1e-6))

    def test_invalid_masses(self):
        # Zero or negative masses should raise ValueError
        with self.assertRaises(ValueError):
            find_acceleration_of_pulley_system(0, 5)
        with self.assertRaises(ValueError):
            find_acceleration_of_pulley_system(-1, 5)
        with self.assertRaises(ValueError):
            find_acceleration_of_pulley_system(5, -2)
        with self.assertRaises(ValueError):
            find_acceleration_of_pulley_system(0, 0)

if __name__ == "__main__":
    unittest.main()
