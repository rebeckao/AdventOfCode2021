from dataclasses import dataclass
from typing import List, Set, Dict


def number_of_possible_paths(connections: List[str]) -> int:
    caves = to_cave_map(connections)
    all_paths = visited_caves(["start"], caves)
    paths_to_end = [path for path in all_paths if path[-1] == "end"]
    return len(paths_to_end)


def visited_caves(visited: List[str], all_caves: Dict) -> List[List[str]]:
    current_cave = visited[-1]
    if current_cave == "end":
        return [visited]
    else:
        available_caves = all_caves[current_cave].connected_caves
        possible_paths = [visited]
        for cave in available_caves:
            if cave in visited and not all_caves[cave].large:
                continue
            new_visited = visited + [cave]
            new_paths = visited_caves(new_visited, all_caves)
            possible_paths += new_paths
        ending_paths = [path for path in possible_paths if path[-1] == "end"]
        return ending_paths


def to_cave_map(mapping):
    caves = dict()
    for line in mapping:
        caves_in_line = line.split("-")
        first_cave_name = caves_in_line[0]
        second_cave_name = caves_in_line[1]
        if first_cave_name not in caves:
            caves[first_cave_name] = Cave(first_cave_name.isupper(), set())
        if second_cave_name not in caves:
            caves[second_cave_name] = Cave(second_cave_name.isupper(), set())
        caves[first_cave_name].connected_caves.add(second_cave_name)
        caves[second_cave_name].connected_caves.add(first_cave_name)
    return caves


@dataclass
class Cave:
    large: bool
    connected_caves: Set
