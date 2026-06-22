from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a King character,
    inheriting from both Baratheon and Lannister families."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a King character with a first name and alive status."""
        super().__init__(first_name, is_alive)

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

    def set_eyes(self, eyes: str) -> None:
        """A setter for eyes attribute"""
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """A setter for hairs attribute"""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """A getter for eyes attribute"""
        return self.eyes

    def get_hairs(self) -> str:
        """A getter for hairs attribute"""
        return self.hairs
