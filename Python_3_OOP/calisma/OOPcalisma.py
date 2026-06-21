from abc import ABC, abstractmethod


class Character(ABC):
    """Representing a character."""

    def __init__(self, first_name):
        """Initialize a character."""
        self.first_name = first_name

    def say_name(self):
        print(self.first_name)

    @abstractmethod
    def die(self):
        """Change alive state to False."""
        self.is_alive = False


class Stark(Character):
    """Representing a Stark character."""

    def __init__(self, first_name):
        """Initialize a Stark character."""
        super().__init__(first_name)
        self._protected = "protected"
        self.__private = "private"

    def __str__(self):
        return self.first_name

    def die(self):
        super().die()
    
    @property
    def protected(self):
        return self._protected
    
    @protected.setter
    def protected(self, value):
        self._protected = value


class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


# Arya = Stark("Arya")
# print(Arya)
# print(Arya._Stark__private)
# print(Arya.__private)
# print(Arya.__dict__)


##MRO

class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B"


class C(A):
    def who(self):
        return "C"


class D(B, C):
    pass


# print(D.mro())
# print(D().who())


class Base:
    """Base class."""

    def __init__(self):
        """Initialize base secret."""
        self.secret = "base"


class Derived(Base):
    """Derived class."""

    def __init__(self):
        """Initialize both secrets."""
        super().__init__()
        self.secret = "derived"


obj = Derived()
print(obj.__dict__)