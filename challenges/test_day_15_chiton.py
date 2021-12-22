from unittest import TestCase

from challenges.day_15_chiton import lowest_risk_breath_first, risk_at_location, lowest_risk_large_cave


class Test(TestCase):
    def test_lowest_risk(self):
        self.assertEqual(5, lowest_risk_breath_first([
            "121",
            "131",
            "151",
        ]))
        self.assertEqual(38, lowest_risk_breath_first([
            "1163751742",
            "1381373672"
        ]))
        self.assertEqual(12, lowest_risk_breath_first([
            "11199",
            "99199",
            "11199",
            "19999",
            "11111",
        ]))
        self.assertEqual(14, lowest_risk_breath_first([
            "111999",
            "991999",
            "111999",
            "199999",
            "199999",
            "111111",
        ]))
        self.assertEqual(19, lowest_risk_breath_first([
            "111199",
            "999199",
            "111199",
            "199999",
            "191111",
            "191991",
            "111991"
        ]))
        self.assertEqual(40, lowest_risk_breath_first([
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581"
        ]))

    def test_lowest_risk_real_input(self):
        with open('inputs/day_15.txt') as f:
            all_lines = f.read().splitlines()
            self.assertEqual(589, lowest_risk_breath_first(all_lines))

    def test_risk_at_location(self):
        self.assertEqual(8, risk_at_location(["8"], 0, 0, 1, 1))
        self.assertEqual(1, risk_at_location(["8"], 1, 1, 1, 1))
        self.assertEqual(5, risk_at_location(["8"], 2, 4, 1, 1))
        self.assertEqual(9, risk_at_location([
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581"
        ], 49, 49, 10, 10))

    def test_lowest_risk_large_cave(self):
        self.assertEqual(315, lowest_risk_large_cave([
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581"
        ]))

    def test_lowest_risk_large_cave_real_input(self):
        with open('inputs/day_15.txt') as f:
            all_lines = f.read().splitlines()
            self.assertEqual(2885, lowest_risk_large_cave(all_lines))
