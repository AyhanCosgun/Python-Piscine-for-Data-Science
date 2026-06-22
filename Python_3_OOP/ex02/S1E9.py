from abc import ABC, abstractmethod


class Character(ABC):
    """Represents a character in the Game of Thrones universe."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Changes the character's status to dead."""
        self.is_alive = False


class Stark(Character):
    """Represents a member of the Stark family."""
    def die(self) -> None:
        """Changes the character's status to dead."""
        super().die()
