def gcd(a: int, b: int) -> int:
    """Greatest common divisor of two integers using Euclid's algorithm."""

    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Least common multiple of two integers"""

    return abs(a * b) // gcd(a, b)