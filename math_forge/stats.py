def arithmetic_mean(data: list[float]) -> float:
    """Returns the arithmetic mean of the numbers given in a list of floats."""

    return sum(data) / len(data)

def geometric_mean(data: list[float]) -> float:
    """Returns the geometric mean of the numbers given in a list of floats."""

    product = 1
    for item in data:
        product *= item

    return product**(1/len(data))

def median(data):
    """Returns the median of the numbers given in a list of floats."""

    sorted_data = sorted(data)
    if len(data) % 2 == 0:
        return (sorted_data[(len(sorted_data) // 2) - 1] + sorted_data[len(sorted_data) // 2])/2
    else:
        return sorted_data[len(sorted_data) // 2]