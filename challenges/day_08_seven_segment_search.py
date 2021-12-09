from typing import List


def number_of_identifiable_digits_in_output(input: List[str]):
    number_of_identifiable_digits = 0
    for line in input:
        lengths = [len(digit) for digit in line.split("|")[1].split(" ")]
        number_of_identifiable_digits += len([length for length in lengths if length in [2, 4, 3, 7]])
    return number_of_identifiable_digits
