from time import sleep
import os
from tqdm import tqdm
# tuple1 = (3, "ads")
# tuple2 = 5,"bds"

# print(type(tuple1))
# print(id(tuple1))

# tuple1 = 5 ** 0.5
# print(type(tuple1))
# print(type(tuple2))

# str = "Ayhan"
# print(str[0])
# print(str[1])

# evens = (x for x in range(10) if x % 2 == 0)
# print(*evens) # [0, 2, 4, 6, 8]
# a,b = next(enumerate("Ayhan"))
# print(a)
# i,asd =a.__next__()
# print(i)
# print(asd)

# list = ["a","b","c", 1,2,3]
# tuple = ['x','y','z', 4,5,6]
# for list_elm, tuple_elm in zip(list, tuple):
#     print(list_elm, tuple_elm)

# keys = ["km", 6]
# values = [120000, 5000]
# d = dict(zip(keys, values))
# print(d)

# ft_set = {"Hello", "tutu!"}

# print(ft_set)
# set1 = {"Hello", "tutu!", "tata", "selam"}
# print('*'.join(set1))

# width = os.get_terminal_size().columns
# print(f"Terminal width: {width} columns")

# for i in range(100):
#     new_width = os.get_terminal_size().columns
#     if new_width != width:
#         width = new_width
#         print(f"Terminal width changed: {width} columns")
#     sleep(0.1)

# for i in range(100):
#     filled = int(width * (i+1) / 100)
#     empty = width - filled
#     bar = "=" * (filled//2) + ">" + " " * (empty//2)
#     print(f"\r{i+1}%| [{bar}", end="] |", flush=True)
#     sleep(0.1)

gen = (x for x in range(100))

for x in tqdm(gen, total=100):
    sleep(0.1)

# str = " [00:01<00:00, 191.61it/s] "
# print(len(str))

# print("="*(-10) + ">")