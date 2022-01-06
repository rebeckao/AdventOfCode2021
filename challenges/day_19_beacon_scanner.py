import re
from dataclasses import dataclass
from typing import List, Dict, Set, Tuple


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
    z: int


def number_of_beacons(raw_scanners: List[str]) -> Tuple[int, int]:
    scanners: dict[int, set[Coordinate]] = parse_scanners(raw_scanners)
    starting_scanner_id = list(scanners.keys())[0]
    identified_beacons = set(scanners[starting_scanner_id])
    already_read_scanners = {starting_scanner_id}
    scanner_locations = {Coordinate(0, 0, 0)}
    while True:
        if len(already_read_scanners) == len(scanners):
            break
        previous_number_of_identified_beacons = len(identified_beacons)
        for scanner_id in scanners:
            if scanner_id in already_read_scanners:
                continue
            new_beacons = scanners[scanner_id]
            correct_orientation_index, offset = correct_orientation_if_any_overlap(identified_beacons, new_beacons)
            if correct_orientation_index is None:
                continue
            scanner_locations.add(offset)
            already_read_scanners.add(scanner_id)
            for beacon in new_beacons:
                correct_orientation = possible_rotations(beacon)[correct_orientation_index]
                coordinates_relative_starting_scanner = Coordinate(correct_orientation.x + offset.x, correct_orientation.y + offset.y, correct_orientation.z + offset.z)
                identified_beacons.add(coordinates_relative_starting_scanner)
        new_number_of_identified_beacons = len(identified_beacons)
        if new_number_of_identified_beacons == previous_number_of_identified_beacons:
            if len(already_read_scanners) != len(scanners):
                print(f"identified scanners: {already_read_scanners}")
            break
    greatest_manhattan_distance = 0
    for scanner_location in scanner_locations:
        distances = relative_distances_to_other_identified(scanner_location, scanner_locations)
        for distance in distances:
            current_manhattan_distance = abs(distance.x) + abs(distance.y) + abs(distance.z)
            if current_manhattan_distance > greatest_manhattan_distance:
                greatest_manhattan_distance = current_manhattan_distance
    return len(identified_beacons), greatest_manhattan_distance


def correct_orientation_if_any_overlap(identified_beacons, new_beacons):
    identified_distances = dict()
    for identified_beacon in identified_beacons:
        identified_distances[identified_beacon] = relative_distances_to_other_identified(identified_beacon, identified_beacons)
    possible_rotations_of_new_beacons = dict()
    for beacon in new_beacons:
        possible_rotations_of_new_beacons[beacon] = possible_rotations(beacon)
    beacon_rotations = [possible_rotations(beacon) for beacon in new_beacons]
    number_of_rotations = len(beacon_rotations[0])
    for idx in range(0, number_of_rotations):
        for new_beacon in new_beacons:
            matches_for_this_beacon = 0
            rotated_beacon = possible_rotations_of_new_beacons[new_beacon][idx]
            distances_to_other_new = relative_distances_to_other_new(idx, possible_rotations_of_new_beacons, rotated_beacon)
            for identified_beacon in identified_beacons:
                distances_to_other_identified = identified_distances[identified_beacon]
                for distance_to_other in distances_to_other_new:
                    if distance_to_other in distances_to_other_identified:
                        matches_for_this_beacon += 1
                if matches_for_this_beacon >= 11:
                    x_offset = identified_beacon.x - rotated_beacon.x
                    y_offset = identified_beacon.y - rotated_beacon.y
                    z_offset = identified_beacon.z - rotated_beacon.z
                    offset = Coordinate(x_offset, y_offset, z_offset)
                    return idx, offset
    return None, None


def relative_distances_to_other_identified(identified_beacon, identified_beacons):
    relative_distances_to_others = set()
    for other in identified_beacons:
        if other == identified_beacon:
            continue
        relative_distances_to_others.add(Coordinate(other.x - identified_beacon.x, other.y - identified_beacon.y, other.z - identified_beacon.z))
    return relative_distances_to_others


def relative_distances_to_other_new(idx, possible_rotations_of_new_beacons, rotated_beacon):
    relative_distances = set()
    for other in possible_rotations_of_new_beacons:
        other_rotated = possible_rotations_of_new_beacons[other][idx]
        if other_rotated == rotated_beacon:
            continue
        relative_distances.add(Coordinate(other_rotated.x - rotated_beacon.x, other_rotated.y - rotated_beacon.y, other_rotated.z - rotated_beacon.z))
    return relative_distances


def possible_rotations(coordinate: Coordinate):
    x = coordinate.x
    y = coordinate.y
    z = coordinate.z
    return [
        Coordinate(x, y, z),
        Coordinate(x, -y, -z),
        Coordinate(x, -z, y),
        Coordinate(x, z, -y),
        Coordinate(-x, z, y),
        Coordinate(-x, -z, -y),
        Coordinate(-x, y, -z),
        Coordinate(-x, -y, z),
        Coordinate(z, x, y),
        Coordinate(-z, x, -y),
        Coordinate(-y, x, z),
        Coordinate(y, x, -z),
        Coordinate(y, -x, z),
        Coordinate(-y, -x, -z),
        Coordinate(-z, -x, y),
        Coordinate(z, -x, -y),
        Coordinate(y, z, x),
        Coordinate(-y, -z, x),
        Coordinate(-z, y, x),
        Coordinate(z, -y, x),
        Coordinate(z, y, -x),
        Coordinate(-z, -y, -x),
        Coordinate(-y, z, -x),
        Coordinate(y, -z, -x)
    ]


def parse_scanners(raw_scanners: List[str]) -> Dict[int, Set[Coordinate]]:
    header_pattern = re.compile("^--- scanner ([0-9]*) ---")
    current_scanner = None
    scanners = {}
    for line in raw_scanners:
        match_result = header_pattern.match(line)
        if match_result:
            scanner_number = match_result.group(1)
            current_scanner = int(scanner_number)
            scanners[current_scanner] = set()
            continue
        if line == "":
            continue
        beacon = [int(coord) for coord in line.split(",")]
        scanners[current_scanner].add(Coordinate(beacon[0], beacon[1], beacon[2]))
    return scanners
