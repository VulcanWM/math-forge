def gcd(a: int, b: int) -> int:
    """Greatest common divisor of two integers using Euclid's algorithm."""

    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Least common multiple of two integers"""

    return abs(a * b) // gcd(a, b)

def quadratic_roots(a: int, b: int, c:int):
    "Returns the roots of ax^2 + bx + c = 0."

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        return (-1 * b) / (2 * a)
    else:
        root1 = ((-1 * b) + discriminant ** 0.5) / (2 * a)
        root2 = ((-1 * b) - discriminant)**0.5 / (2 * a)
        return root1, root2

