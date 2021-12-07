from typing import List, Tuple


def most_fuel_efficient_position(initial_positions: List[int], cost_of_position) -> Tuple[int, int]:
    lowest_cost = cost_of_position(initial_positions, 0)
    best_position = 0
    for x in range(min(initial_positions), max(initial_positions)):
        cost = cost_of_position(initial_positions, x)
        if cost < lowest_cost:
            lowest_cost = cost
            best_position = x
    return best_position, lowest_cost


def linear_cost_of_position(initial_positions, position) -> int:
    return sum([abs(position - x_i) for x_i in initial_positions])


def growing_cost_of_position(initial_positions, position) -> int:
    return sum([growing_cost_of_movement(abs(position - x_i)) for x_i in initial_positions])


def growing_cost_of_movement(steps: int) -> int:
    return int((steps + 1) * steps / 2)
