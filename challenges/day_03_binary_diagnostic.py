from typing import List, Tuple


def power_consumption(diagnostics: List[str]) -> Tuple[int, int]:
    gamma_rate_digits = [0 for _ in diagnostics[0]]
    for measurement in diagnostics:
        for idx, digit in enumerate(measurement):
            if measurement[idx] == '1':
                gamma_rate_digits[idx] += 1
            else:
                gamma_rate_digits[idx] -= 1
    binary_gamma = [1 if digit > 0 else 0 for digit in gamma_rate_digits]
    gamma_rate = sum([value * pow(2, (len(binary_gamma) - idx - 1)) for idx, value in enumerate(binary_gamma)])
    binary_epsilon = [0 if digit > 0 else 1 for digit in gamma_rate_digits]
    epsilon_rate = sum([value * pow(2, (len(binary_epsilon) - idx - 1)) for idx, value in enumerate(binary_epsilon)])
    return gamma_rate, epsilon_rate
