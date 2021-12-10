from typing import List, Dict, Tuple, Set


def risk_scores_of_local_minima(cave_map: List[str]) -> int:
    local_minima_values, _ = _local_minima(cave_map)
    return sum(local_minima_values) + len(local_minima_values)


def _local_minima(cave_map):
    local_minima_values = []
    local_minima_locations = []
    for y, row in enumerate(cave_map):
        for x, location in enumerate(row):
            local_value = int(location)
            lower_than_left_side = x == 0 or local_value < int(row[x - 1])
            lower_than_right_side = x == len(row) - 1 or local_value < int(row[x + 1])
            lower_than_above = y == 0 or local_value < int(cave_map[y - 1][x])
            lower_than_below = y == len(cave_map) - 1 or local_value < int(cave_map[y + 1][x])
            if lower_than_left_side and lower_than_right_side and lower_than_above and lower_than_below:
                local_minima_values.append(local_value)
                local_minima_locations.append((x, y))
    return local_minima_values, local_minima_locations


def basin_sizes(cave_map):
    _, local_minima_points = _local_minima(cave_map)
    points_in_basin: Dict[int, Set[Tuple[int, int]]] = dict()
    basin_for_point = dict()
    for idx, point in enumerate(local_minima_points):
        points_in_basin[idx] = {point}
        basin_for_point[point] = idx
    barriers = set()
    total_number_of_locations = len(cave_map) * len(cave_map[0])
    while len(barriers) + len(basin_for_point) < total_number_of_locations:
        for y, row in enumerate(cave_map):
            for x, location in enumerate(row):
                point = (x, y)
                if point in basin_for_point or point in barriers:
                    continue
                if int(location) == 9:
                    barriers.add(point)
                    continue
                basin = belongs_to_basin(x, y, basin_for_point)
                if basin is not None:
                    basin_for_point[point] = basin
                    points_in_basin[basin].add(point)
    sizes = [len(points_in_basin[basin]) for basin in points_in_basin]
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def belongs_to_basin(x, y, basin_for_point):
    if (x - 1, y) in basin_for_point:
        return basin_for_point[(x - 1, y)]
    if (x + 1, y) in basin_for_point:
        return basin_for_point[(x + 1, y)]
    if (x, y - 1) in basin_for_point:
        return basin_for_point[(x, y - 1)]
    if (x, y + 1) in basin_for_point:
        return basin_for_point[(x, y + 1)]
    return None
