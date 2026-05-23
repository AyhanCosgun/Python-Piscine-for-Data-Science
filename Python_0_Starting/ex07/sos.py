import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": '--. ',
    "H": '.... ',
    "I": '.. ',
    "J": '.--- ',
    "K": '-.- ',
    "L": '.-.. ',
    "M": '-- ',
    "N": '-. ',
    "O": '--- ',
    "P": '.--. ',
    "Q": '--.- ',
    "R": '.-. ',
    "S": '... ',
    "T": '- ',
    "U": '..- ',
    "V": '...- ',
    "W": '.-- ',
    "X": '-..- ',
    "Y": '-.-- ',
    "Z": '--.. ',

    # Digits
    "0": '----- ',
    "1": '.---- ',
    "2": '..--- ',
    "3": '...-- ',
    "4": '....- ',
    "5": '..... ',
    "6": '-.... ',
    "7": '--... ',
    "8": '---.. ',
    "9": '----. ',
}


def main():
    """Encodes the given string (first argument)
    into its Morse Code representation."""
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    string = sys.argv[1]
    if any(not char.isalnum() and char != " " for char in string):
        print("AssertionError: the arguments are bad")
        return

    morse_code = []
    for char in string.upper():
        if char in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char])
    print("".join(morse_code).rstrip())


if __name__ == "__main__":
    main()
