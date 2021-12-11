from typing import List


def total_flashes_after_steps(octopuses: List[str], steps: int):
    current_octopuses = [[int(octopus) for octopus in row] for row in octopuses]
    total_number_of_flashes = 0
    for step in range(steps):
        has_already_flashed = dict()
        for y, row in enumerate(current_octopuses):
            for x, octopus in enumerate(row):
                increase_and_possibly_flash((x, y), current_octopuses, has_already_flashed)
        for octopus in has_already_flashed:
            current_octopuses[octopus[1]][octopus[0]] = 0
        total_number_of_flashes += len(has_already_flashed)
    return total_number_of_flashes


def increase_and_possibly_flash(octopus_location, current_octopuses, has_already_flashed):
    x = octopus_location[0]
    y = octopus_location[1]
    max_y = len(current_octopuses) - 1
    max_x = len(current_octopuses[0]) - 1
    current_octopuses[y][x] += 1
    if current_octopuses[y][x] > 9 and not has_already_flashed.get((x, y), False):
        has_already_flashed[octopus_location] = True
        for x_neighbour in range(max(0, x - 1), min(max_x, x + 1) + 1):
            for y_neighbour in range(max(0, y - 1), min(max_y, y + 1) + 1):
                if not (x == x_neighbour and y == y_neighbour):
                    increase_and_possibly_flash((x_neighbour, y_neighbour), current_octopuses, has_already_flashed)
