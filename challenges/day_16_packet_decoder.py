from functools import reduce
from typing import List, Tuple

hex_to_binary_mapping = {
    "0": [0, 0, 0, 0],
    "1": [0, 0, 0, 1],
    "2": [0, 0, 1, 0],
    "3": [0, 0, 1, 1],
    "4": [0, 1, 0, 0],
    "5": [0, 1, 0, 1],
    "6": [0, 1, 1, 0],
    "7": [0, 1, 1, 1],
    "8": [1, 0, 0, 0],
    "9": [1, 0, 0, 1],
    "A": [1, 0, 1, 0],
    "B": [1, 0, 1, 1],
    "C": [1, 1, 0, 0],
    "D": [1, 1, 0, 1],
    "E": [1, 1, 1, 0],
    "F": [1, 1, 1, 1]
}
LITERAL_TYPE = 4


def hexadecimal_to_binary(hexadecimal: str) -> List[int]:
    binary = []
    for digit in hexadecimal:
        binary += hex_to_binary_mapping[digit]
    return binary


def parse_literal(binary, current_pos) -> Tuple[int, int]:
    digits = []
    while True:
        prefix = binary[current_pos]
        digits += binary[current_pos + 1:current_pos + 5]
        current_pos += 5
        if prefix == 0:
            break
    return current_pos, to_decimal(digits)


def parse_operator(binary, current_pos, type_id) -> Tuple[int, int, int]:
    sum_version_numbers = 0
    length_type_id = binary[current_pos]
    current_pos += 1
    subpacket_values = []
    if length_type_id == 0:
        total_length_of_subpackets = to_decimal(binary[current_pos: current_pos + 15])
        current_pos += 15
        end_of_this_packet = current_pos + total_length_of_subpackets
        while current_pos < end_of_this_packet:
            current_pos, new_sum_version_numbers, value = parse_packet(binary, current_pos)
            subpacket_values.append(value)
            sum_version_numbers += new_sum_version_numbers
    else:
        total_number_of_sub_packets = to_decimal((binary[current_pos: current_pos + 11]))
        current_pos += 11
        for _ in range(0, total_number_of_sub_packets):
            current_pos, new_sum_version_numbers, value = parse_packet(binary, current_pos)
            subpacket_values.append(value)
            sum_version_numbers += new_sum_version_numbers
    total_value = 0
    match type_id:
        case 0:
            total_value = sum(subpacket_values)
        case 1:
            total_value = reduce(lambda a, b: a * b, subpacket_values)
        case 2:
            total_value = min(subpacket_values)
        case 3:
            total_value = max(subpacket_values)
        case 5:
            total_value = 1 if subpacket_values[0] > subpacket_values[1] else 0
        case 6:
            total_value = 1 if subpacket_values[0] < subpacket_values[1] else 0
        case 7:
            total_value = 1 if subpacket_values[0] == subpacket_values[1] else 0
    return current_pos, sum_version_numbers, total_value


def parse_packet(binary: List[int], current_pos: int) -> Tuple[int, int, int]:
    sum_version_numbers = 0
    version_number = to_decimal(binary[current_pos:current_pos + 3])
    current_pos += 3
    sum_version_numbers += version_number
    type_id = to_decimal(binary[current_pos:current_pos + 3])
    current_pos += 3
    if type_id == LITERAL_TYPE:
        current_pos, value = parse_literal(binary, current_pos)
    else:
        current_pos, version_number_sum, value = parse_operator(binary, current_pos, type_id)
        sum_version_numbers += version_number_sum
    return current_pos, sum_version_numbers, value


def to_decimal(binary: List[int]) -> int:
    decimal = 0
    for idx, val in enumerate(binary):
        decimal += pow(2, len(binary) - idx - 1) * val
    return decimal


def sum_of_version_numbers(hexadecimal: str) -> int:
    binary = hexadecimal_to_binary(hexadecimal)
    _, sum_version_numbers, _ = parse_packet(binary, 0)
    return sum_version_numbers


def value_of_expression(hexadecimal: str) -> int:
    binary = hexadecimal_to_binary(hexadecimal)
    _, _, value = parse_packet(binary, 0)
    return value
