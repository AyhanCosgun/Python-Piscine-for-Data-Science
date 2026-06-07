def slice_me(family: list, start: int, end: int) -> list:
    """Prints the original and sliced shapes and returns the sliced list."""

    if not isinstance(family, list) or not family:
        print("Error: family must be a non-empty list.")
        return []

    if not all(isinstance(row, list) for row in family):
        print("Error: family must contain only lists.")
        return []

    column_size = len(family[0])

    if not all(len(row) == column_size for row in family):
        print("Error: all rows must have the same size.")
        return []

    if not isinstance(start, int) or not isinstance(end, int):
        print("Error: start and end must be integers.")
        return []

    row_size = len(family)
    print(f"My shape is : ({row_size}, {column_size})")

    result = family[start:end]
    result_row_size = len(result)
    print(f"My new shape is : ({result_row_size}, {column_size})")

    return result

