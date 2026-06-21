class UpperString(str):
    """String that always stores uppercase text."""

    def __new__(cls, value):
        """Create an uppercase string object."""
        return super().__new__(cls, value.upper())


name = UpperString("ned stark")
print(name)             # NED STARK
print(type(name))       # <class '__main__.UpperString'>


class UpperStrings(str):
    """String that always stores uppercase text."""

    def __init__(cls, value):
        """Create an uppercase string object."""
        super().__init__()
        cls.value = value.upper()


name2 = UpperStrings("ned stark")
print(name2)
print(type(name2))