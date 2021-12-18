from typing import List


def visible_after_fold(points_raw: List[str], fold: str):
    points = parse_points(points_raw)
    new_points = points_after_fold(points, fold)
    return len(new_points)


def result_after_folds(points_raw: List[str], folds: List[str]):
    points = parse_points(points_raw)
    for fold in folds:
        points = points_after_fold(points, fold)
    return printable(points)


def printable(points) -> List[str]:
    max_x = max([point[0] for point in points])
    max_y = max([point[1] for point in points])
    result = ["." * (max_x + 1) for _ in range(0, max_y + 1)]
    for point in points:
        y = point[1]
        x = point[0]
        result[y] = result[y][0:x] + "#" + result[y][x+1:]
    return result


def parse_points(points_raw):
    points = set()
    for point in points_raw:
        coords = point.split(",")
        points.add((int(coords[0]), int(coords[1])))
    return points


def points_after_fold(points, fold):
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
    return new_points
