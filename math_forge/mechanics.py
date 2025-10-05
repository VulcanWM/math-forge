G = 9.8


def find_acceleration_of_pulley_system(x: float, y: float) -> float:
    """
    Returns the acceleration (magnitude) of an Atwood pulley system with masses x and y (kg).
    Acceleration direction is towards the heavier mass.
    """
    if x <= 0 or y <= 0:
        raise ValueError("Masses must be positive.")

    return abs(x - y) * G / (x + y)
