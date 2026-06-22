from S1E7 import Baratheon, Lannister
Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")




# print(f"\n Robert.__str__ : {Robert.__str__}")
# print(f"Robert.__str__() : {Robert.__str__()} \n")

# print(f"Robert.__repr__ : {Robert.__repr__}")
# print(f"Robert.__repr__() : {Robert.__repr__()} \n")

# print(f"Cersei.die : {Cersei.die}")
# print(f"Cersei.die() : {Cersei.die()} \n")


# print(f"Cersei.create_lannister : {Lannister.create_lannister}")
# print(f"Cersei.create_lannister('Cersei2', True) : {Cersei.create_lannister('Cersei2', True)}")


