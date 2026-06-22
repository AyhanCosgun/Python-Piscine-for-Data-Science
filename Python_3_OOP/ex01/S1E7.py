from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a Baratheon character
        with a first name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self) -> None:
        """Changes the character's status to dead."""
        super().die()

    def __str__(self):
        """Overrides the default method __str__ to provide
        an informal string representation of the Baratheon character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """Overrides the default method __repr__ to provide
        a formal string representation of the Baratheon character."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a Lannister character
        with a first name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self) -> None:
        """Changes the character's status to dead."""
        super().die()

    def __str__(self):
        """Overrides the default method __str__ to provide
        an informal string representation of the Lannister character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """Overrides the default method __repr__ to provide
        a formal string representation of the Lannister character."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to create a Lannister character."""
        return cls(first_name, is_alive)
