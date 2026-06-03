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