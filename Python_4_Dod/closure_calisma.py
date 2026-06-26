def pow(x: int | float) -> int | float:
    return x ** x


def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 1
        return x

    return inner


inner_func = outer()
print(inner_func())  # Output: 11
print(inner_func())  # Output: 12
print(inner_func())  # Output: 13
res = (-0.5) ** (-0.5)
print(res)  # Output: 0.7071067811865476