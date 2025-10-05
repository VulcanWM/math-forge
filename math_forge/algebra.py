def quadratic_roots(a: int, b: int, c:int):
    """Returns the roots of ax^2 + bx + c = 0."""

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        return (-1 * b) / (2 * a)
    else:
        root1 = ((-1 * b) + discriminant ** 0.5) / (2 * a)
        root2 = ((-1 * b) - discriminant)**0.5 / (2 * a)
        return root1, root2

def completing_the_square(a: int, b: int, c: int) -> list[int | float]:
    """
    Rewrites the quadratic ax^2 + bx + c into the completed square form:
        k(x + l)^2 + m
    Returns the coefficients [k, l, m].
    """

    k = a
    l = (b/(2*a))
    m = ((-1 * k) * l**2) + c

    return [k, l, m]