from typing import List

def arithmetic_mean(data: List[float]) -> float:
    """Returns the arithmetic mean of the numbers given in a list of floats."""

    return sum(data) / len(data)

def geometric_mean(data: List[float]) -> float:
    """Returns the geometric mean of the numbers given in a list of floats."""

    product = 1
    for item in data:
        product *= item

    return product**(1/len(data))