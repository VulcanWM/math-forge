# Contributing to MathForge 

Thanks for your interest in contributing! 

MathForge is a student-built math library, and every contribution (big or small) helps the project grow.

This guide will walk you through how to contribute.

---

## Ways to Contribute

* Add new math functions (algebra, geometry, probability, calculus, etc.).
* Improve existing functions (better explanations, clearer code).
* Write or improve tests.
* Add examples in the `examples/` folder.
* Fix typos or improve documentation.

---

## Getting Started

1. **Fork** the repository.
2. **Clone** your fork:

   ```bash
   git clone https://github.com/YOUR-USERNAME/math-forge.git
   cd math-forge
   ```
3. Install dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```
4. Run the tests to make sure everything works:

---

## Adding a Function

1. Open the right file (e.g., `algebra.py` for equations).

2. Add your function. Always include:

   * A clear name
   * Input/output types
   * A short docstring explaining what it does

   Example:

   ```python
   def area_of_triangle(base: float, height: float) -> float:
       """Return the area of a triangle given base and height."""
       
        return 0.5 * base * height
   ```

3. Add a test for your function in the matching file under `tests/`.

   Example (`tests/test_geometry.py`):

   ```python
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

   ```

4. Run tests again

---

## Submitting Your Contribution

1. Commit your changes:

   ```bash
   git add .
   git commit -m "Added area_of_triangle function"
   ```
2. Push your branch:

   ```bash
   git push origin your-branch-name
   ```
3. Open a Pull Request on GitHub.

---

## Code Style

* Keep functions short and clear.
* Use Python type hints where possible.

---

## Need Help?

If you’re new to open source, don’t worry! Feel free to open an issue with questions or ask for help in your pull request.

We’re here to learn together
