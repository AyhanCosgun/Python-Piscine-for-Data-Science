class ManagedFile:
    """Simple context manager for files."""

    def __init__(self, path):
        """Store file path."""
        self.path = path
        self.file = None

    def __enter__(self):
        """Acquire resource."""
        print("opening file")
        self.file = open(self.path, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Release resource."""
        print("closing file")
        self.file.close()
    
    def __del__(self):
        """Destructor to ensure file is closed."""
        if self.file and not self.file.closed:
            print(f"closing file in destructor for {self.path}")
            self.file.close()


# with ManagedFile("data.txt") as file:
#     file.write("hello")
  
# with open("data2.txt", "w", encoding="utf-8") as file:
#     file.write("hello2")

# m = ManagedFile("data5.txt")

# with m as file:
#     file.write("hello3")

# del m

# print("end")