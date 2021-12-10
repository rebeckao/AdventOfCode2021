from unittest import TestCase

from challenges.day_08_seven_segment_search import number_of_identifiable_digits_in_output, wire_mapping, \
    as_sorted_string, digits_in_output


class Test(TestCase):
    def test_number_of_identifiable_digits_in_output(self):
        actual = number_of_identifiable_digits_in_output(
            ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
             "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
             "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
             "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
             "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
             "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
             "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
             "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
             "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
             "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"])
        self.assertEqual(26, actual)

    def test_number_of_identifiable_digits_in_output_real_input(self):
        with open('inputs/day_08.txt') as f:
            actual = number_of_identifiable_digits_in_output(f.read().splitlines())
            self.assertEqual(247, actual)

    def test_wire_mapping(self):
        actual = wire_mapping("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")
        expected = {
            "abcdeg": 0,
            "ab": 1,
            "acdfg": 2,
            "abcdf": 3,
            "abef": 4,
            "bcdef": 5,
            "bcdefg": 6,
            "abd": 7,
            "abcdefg": 8,
            "abcdef": 9
        }
        self.assertEqual(expected, actual)

    def test_as_sorted_string(self):
        self.assertEqual("abcdef", as_sorted_string("fedcba"))
        self.assertEqual("abc", as_sorted_string({"b", "c", "a"}))

    def test_digits_in_output(self):
        self.assertEqual(digits_in_output("be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"), 8394)
        self.assertEqual(digits_in_output("edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"), 9781)
        self.assertEqual(digits_in_output("fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg"), 1197)
        self.assertEqual(digits_in_output("fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb"), 9361)
        self.assertEqual(digits_in_output("aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea"), 4873)
        self.assertEqual(digits_in_output("fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb"), 8418)
        self.assertEqual(digits_in_output("dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe"), 4548)
        self.assertEqual(digits_in_output("bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef"), 1625)
        self.assertEqual(digits_in_output("egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb"), 8717)
        self.assertEqual(digits_in_output("gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"), 4315)

    def test_digits_in_output_real_input(self):
        with open('inputs/day_08.txt') as f:
            sum_of_outputs = sum([digits_in_output(digit_line) for digit_line in f.read().splitlines()])
            self.assertEqual(933305, sum_of_outputs)
