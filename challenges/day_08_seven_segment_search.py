from typing import List, Dict


def number_of_identifiable_digits_in_output(input: List[str]):
    number_of_identifiable_digits = 0
    for line in input:
        lengths = [len(digit) for digit in line.split("|")[1].split(" ")]
        number_of_identifiable_digits += len([length for length in lengths if length in [2, 4, 3, 7]])  # 1,4,7,8
    return number_of_identifiable_digits


def wire_mapping(digit_lines: str) -> Dict[str, int]:
    digits = [digit for digit in digit_lines.split(" ") if digit != "|"]
    ones = [digit for digit in digits if len(digit) == 2][0]
    fours = [digit for digit in digits if len(digit) == 4][0]
    sevens = [digit for digit in digits if len(digit) == 3][0]
    twos_or_threes_or_fives = set([digit for digit in digits if len(digit) == 5])
    zeros_or_sixes_or_nines = set([digit for digit in digits if len(digit) == 6])
    sides = {}
    for char in "abcdefg":
        if char in sevens and char not in ones:
            sides["top"] = char
        elif char in fours and char_is_in_each(char, twos_or_threes_or_fives):
            sides["middle"] = char
        elif char_is_in_each(char, twos_or_threes_or_fives):
            sides["bottom"] = char
        elif char_is_in_each(char, zeros_or_sixes_or_nines):
            if char in ones:
                sides["bottom-right"] = char
            else:
                sides["top-left"] = char
        elif char in ones:
            sides["top-right"] = char
        else:
            sides["bottom-left"] = char
    return {
        as_sorted_string({sides["top"], sides["top-left"], sides["top-right"], sides["bottom-left"], sides["bottom-right"], sides["bottom"]}): 0,
        as_sorted_string({sides["top-right"], sides["bottom-right"]}): 1,
        as_sorted_string({sides["top"], sides["top-right"], sides["middle"], sides["bottom-left"], sides["bottom"]}): 2,
        as_sorted_string({sides["top"], sides["top-right"], sides["middle"], sides["bottom-right"], sides["bottom"]}): 3,
        as_sorted_string({sides["top-left"], sides["top-right"], sides["middle"], sides["bottom-right"]}): 4,
        as_sorted_string({sides["top"], sides["top-left"], sides["middle"], sides["bottom-right"], sides["bottom"]}): 5,
        as_sorted_string({sides["top"], sides["top-left"], sides["middle"], sides["bottom-left"], sides["bottom-right"], sides["bottom"]}): 6,
        as_sorted_string({sides["top"], sides["top-right"], sides["bottom-right"]}): 7,
        as_sorted_string({sides["top"], sides["top-left"], sides["top-right"], sides["middle"], sides["bottom-left"], sides["bottom-right"], sides["bottom"]}): 8,
        as_sorted_string({sides["top"], sides["top-left"], sides["top-right"], sides["middle"], sides["bottom-right"], sides["bottom"]}): 9
    }


def digits_in_output(digit_line):
    mapping = wire_mapping(digit_line)
    output_digits = [digit for digit in digit_line.split("|")[1].split(" ") if len(digit) > 0]
    identified_output_digits = [mapping[as_sorted_string(digit)] for digit in output_digits]
    return int("".join([str(digit) for digit in identified_output_digits]))


def char_is_in_each(char, digits):
    for digit in digits:
        if char not in digit:
            return False
    return True


def as_sorted_string(as_set):
    as_list = list(as_set)
    as_list.sort()
    return "".join(as_list)
