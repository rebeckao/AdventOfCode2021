from typing import List


def syntax_score(lines: List[str]):
    return sum([error_score(first_illegal_character(line)) for line in lines])


def middle_completion_score(lines: List[str]):
    scores = [total_completion_score(line) for line in lines]
    scores = [score for score in scores if score is not None]
    scores.sort()
    return scores[int(len(scores) / 2)]


def first_illegal_character(line: str):
    illegal_character, _ = analyse(line)
    return illegal_character


def analyse(line: str):
    expected = []
    for char in line:
        if char == "(":
            expected.append(")")
        elif char == "[":
            expected.append("]")
        elif char == "{":
            expected.append("}")
        elif char == "<":
            expected.append(">")
        else:
            expected_closing = expected.pop()
            if char != expected_closing:
                return char, expected
    return None, expected


def error_score(char):
    match char:
        case ")":
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137
    return 0


def total_completion_score(line: str):
    illegal_character, completion_in_reverse_order = analyse(line)
    if illegal_character is not None:
        return None
    score = 0
    while len(completion_in_reverse_order) > 0:
        next_closing = completion_in_reverse_order.pop()
        score = score * 5 + correct_score(next_closing)
    return score


def correct_score(char: str):
    match char:
        case ")":
            return 1
        case "]":
            return 2
        case "}":
            return 3
        case ">":
            return 4
