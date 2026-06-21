from dataclasses import dataclass


# class Character:
#     """Representing a character."""

#     def __init__(self, first_name, is_alive=True):
#         """Initialize character."""
#         self.first_name = first_name
#         self.is_alive = is_alive

#     def __repr__(self):
#         """Return representation."""
#         return (
#             f"Character(first_name={self.first_name!r}, "
#             f"is_alive={self.is_alive!r})"
#         )

#     def __eq__(self, other):
#         """Compare characters."""
#         if not isinstance(other, Character):
#             return False
#         return (
#             self.first_name == other.first_name
#             and self.is_alive == other.is_alive
#         )


@dataclass
class Character:
    """Representing a character."""

    first_name: str
    is_alive: bool = True
    

ned = Character("Ned")
other = Character("Ned")

print(ned)
print(ned == other)



