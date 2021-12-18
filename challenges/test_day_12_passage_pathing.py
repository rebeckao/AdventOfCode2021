from unittest import TestCase

from challenges.day_12_passage_pathing import number_of_possible_paths, number_of_possible_paths_with_revisit


class Test(TestCase):
    def test_number_of_possible_paths(self):
        self.assertEqual(10, number_of_possible_paths([
            "start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end"
        ]))
        self.assertEqual(19, number_of_possible_paths([
            "dc-end",
            "HN-start",
            "start-kj",
            "dc-start",
            "dc-HN",
            "LN-dc",
            "HN-end",
            "kj-sa",
            "kj-HN",
            "kj-dc"
        ]))
        self.assertEqual(226, number_of_possible_paths([
            "fs-end",
            "he-DX",
            "fs-he",
            "start-DX",
            "pj-DX",
            "end-zg",
            "zg-sl",
            "zg-pj",
            "pj-he",
            "RW-he",
            "fs-DX",
            "pj-RW",
            "zg-RW",
            "start-pj",
            "he-WI",
            "zg-he",
            "pj-fs",
            "start-RW"
        ]))

    def test_number_of_possible_paths_real_input(self):
        with open('inputs/day_12.txt') as f:
            cave_mappings = f.read().splitlines()
            self.assertEqual(4011, number_of_possible_paths(cave_mappings))

    def test_number_of_possible_paths_with_revisit(self):
        self.assertEqual(36, number_of_possible_paths_with_revisit([
            "start-A",
            "start-b",
            "A-c",
            "A-b",
            "b-d",
            "A-end",
            "b-end"
        ]))
        self.assertEqual(103, number_of_possible_paths_with_revisit([
            "dc-end",
            "HN-start",
            "start-kj",
            "dc-start",
            "dc-HN",
            "LN-dc",
            "HN-end",
            "kj-sa",
            "kj-HN",
            "kj-dc"
        ]))
        self.assertEqual(3509, number_of_possible_paths_with_revisit([
            "fs-end",
            "he-DX",
            "fs-he",
            "start-DX",
            "pj-DX",
            "end-zg",
            "zg-sl",
            "zg-pj",
            "pj-he",
            "RW-he",
            "fs-DX",
            "pj-RW",
            "zg-RW",
            "start-pj",
            "he-WI",
            "zg-he",
            "pj-fs",
            "start-RW"
        ]))

    def test_number_of_possible_paths_with_revisit_real_input(self):
        with open('inputs/day_12.txt') as f:
            cave_mappings = f.read().splitlines()
            self.assertEqual(108035, number_of_possible_paths_with_revisit(cave_mappings))
