from collections import Counter
from typing import List


def polymer_after_steps(template: str, substitutions: List[str], steps: int):
    subs = dict()
    for sub_raw in substitutions:
        sub = sub_raw.split(" -> ")
        subs[sub[0]] = sub[1]
    polymer = template
    for _ in range(0, steps):
        new_polymer = ""
        prev_char = ""
        for char in polymer:
            insertion = subs.get(prev_char + char, "")
            new_polymer += insertion + char
            prev_char = char
        polymer = new_polymer
    return polymer


def polymer_hash(template: str, substitutions: List[str], steps: int):
    polymer = polymer_after_steps(template, substitutions, steps)
    counter = Counter(polymer)
    sorted_elements = sorted(counter.items(), key=lambda item: item[1])
    return sorted_elements[-1][1] - sorted_elements[0][1]
