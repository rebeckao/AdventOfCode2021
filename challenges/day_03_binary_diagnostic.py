from typing import List, Tuple


def power_consumption(diagnostics: List[str]) -> Tuple[int, int]:
    common_digits = [0 for _ in diagnostics[0]]
    for measurement in diagnostics:
        for idx, digit in enumerate(measurement):
            if measurement[idx] == '1':
                common_digits[idx] += 1
            else:
                common_digits[idx] -= 1
    binary_gamma = [1 if digit > 0 else 0 for digit in common_digits]
    gamma_rate = _binary_to_decimal(binary_gamma)
    binary_epsilon = [0 if digit > 0 else 1 for digit in common_digits]
    epsilon_rate = _binary_to_decimal(binary_epsilon)
    return gamma_rate, epsilon_rate


def life_support_rating(diagnostics: List[str]) -> Tuple[int, int]:
    oxygen_rate_binary = _resolve_rate(_most_common_digit_at_index, diagnostics)
    co2_rate_binary = _resolve_rate(_least_common_digit_at_index, diagnostics)
    return _binary_to_decimal(oxygen_rate_binary), _binary_to_decimal(co2_rate_binary)


def _resolve_rate(bit_criteria, diagnostics):
    candidates = diagnostics
    index = 0
    while len(candidates) > 1:
        correct_digit = bit_criteria(candidates, index)
        candidates = [candidate for candidate in candidates if int(candidate[index]) == correct_digit]
        index += 1
    return [1 if int(digit) > 0 else 0 for digit in candidates[0]]


def _least_common_digit_at_index(measurements: List[str], index: int) -> int:
    return 1 - _most_common_digit_at_index(measurements, index)


def _most_common_digit_at_index(measurements: List[str], index: int) -> int:
    common_digit = 0
    for measurement in measurements:
        if measurement[index] == '1':
            common_digit += 1
        else:
            common_digit -= 1
    return 1 if common_digit >= 0 else 0


def _binary_to_decimal(binary_gamma):
    gamma_rate = sum([value * pow(2, (len(binary_gamma) - idx - 1)) for idx, value in enumerate(binary_gamma)])
    return gamma_rate
