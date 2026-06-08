import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Prints the original and sliced shapes and returns the sliced list."""

    if not isinstance(family, list) or not family:
        print("Error: family must be a non-empty list.")
        return []

    if not all(isinstance(row, list) for row in family):
        print("Error: family must contain only lists.")
        return []
    if any(isinstance(cell, bool) for row in family for cell in row):
        print("Error: family must contain only int or float values.")
        return []

    column_size = len(family[0])

    if column_size == 0 or not all(len(row) == column_size for row in family):
        print("Error: all rows must have the same non-zero size.")
        return []

    if not isinstance(start, int) or isinstance(start, bool):
        print("Error: start must be an integer.")
        return []

    if not isinstance(end, int) or isinstance(end, bool):
        print("Error: end must be an integer.")
        return []

    try:
        array = np.asarray(family)
    except Exception as e:
        print(f"Error: family must be a 2D numeric array.\n{e}")
        return []

    if array.ndim != 2 or array.size == 0 \
            or not np.issubdtype(array.dtype, np.number):
        print("Error: family must be a non-empty 2D numeric array.")
        return []

    print(f"My shape is : {array.shape}")

    result = array[start:end]
    print(f"My new shape is : {result.shape}")

    return result.tolist()
