import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a student id as a random string of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class representing a student with name, surname,
    active status, an auto-generated login, and a random generated id."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Generates the login for the student after initialization."""
        self.login = self.name[0] + self.surname
