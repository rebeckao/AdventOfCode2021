from typing import List, Dict, Tuple


def number_of_intersections_excluding_diagonal(vent_lines_raw: List[str]) -> int:
    return _number_of_intersections(_interesting_points_vertical_horizontal, vent_lines_raw)


def number_of_intersections_including_diagonal(vent_lines_raw: List[str]) -> int:
    return _number_of_intersections(_interesting_points_vertical_horizontal_diagonal, vent_lines_raw)


def _number_of_intersections(interesting_lines, vent_lines_raw):
    covered_points: Dict[Tuple[int, int], int] = dict()
    for raw_line in vent_lines_raw:
        parts = raw_line.split(" -> ")
        starting_point = [int(value) for value in parts[0].split(",")]
        ending_point = [int(value) for value in parts[1].split(",")]
        points = interesting_lines(ending_point, starting_point)
        for point in points:
            if point in covered_points:
                covered_points[point] += 1
            else:
                covered_points[point] = 1
    intersections = [value for value in covered_points.values() if value >= 2]
    return len(intersections)


def _interesting_points_vertical_horizontal(starting_point, ending_point):
    points = []
    if starting_point[0] == ending_point[0]:
        if starting_point[1] < ending_point[1]:
            points = [(starting_point[0], y) for y in range(starting_point[1], ending_point[1] + 1)]
        else:
            points = [(starting_point[0], y) for y in range(ending_point[1], starting_point[1] + 1)]
    if starting_point[1] == ending_point[1]:
        if starting_point[0] < ending_point[0]:
            points = [(x, starting_point[1]) for x in range(starting_point[0], ending_point[0] + 1)]
        else:
            points = [(x, starting_point[1]) for x in range(ending_point[0], starting_point[0] + 1)]
    return points


def _interesting_points_vertical_horizontal_diagonal(starting_point, ending_point):
    points = _interesting_points_vertical_horizontal(starting_point, ending_point)
    if len(points) > 0:
        return points
    if starting_point[0] < ending_point[0]:
        steps = 0
        for x in range(starting_point[0], ending_point[0] + 1):
            if starting_point[1] < ending_point[1]:  # \
                points.append((x, starting_point[1] + steps))
            else:  # /
                points.append((x, starting_point[1] - steps))
            steps += 1
    else:
        steps = 0
        for x in range(ending_point[0], starting_point[0] + 1):
            if starting_point[1] < ending_point[1]:  # /
                points.append((x, ending_point[1] - steps))
            else:  # \
                points.append((x, ending_point[1] + steps))
            steps += 1
    return points
