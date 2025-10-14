def arithmetic_mean(data: list[float]) -> float:
    """Returns the arithmetic mean of the numbers given in a list of floats."""

    return sum(data) / len(data)

def geometric_mean(data: list[float]) -> float:
    """Returns the geometric mean of the numbers given in a list of floats."""

    product = 1
    for item in data:
        product *= item

    return product**(1/len(data))

def median(data: list[float]) -> float:
    """Returns the median of the numbers given in a list of floats."""

    sorted_data = sorted(data)
    if len(data) % 2 == 0:
        return (sorted_data[(len(sorted_data) // 2) - 1] + sorted_data[len(sorted_data) // 2])/2
    else:
        return sorted_data[len(sorted_data) // 2]

def data_range(data: list[float]) -> float:
    """Returns the range of the numbers given in a list of floats."""

    return max(data) - min(data)

def lower_quartile(data: list[float]) -> float:
    """Returns the lower quartile of the numbers given in a list of floats."""

    sorted_data = sorted(data)

    return 0

def upper_quartile(data: list[float]) -> float:
    """Returns the upper quartile of the numbers given in a list of floats."""

    sorted_data = sorted(data)

    return 0

def interquartile_range(data: list[float]) -> float:
    """Returns the interquartile range of the numbers given in a list of floats."""

    lq = lower_quartile(data)
    uq = upper_quartile(data)

    return uq - lq

def mode(data: list[float]) -> list[float]:
    """Returns the mode of the numbers given in a list of floats."""
    numbers = {}

    for item in data:
        if item in numbers:
            numbers[item] += 1
        else:
            numbers[item] = 1

    max_count = max(numbers.values())

    modes = []

    for key, value in numbers.items():
        if value == max_count:
            modes.append(key)

    return modes