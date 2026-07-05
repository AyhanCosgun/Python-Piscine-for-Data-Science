def square(x: int | float) -> int | float:
    """Returns the square of a number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the result of raising a number to its own power."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a closure that applies the given function to x."""

    def inner() -> float:
        """Applies the given function to x and returns the result."""
        nonlocal x
        x = function(x)
        return x

    return inner
