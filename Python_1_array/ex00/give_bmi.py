def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate the Body Mass Index (BMI) for a list of heights and weights.
    BMI = weight (kg) / (height (m))^2"""

    try:
        height = [float(h) for h in height]
        weight = [float(w) for w in weight]
    except ValueError:
        print("Height and weight lists must contain numeric values.")
        return []
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    
    bmi = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi.append(w / (h ** 2))
    
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to a list of BMI values and return a list of boolean values indicating whether each BMI is above the limit."""
    return [b > limit for b in bmi]





def is_number(value):
    """Return True if value is int or float, but not bool."""
    return isinstance(value, (int, float)) and not isinstance(value, bool)

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI for each height and weight pair."""
    if not isinstance(height, list) or not isinstance(weight, list):
        print("Error: height and weight must be lists.")
        return []

    if len(height) != len(weight):
        print("Error: height and weight must have the same length.")
        return []

    if not all(is_number(h) for h in height):
        print("Error: height must contain only int or float values.")
        return []

    if not all(is_number(w) for w in weight):
        print("Error: weight must contain only int or float values.")
        return []

    if not all(h > 0 for h in height):
        print("Error: height values must be greater than zero.")
        return []

    return [w / (h ** 2) for h, w in zip(height, weight)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value above the limit."""
    if not isinstance(bmi, list):
        print("Error: bmi must be a list.")
        return []

    if not isinstance(limit, int) or isinstance(limit, bool):
        print("Error: limit must be an integer.")
        return []

    if not all(is_number(value) for value in bmi):
        print("Error: bmi must contain only int or float values.")
        return []

    return [value > limit for value in bmi]