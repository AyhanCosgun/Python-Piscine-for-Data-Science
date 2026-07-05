from typing import Any


def callLimit(limit: int):
    """A decorator factory that returns a decorator
    limiting the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """A decorator that takes as an argument the original function
        to be decorated under the \"@callLimit(limit)\" line
        and returns a wrapper function to wrap the original function."""
        def limit_function(*args: Any, **kwds: Any):
            """A wrapper function that replaces the original function"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return None
        return limit_function
    return callLimiter
