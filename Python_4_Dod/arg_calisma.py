def f(*args, **kwargs):
    if len(args) == 0:
        print("No positional arguments provided.")
        return
    print(args)
    sorted = list(args)
    sorted.sort()
    print(f"sorted : {sorted}")
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    mean = sum(x for x in args) / len(args)
    print(f"mean : {mean}")


f(1,8,4,7,4)