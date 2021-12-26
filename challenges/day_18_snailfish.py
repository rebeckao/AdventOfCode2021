from dataclasses import dataclass
from math import floor, ceil
from typing import List, Union, Tuple


def add(number_1: str, number_2: str) -> str:
    return f"[{number_1},{number_2}]"


def add_explosion_result(number: str, value, coming_from_side) -> str:
    if coming_from_side == 1:
        for idx, char in enumerate(number):
            if char.isdigit():
                steps_to_end_of_number = end_of_number(number[idx:])
                new_value = (int(number[idx:idx + steps_to_end_of_number]) + value)
                return number[0:idx] + str(new_value) + number[idx + steps_to_end_of_number:]
    else:
        for idx in range(len(number) - 1, -1, -1):
            if number[idx].isdigit():
                steps_to_start_of_number = start_of_number(number[0:idx])
                new_value = (int(number[steps_to_start_of_number: idx + 1]) + value)
                return number[0:steps_to_start_of_number] + str(new_value) + number[idx + 1:]
    return number


def end_of_number(number):
    for idx in range(0, len(number)):
        if not number[idx].isdigit():
            return idx


def start_of_number(number: str) -> int:
    for idx in range(len(number) - 1, -1, -1):
        if not number[idx].isdigit():
            return idx + 1


def explode(number: str) -> str:
    level = 0
    for idx, char in enumerate(number):
        if char == "[":
            level += 1
        elif char == "]":
            level -= 1
        elif char.isdigit() and level > 4:
            steps_to_comma = number[idx:].index(",")
            steps_to_end_pair = number[idx:].index("]")
            left_val = int(number[idx:idx + steps_to_comma])
            right_val = int(number[idx + steps_to_comma + 1:idx + steps_to_end_pair])
            left_side = add_explosion_result(number[0:idx - 1], left_val, 0)
            right_side = add_explosion_result(number[idx + steps_to_end_pair + 1:], right_val, 1)
            return f"{left_side}0{right_side}"
    return number


def split(number: str) -> str:
    for idx in range(0, len(number) - 1):
        if number[idx].isdigit() and number[idx + 1].isdigit():
            val = int(number[idx:idx + 2])
            left_number = floor(val / 2.0)
            right_number = ceil(val / 2.0)
            return f"{number[0:idx]}[{left_number},{right_number}]{number[idx + 2:]}"
    return number


def reduce_one_step(number: str) -> str:
    after_explode = explode(number)
    if after_explode != number:
        return after_explode
    after_split = split(number)
    return after_split


def reduce(number: str) -> str:
    before_reduction = number
    while True:
        after_reduction = reduce_one_step(before_reduction)
        if after_reduction == before_reduction:
            return after_reduction
        before_reduction = after_reduction


def add_together_list(raw_numbers: List[str]) -> str:
    result = raw_numbers[0]
    for raw_number in raw_numbers[1:]:
        result = add(result, raw_number)
        result = reduce(result)
    return result


def largest_magnitude(numbers: List[str]) -> int:
    largest_magn = 0
    for first_idx in range(0, len(numbers)):
        for second_idx in range(0, len(numbers)):
            if first_idx == second_idx:
                continue
            result = add_together_list([numbers[first_idx], numbers[second_idx]])
            magn = magnitude(parse_snailfish_expression(result))
            if magn > largest_magn:
                largest_magn = magn
    return largest_magn


@dataclass
class SnailfishNumber:
    plain_value: Union[int, None] = None
    pair: Union[Tuple, None] = None


def parse_snailfish_expression(raw_number: str) -> SnailfishNumber:
    number, _ = parse_snailfish_number(raw_number)
    return number


def parse_snailfish_number(raw_number: str) -> Tuple[SnailfishNumber, str]:
    next_char = raw_number[0]
    if next_char == "[":  # Pair
        left_number, rest_of_string = parse_snailfish_number(raw_number[1:])
        if rest_of_string[0] != ",":
            raise Exception("rest of string should start with ,: " + rest_of_string)
        right_number, rest_of_string = parse_snailfish_number(rest_of_string[1:])
        if rest_of_string[0] != "]":
            raise Exception("rest of string should start with ]: " + rest_of_string)
        return SnailfishNumber(None, (left_number, right_number)), rest_of_string[1:]
    elif next_char.isdigit():  # Regular number
        return SnailfishNumber(int(next_char), None), raw_number[1:]


def magnitude(number: SnailfishNumber) -> int:
    if number.plain_value is not None:
        return number.plain_value
    else:
        return 3 * magnitude(number.pair[0]) + 2 * magnitude(number.pair[1])
