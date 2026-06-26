from typing import Any


def is_number(value: Any) -> bool:
    """Checks if a value is a number (int or float)."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def median_sorted(data: list) -> float:
    """Calculates the median of a sorted list."""
    n = len(data)
    mid = n // 2

    if n % 2:
        return data[mid]
    return (data[mid - 1] + data[mid]) / 2


def quartiles(data: list) -> tuple[float, float]:
    """Calculates the first and third quartiles of a sorted list
    according to Tukey's method."""
    n = len(data)
    mid = n // 2

    if n % 2:
        lower = data[:mid + 1]
        upper = data[mid:]
    else:
        lower = data[:mid]
        upper = data[mid:]

    Q1 = median_sorted(lower)
    Q3 = median_sorted(upper)

    return Q1, Q3


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculates and prints requested statistics
    based on provided positional arguments"""
    if not all(is_number(arg) for arg in args):
        print("ERROR: All positional arguments must be numbers.")
        return
    arg_len = len(args)
    if arg_len == 0:
        occurance = len([request for request in kwargs.values()
                         if request.lower() in
                         ["mean", "median", "quartile", "std", "var"]])
        for i in range(occurance):
            print("ERROR")
        return
    sorted = list(args)
    sorted.sort()
    mean = sum(x for x in args) / arg_len
    for request in kwargs.values():
        if request.lower() == "mean":
            print(f"mean : {mean}")
        elif request.lower() == "median":
            median = median_sorted(sorted)
            print(f"median : {median}")
        elif request.lower() == "quartile":
            Q1, Q3 = quartiles(sorted)
            print(f"quartile : [{Q1:.1f}, {Q3:.1f}]")
        elif request.lower() == "var":
            variance = sum((x - mean) ** 2 for x in args) / arg_len
            print(f"variance : {variance}")
        elif request.lower() == "std":
            variance = sum((x - mean) ** 2 for x in args) / arg_len
            std_dev = variance ** 0.5
            print(f"std : {std_dev}")
