from ft_filter import ft_filter


def main():
    values_list = [0, 1, "", "hello", None, [], [1, 2], False, True]
    words_set = {"hi", "", "hello", "", "world"}
    numbers_tuple = (1, 2, 3, 4, 5, 6)
    string = "Hello World !"
    dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
    numbers_range = range(10)
    numbers_gen = (x for x in range(10))


    def is_even(x):
        print(f"checking {x}...")
        return x % 2 == 0


    print(f"values_list ft_filter result       :  {list(ft_filter(None, values_list))}")
    print(f"values_list original filter result :  {list(filter(None, values_list))}")
    print(f"\n {50 * '*'} \n")
    print(f"words_set ft_filter result       :  {list(ft_filter(lambda word: len(word) > 4, words_set))}")
    print(f"words_set original filter result :  {list(filter(lambda word: len(word) > 4, words_set))}")
    print(f"\n {50 * '*'} \n")
    print(f"numbers_tuple ft_filter result       :  {list(ft_filter(lambda n: n > 3, numbers_tuple))}")
    print(f"numbers_tuple original filter result :  {list(filter(lambda n: n > 3, numbers_tuple))}")
    print(f"\n {50 * '*'} \n")
    print(f"string ft_filter result       :  {list(ft_filter(lambda c: c.isupper(), string))}")
    print(f"string original filter result :  {list(filter(lambda c: c.isupper(), string))}")
    print(f"\n {50 * '*'} \n")
    print(f"dictionary ft_filter result       :  {list(ft_filter(lambda k: dictionary[k] > 2, dictionary))}")
    print(f"dictionary original filter result :  {list(filter(lambda k: dictionary[k] > 2, dictionary))}")
    print(f"\n {50 * '*'} \n")
    print(f"numbers_range ft_filter result       :  {list(ft_filter(lambda n: n % 2 == 0, numbers_range))}")
    print(f"numbers_range original filter result :  {list(filter(lambda n: n % 2 == 0, numbers_range))}")
    print(f"\n {50 * '*'} \n")
    print(f"numbers_gen ft_filter result          :  {list(ft_filter(lambda n: n % 2 == 1, numbers_gen))}")
    print(f"numbers_gen original filter result (!):  {list(filter(lambda n: n % 2 == 1, numbers_gen))}")

    print(f"\n {20 * '*'}   LAZY  WORKING  {20 * '*'} \n")

    numberrange = range(10)
    # numberrange = range(1000000)

    print("Before original filter call")
    original = filter(is_even, numberrange)
    print("After original filter call \n")

    print("Before consuming original")
    print(next(original))
    print(next(original))
    print("After consuming original \n")

    print("---"*10)

    print("Before ft_filter call")
    custom = ft_filter(is_even, numberrange)
    print("After ft_filter call \n")

    print("Before consuming ft_filter")
    print(next(custom))
    print(next(custom))
    print("After consuming ft_filter")

if __name__ == "__main__":
    main()
