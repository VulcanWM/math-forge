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