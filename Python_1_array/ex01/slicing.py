list = [1, 2, "ali", True, 5]
# print(list[1:4])  # Output: [2, 3, 4]
# print(list[:3])   # Output: [1, 2, 3]
# print(list[2:])   # Output: [3, 4, 5]
# print(list[-3:-1])  # Output: [3, 4]
# print(list[::2])  # Output: [1, 3, 5]

# print(list[1:4:2])  # Output: [2, 4]
# print(list[3::-2])  # Output: [5, 4, 3] 
# print(list[::-1])  # Output: [5, 4, 3, 2, 1]    

# print(list[4:2])  # Output: []
# #print(list[2.1:3.5])  # Output: TypeError: slice indices must be integers or None or have an __index__ method
# #print(list["a":3])  # Output: TypeError: slice indices must be integers or None or have an __index__ method

# matrix = [
#     [10, 11, 12, 13, 14],
#     [20, 21, 22, 23, 24],
#     [30, 31, 32, 33, 34]
# ]

# #print(matrix[0:2, 1:4])  # Output: TypeError: list indices must be integers or slices, not tuple
# submatrix = [row[1:4] for row in matrix[0:2]]
# print(submatrix)  # Output: [[11, 12, 13], [21, 22, 23]]

# import numpy as np

# matrix = np.array([
#     [10, 11, 12, 13, 14],
#     [20, 21, 22, 23],
#     [30, 31, 32, 33, 34]
# ])

# print(matrix[0:2, 1:4])  # Output: [[11 12 13]
#                             #      [21 22 23]]

print(list[1:4])  # Output: [2, 'ali', True]