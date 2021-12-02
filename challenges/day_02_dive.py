from typing import List, Tuple


def dive(instructions: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    for instruction in instructions:
        action, raw_value = instruction.split(" ")
        value = int(raw_value)
        match action:
            case "forward":
                horizontal += value
            case "down":
                depth += value
            case "up":
                depth -= value
    return horizontal, depth


def dive_with_aim(instructions: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        action, raw_value = instruction.split(" ")
        value = int(raw_value)
        match action:
            case "forward":
                horizontal += value
                depth += value * aim
            case "down":
                aim += value
            case "up":
                aim -= value
    return horizontal, depth
