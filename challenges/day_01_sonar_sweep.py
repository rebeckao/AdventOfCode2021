from typing import List


def number_of_increases(measurements: List[int]):
    increases = 0
    prev = measurements[0]
    for measurement in measurements:
        if measurement > prev:
            increases += 1
        prev = measurement
    return increases


def number_of_sliding_window_increases(measurements: List[int]):
    increases = 0
    first = measurements[0]
    second = measurements[1]
    third = measurements[2]
    for measurement in measurements[3:]:
        if second + third + measurement > first + second + third:
            increases += 1
        first = second
        second = third
        third = measurement
    return increases
