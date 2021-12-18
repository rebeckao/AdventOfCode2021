from unittest import TestCase

from challenges.day_14_extended_polymerization import polymer_after_steps, polymer_hash


class Test(TestCase):
    def test_polymer_after_steps(self):
        self.assertEqual("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB", polymer_after_steps("NNCB", [
            "CH -> B",
            "HH -> N",
            "CB -> H",
            "NH -> C",
            "HB -> C",
            "HC -> B",
            "HN -> C",
            "NN -> C",
            "BH -> H",
            "NC -> B",
            "NB -> B",
            "BN -> B",
            "BB -> N",
            "BC -> B",
            "CC -> N",
            "CN -> C"
        ], 4))

    def test_polymer_hash(self):
        self.assertEqual(1588, polymer_hash("NNCB", [
            "CH -> B",
            "HH -> N",
            "CB -> H",
            "NH -> C",
            "HB -> C",
            "HC -> B",
            "HN -> C",
            "NN -> C",
            "BH -> H",
            "NC -> B",
            "NB -> B",
            "BN -> B",
            "BB -> N",
            "BC -> B",
            "CC -> N",
            "CN -> C"
        ], 10))

    def test_polymer_hash_real_iunput(self):
        with open('inputs/day_14.txt') as f:
            all_lines = f.read().splitlines()
            template = all_lines[0]
            substitutions = all_lines[2:]
        self.assertEqual(3408, polymer_hash(template, substitutions, 10))
