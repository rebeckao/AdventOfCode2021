from typing import List


def number_of_increases(measurements: List[int]):
    increases = 0
    prev = measurements[0]
    for measurement in measurements:
        if measurement > prev:
            increases += 1
        prev = measurement
    return increases
