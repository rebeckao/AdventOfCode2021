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
