from typing import List


def visible_after_fold(points_raw: List[str], fold: str):
    points = set()
    for point in points_raw:
        coords = point.split(",")
        points.add((int(coords[0]), int(coords[1])))
    fold_instructions = fold[11:].split("=")
    fold_line = int(fold_instructions[1])
    new_points = set()
    if fold_instructions[0] == "y":
        for point in points:
            if point[1] < fold_line:
                new_points.add(point)
            else:
                new_y = fold_line - (point[1] - fold_line)
                new_points.add((point[0], new_y))
    else:
        for point in points:
            if point[0] < fold_line:
                new_points.add(point)
            else:
                new_x = fold_line - (point[0] - fold_line)
                new_points.add((new_x, point[1]))
    return len(new_points)
