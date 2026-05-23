import sys
from ft_filter import ft_filter


def main():
    """ Filters words longer than the provided \"lenght\" (second argument)
    in the given \"string\" (first argument)."""

    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        length = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    text = sys.argv[1]

    filtered_words = ft_filter(lambda word: len(word) > length, text.split())
    result = [word for word in filtered_words]

    print(result)


if __name__ == "__main__":
    main()
