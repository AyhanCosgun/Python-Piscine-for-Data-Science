import sys


def count_text(text: str) -> dict:
    """
    Counts the number of characters in the text according to categories
    """
    punctuation_chars = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    upper = 0
    lower = 0
    digit = 0
    space = 0
    punctuation = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in punctuation_chars:
            punctuation += 1
    return {"upper": upper, "lower": lower, "digit": digit, "space": space,
            "punctuation": punctuation}


def main():
    """
    Count character categories from a single command-line argument.
    """

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif len(sys.argv) == 1:
        print("What is the text to count?")
        try:
            text = sys.stdin.readline()
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return
    else:
        text = sys.argv[1]

    counts = count_text(text)

    print(f"The text contains {len(text)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


if __name__ == "__main__":
    main()
