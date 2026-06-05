def is_number(value):
    """Return True if value is int or float, but not bool."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the Body Mass Index (BMI)
    for each pair of height and weight in the given lists.
    BMI = weight (kg) / (height (m))^2"""

    if not isinstance(height, list) or not isinstance(weight, list):
        print("Error: height and weight must be lists.")
        return []
    if len(height) != len(weight):
        print("Error: height and weight must have the same length.")
        return []
    if not all(is_number(h) and h > 0 for h in height):
        print("Error: height must contain only positive int or float values.")
        return []

    if not all(is_number(w) and w > 0 for w in weight):
        print("Error: weight must contain only positive int or float values.")
        return []

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Retruns a list of boolean values
    indicating whether each BMI is above the limit."""
    if not isinstance(bmi, list):
        print("Error: bmi must be a list.")
        return []

    if not all(is_number(value) for value in bmi):
        print("Error: bmi must contain only int or float values.")
        return []

    if not isinstance(limit, int) or isinstance(limit, bool):
        print("Error: limit must be an integer.")
        return []

    return [value > limit for value in bmi]
