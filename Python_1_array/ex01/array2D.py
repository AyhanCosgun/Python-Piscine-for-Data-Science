def slice_me(family: list, start: int, end: int) -> list:
    """Returns a slice of the list of family members from start to end (exclusive).

    Args:
        family: A list of family members.
        start: The starting index of the slice.
        end: The ending index of the slice (exclusive).
    Returns:
        A list containing the slice of family members from start to end (exclusive).
    """

    if not isinstance(family, list) or not all(isinstance(member, list) for member in family):
        raise ValueError("family must be a list of lists")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("start and end must be integers")
    if start < 0 or end > len(family) or start >= end:
        raise ValueError("start and end must be valid indices of the family list")
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({end - start}, {len(family[0])})")
    return family[start:end]

# tester.py:
# from array2D import slice_me
# family = [[1.80, 78.4],
# [2.15, 102.7],
# [2.10, 98.5],
# [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
# Expected output:
# $> python test_array2D.py
# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]
# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]]
# $>

