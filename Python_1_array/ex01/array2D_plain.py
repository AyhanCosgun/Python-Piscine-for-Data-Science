def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def slice_me2(family: list, start: int, end: int) -> list:
    """Print the original and sliced shapes and return the sliced list."""

    if not isinstance(family, list) or not family:
        print("Error: family must be a non-empty list.")
        return []

    if not isinstance(start, int) or isinstance(start, bool):
        print("Error: start must be an integer.")
        return []

    if not isinstance(end, int) or isinstance(end, bool):
        print("Error: end must be an integer.")
        return []

    if not all(isinstance(row, list) for row in family):
        print("Error: family must contain only lists.")
        return []

    column_size = len(family[0])
    if column_size == 0:
        print("Error: rows must contain at least one element.")
        return []

    if not all(len(row) == column_size for row in family):
        print("Error: all rows must have the same size.")
        return []

    if not all(all(is_number(cell) for cell in row) for row in family):
        print("Error: family must contain only int or float values.")
        return []

    row_size = len(family)
    print(f"My shape is : ({row_size}, {column_size})")

    result = family[start:end]
    result_row_size = len(result)
    print(f"My new shape is : ({result_row_size}, {column_size})")

    return result