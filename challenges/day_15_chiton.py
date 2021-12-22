from typing import List


def lowest_risk_breath_first(cave_map: List[str]):
    lowest_risk_to_location = {(0, 0): 0}
    locations_to_explore = {(1, 0): int(cave_map[0][1]), (0, 1): int(cave_map[1][0])}
    max_x = len(cave_map[0]) - 1
    max_y = len(cave_map) - 1
    while len(locations_to_explore) > 0:
        sorted_elements = sorted(locations_to_explore.items(), key=lambda item: item[1])
        next_best_location, risk_to_go_there = sorted_elements[0]
        locations_to_explore.pop(next_best_location)
        x = next_best_location[0]
        y = next_best_location[1]
        if (x == max_x and y == max_y - 1) or (x == max_x - 1 and y == max_y):  # close to goal
            return risk_to_go_there + int(cave_map[max_y][max_x])
        for possible_next in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            new_x = possible_next[0]
            new_y = possible_next[1]
            if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                continue
            new_risk = risk_to_go_there + int(cave_map[new_y][new_x])
            if lowest_risk_to_location.get(possible_next) is None or lowest_risk_to_location[possible_next] > new_risk:
                lowest_risk_to_location[possible_next] = new_risk
                locations_to_explore[possible_next] = new_risk


def lowest_risk_large_cave(cave_map: List[str]):
    lowest_risk_to_location = {(0, 0): 0}
    locations_to_explore = {(1, 0): int(cave_map[0][1]), (0, 1): int(cave_map[1][0])}
    original_x_length = len(cave_map[0])
    original_y_length = len(cave_map)
    max_x = original_x_length * 5 - 1
    max_y = original_y_length * 5 - 1
    large_cave_map = build_large_map(cave_map, original_x_length, original_y_length)
    goal_risk = int(large_cave_map[max_y][max_x])
    while len(locations_to_explore) > 0:
        sorted_elements = sorted(locations_to_explore.items(), key=lambda item: item[1])
        next_best_location, risk_to_go_there = sorted_elements[0]
        locations_to_explore.pop(next_best_location)
        x = next_best_location[0]
        y = next_best_location[1]
        if (x == max_x and y == max_y - 1) or (x == max_x - 1 and y == max_y):  # close to goal
            return risk_to_go_there + goal_risk
        for possible_next in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            new_x = possible_next[0]
            new_y = possible_next[1]
            if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                continue
            new_risk = risk_to_go_there + int(large_cave_map[new_y][new_x])
            if lowest_risk_to_location.get(possible_next) is None or lowest_risk_to_location[possible_next] > new_risk:
                lowest_risk_to_location[possible_next] = new_risk
                locations_to_explore[possible_next] = new_risk


def build_large_map(cave_map, original_x_length, original_y_length):
    large_cave_map = []
    for y_round in range(0, 5):
        for y_in_map in range(0, original_y_length):
            row = y_round * original_y_length + y_in_map
            large_cave_map.append("")
            for x_round in range(0, 5):
                for x_in_map in range(0, original_x_length):
                    col = x_round * original_x_length + x_in_map
                    large_cave_map[row] += str(risk_at_location(cave_map, col, row, original_x_length, original_y_length))
    return large_cave_map


def risk_at_location(cave_map, x, y, x_length, y_length):
    x_increase = int(x / x_length)
    y_increase = int(y / y_length)
    x_pos_in_map = x % x_length
    y_pos_in_map = y % y_length
    value_in_original_map = int(cave_map[y_pos_in_map][x_pos_in_map])
    increased_value = value_in_original_map + x_increase + y_increase
    modulated_value = ((increased_value - 1) % 9) + 1
    return modulated_value
