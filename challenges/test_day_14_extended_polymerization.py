from unittest import TestCase

from challenges.day_14_extended_polymerization import polymer_hash, polymer_after_steps, parse_substitutions, optimized_polymerization

example_substitutions = [
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
]


class Test(TestCase):
    substitutions = example_substitutions

    def test_polymer_after_steps(self):
        expected = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
        self.assertEqual(expected, polymer_after_steps("NNCB", parse_substitutions(example_substitutions), 4))

    def test_polymer_hash(self):
        self.assertEqual(1588, polymer_hash("NNCB", example_substitutions, 10))

    def test_polymer_hash_real_iunput(self):
        with open('inputs/day_14.txt') as f:
            all_lines = f.read().splitlines()
            template = all_lines[0]
            substitutions = all_lines[2:]
        self.assertEqual(3408, polymer_hash(template, substitutions, 10))

    def test_small_optimized_polymer_hash(self):
        self.assertEqual(1, optimized_polymerization("NNCB", example_substitutions, 1))
        self.assertEqual(1588, optimized_polymerization("NNCB", example_substitutions, 10))

    def test_large_polymer_hash(self):
        self.assertEqual(2188189693529, optimized_polymerization("NNCB", example_substitutions, 40))

    def test_optimized_polymer_hash_real_iunput(self):
        with open('inputs/day_14.txt') as f:
            all_lines = f.read().splitlines()
            template = all_lines[0]
            substitutions = all_lines[2:]
        self.assertEqual(3724343376942, optimized_polymerization(template, substitutions, 40))
