from collections import Counter
from typing import List


def polymer_after_steps(template, subs, steps):
    polymer = list(template)
    for _ in range(0, steps):
        new_polymer = ""
        prev_char = ""
        for char in polymer:
            insertion = subs.get(prev_char + char, "")
            new_polymer += insertion + char
            prev_char = char
        polymer = new_polymer
    return polymer


def parse_substitutions(substitutions):
    subs = dict()
    for sub_raw in substitutions:
        sub = sub_raw.split(" -> ")
        subs[sub[0]] = sub[1]
    return subs


def polymer_hash(template: str, substitutions: List[str], steps: int):
    polymer = polymer_after_steps(template, parse_substitutions(substitutions), steps)
    counter = Counter(polymer)
    sorted_elements = sorted(counter.items(), key=lambda item: item[1])
    return sorted_elements[-1][1] - sorted_elements[0][1]


def parse_template(template):
    polymer = dict()
    for idx, char in enumerate(template[0:-1]):
        pair = char + template[idx + 1]
        occurrences_of_pair = polymer.get(pair, 0)
        polymer[pair] = occurrences_of_pair + 1
    return polymer


def increase_by(multiplier, the_dict, key):
    prev = the_dict.get(key, 0)
    the_dict[key] = prev + multiplier


def optimized_polymerization(template: str, subs_raw: List[str], steps):
    substitutions = parse_substitutions(subs_raw)
    polymer = parse_template(template)
    for _ in range(0, steps):
        new_polymer = dict()
        for pair in polymer:
            occurrences = polymer[pair]
            if pair in substitutions:
                first_pair = pair[0] + substitutions[pair]
                second_pair = substitutions[pair] + pair[1]
                increase_by(occurrences, new_polymer, first_pair)
                increase_by(occurrences, new_polymer, second_pair)
            else:
                increase_by(occurrences, new_polymer, pair)
        polymer = new_polymer
    character_counter = dict()
    first_char = template[0]
    last_char = template[-1]
    for pair in polymer:
        first = pair[0]
        second = pair[1]
        increase_by(polymer[pair], character_counter, first)
        increase_by(polymer[pair], character_counter, second)
    for char in character_counter:
        if char == first_char or char == last_char:
            character_counter[char] = int((character_counter[char] + 1) / 2)
        else:
            character_counter[char] = int(character_counter[char] / 2)
    sorted_elements = sorted(character_counter.items(), key=lambda item: item[1])
    return sorted_elements[-1][1] - sorted_elements[0][1]
