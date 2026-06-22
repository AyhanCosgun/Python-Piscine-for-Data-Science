class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product of the given two vectors V1 and V2."""
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds the given two vectors V1 and V2."""
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts the second vector V2 from the first vector V1."""
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
