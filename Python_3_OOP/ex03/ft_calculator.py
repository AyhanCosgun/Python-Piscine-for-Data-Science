class calculator:
    """A class that represents a calculator for vector-scalar operations."""
    def __init__(self, vector: list):
        """Initializes a vector with properties of the class calculator."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds each entry of the vector with the scalar given
        and prints the resulting vector."""
        self.vector = [entry + object for entry in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplies each entry of the vector with the scalar given
        and prints the resulting vector."""
        self.vector = [entry * object for entry in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtracts each entry of the vector with the scalar given
        and prints the resulting vector."""
        self.vector = [entry - object for entry in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divides each entry of the vector with the scalar given
        and prints the resulting vector."""
        if object == 0:
            print("Error: division by zero")
            return
        self.vector = [entry / object for entry in self.vector]
        print(self.vector)
