def gcd(a: int, b: int) -> int:
    """Greatest common divisor of two integers using Euclid's algorithm."""

    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Least common multiple of two integers"""

    return abs(a * b) // gcd(a, b)

def is_prime(n: int) -> bool:
    """Returns True if n is prime, False otherwise."""

    num_of_factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            num_of_factors += 1

    return num_of_factors == 2

def prime_factors(n: int) -> list[int]:
    """Returns a list of prime factors of n."""

    n_prime_factors = []
    for i in range(1, n+1):
        if n % i == 0:
            if is_prime(i):
                n_prime_factors.append(i)

    return n_prime_factors