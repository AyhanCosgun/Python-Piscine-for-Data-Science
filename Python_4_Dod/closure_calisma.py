def pow(x: int | float) -> int | float:
    return x ** x


def outer():
    x = 10
    y = 20
    def inner(yaz:str):
        nonlocal x,y
        x = x + 1
        print(yaz)
        return x

    return inner


inner_func = outer()
print(inner_func.__closure__)
print(inner_func.__closure__[0].cell_contents)
print(inner_func.__closure__[1].cell_contents)
print(inner_func("ilk"))  # Output: 11
print(inner_func("ikinci"))  # Output: 12
print(inner_func("üçüncü"))  # Output: 13